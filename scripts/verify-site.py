#!/usr/bin/env python3
"""Verify the static HTML site: every page parses and every internal link resolves.

Usage: python3 scripts/verify-site.py [path-to-site-dir]
Defaults to the site/ directory next to this script.
"""
import os
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "site")

errors = []
warnings = []


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "script" and attrs.get("src"):
            self.links.append(attrs["src"])


def is_external(url):
    return url.startswith(("http://", "https://", "mailto:", "tel:", "ftp://", "data:"))


def is_anchor(url):
    return url.startswith("#") or url == ""


def main():
    if not os.path.isdir(SITE):
        errors.append(f"site directory not found: {SITE}")
        print_fail()
        return 1

    html_files = []
    for dirpath, _dirnames, filenames in os.walk(SITE):
        for name in filenames:
            if name.endswith(".html"):
                html_files.append(os.path.join(dirpath, name))
    html_files.sort()

    if not html_files:
        errors.append(f"no .html files found under {SITE}")
        print_fail()
        return 1

    # 1. Every page parses cleanly and has a DOCTYPE, <html>, <head>, <body>.
    for path in html_files:
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        if not content.lstrip().startswith("<!DOCTYPE html>"):
            errors.append(f"{os.path.relpath(path, SITE)}: missing <!DOCTYPE html>")
        for required in ("<html", "<head", "<body"):
            if required not in content:
                errors.append(f"{os.path.relpath(path, SITE)}: missing {required}")
        # Parse to catch obvious markup errors.
        parser = LinkParser()
        try:
            parser.feed(content)
        except Exception as exc:  # pragma: no cover - defensive
            errors.append(f"{os.path.relpath(path, SITE)}: parse error: {exc}")
        # 2. Every link resolves to a real file or is an anchor/external.
        for link in parser.links:
            if is_external(link) or is_anchor(link):
                continue
            if link.startswith("/"):
                target = os.path.normpath(os.path.join(SITE, link.lstrip("/")))
            else:
                target = os.path.normpath(os.path.join(os.path.dirname(path), link))
            if not os.path.isfile(target):
                errors.append(
                    f"{os.path.relpath(path, SITE)}: broken link '{link}' "
                    f"-> {os.path.relpath(target, SITE)}"
                )

    # 3. Required pages exist.
    required = [
        "index.html", "employers.html", "opting-out.html", "never-paste.html",
        "safe-sharing.html", "checklist.html", "disclaimer.html",
    ]
    for page in required:
        if not os.path.isfile(os.path.join(SITE, page)):
            errors.append(f"missing required page: {page}")

    # 4. Required assets exist.
    for asset in ["css/style.css", "js/app.js"]:
        if not os.path.isfile(os.path.join(SITE, asset)):
            errors.append(f"missing required asset: {asset}")

    # 5. Required docs exist.
    docs_dir = os.path.join(ROOT, "docs")
    for doc in ["index.md", "what-employers-can-see.md", "opting-out-of-training.md",
                "never-paste-patient-payroll.md", "safe-sharing.md",
                "workplace-checklist.md", "disclaimer.md"]:
        if not os.path.isfile(os.path.join(docs_dir, doc)):
            warnings.append(f"missing docs file: {doc}")

    # 6. License and README exist with required copyright line.
    license_path = os.path.join(ROOT, "LICENSE")
    if not os.path.isfile(license_path):
        errors.append("missing LICENSE file")
    else:
        with open(license_path, "r", encoding="utf-8") as fh:
            lic = fh.read()
        if "Copyright (c) 2026 Asdale Dynamics, LLC" not in lic:
            errors.append("LICENSE missing exact copyright line: Copyright (c) 2026 Asdale Dynamics, LLC")

    readme_path = os.path.join(ROOT, "README.md")
    if not os.path.isfile(readme_path):
        errors.append("missing README.md")
    else:
        with open(readme_path, "r", encoding="utf-8") as fh:
            readme = fh.read()
        if "Asdale Dynamics, LLC" not in readme:
            errors.append("README does not credit Asdale Dynamics, LLC")

    print(f"Verified {len(html_files)} HTML page(s) under {os.path.relpath(SITE, ROOT)}")
    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        print_fail()
        return 1
    print("PASS: all pages parse, all links resolve, required files present.")
    return 0


def print_fail():
    for e in errors:
        print(f"ERROR: {e}")
    print(f"FAIL: {len(errors)} error(s)")


if __name__ == "__main__":
    sys.exit(main())