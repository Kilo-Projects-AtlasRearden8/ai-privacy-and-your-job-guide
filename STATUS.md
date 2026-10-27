# STATUS

**Project:** AI Privacy at Work: A Beginner Manual — keeping work and health data private when using AI.
**Author/Publisher:** Asdale Dynamics, LLC (Indiana, formed October 2026).
**Status:** Complete. Verification passes. Committed to a local git repository (no remote, nothing pushed).

## What was built

A beginner manual (education only, not legal advice) covering five topics, in two formats:

1. `docs/` — the manual in Markdown (7 files):
   - `index.md` — introduction, who it is for, disclaimer
   - `what-employers-can-see.md` — company devices/networks, work-provided AI tools, personal accounts, what "can see" means in practice
   - `opting-out-of-training.md` — how to opt out, enterprise vs. free accounts, non-retroactive nature, what opt-out does not protect against
   - `never-paste-patient-payroll.md` — patient/health data (HIPAA context), payroll data, other confidential data, made-up-example alternatives, what to do if something is pasted
   - `safe-sharing.md` — what is okay to share, what to keep out, de-identification table, approved tools, keeping work/personal separate
   - `workplace-checklist.md` — printable before/during/after/incident checklist
   - `disclaimer.md` — education-only disclaimer

2. `site/` — a static HTML version of the same manual (no build step; open `site/index.html` in any browser):
   - `index.html`, `employers.html`, `opting-out.html`, `never-paste.html`, `safe-sharing.html`, `checklist.html`, `disclaimer.html`
   - `css/style.css` — responsive, accessible styling
   - `js/app.js` — nav highlight for current page, print-checklist button

3. `scripts/verify-site.py` — verification script (parses HTML with `html.parser`, checks all internal links resolve, required pages/assets/docs/license/README present).

4. `LICENSE` — MIT License with copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`.
5. `README.md` — credits Asdale Dynamics, LLC; lists contents, topics, and the education-only disclaimer.

## How to run it

- Open the site: `site/index.html` in any browser (or any page in `site/`).
- Run verification: `python3 scripts/verify-site.py` (from the project root).
- The manual text is also readable directly in `docs/`.

## Verification results

- `python3 scripts/verify-site.py` → **PASS**: 7 HTML pages verified; all pages parse, all internal links resolve, all required pages/assets/docs/license/README present. Exit code 0.
- Manual review: no secrets, API keys, passwords, SSNs, or personal data in any file. The only matches for secret-like terms are the guide's own warnings instructing users *not* to paste such data.
- No `.github/workflows` files, no remote repository, no push. Commit uses the existing git identity (`Dylan Asdale <dylanasdale@users.noreply.github.com>`) with a plain commit message and no Co-authored-by trailers.

## Known gaps

- The HTML site is hand-maintained; it is intentionally separate from `docs/`, so edits must be made in both places. A static-site generator (e.g., mkdocs, mdBook) was deliberately avoided to keep the project dependency-free and portable.
- The guide is education only and is not legal advice; it does not replace employer policies, HIPAA guidance, or qualified legal counsel.
- Content is U.S.-law oriented (HIPAA, common U.S. workplace tools); rules differ by jurisdiction and employer.
- No live link checking against the external web; the verification script only checks internal links and file presence.
- Accessibility: the site follows basic ARIA-friendly patterns (skip link, semantic nav, focus-visible styling) but has not been audited with an automated accessibility tool.