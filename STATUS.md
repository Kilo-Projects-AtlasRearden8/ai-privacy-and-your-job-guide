# STATUS

**Project:** AI Privacy at Work: A Beginner Manual — keeping work and health data private when using AI.
**Author/Publisher:** Asdale Dynamics, LLC (Indiana, formed October 2026).
**Status:** Complete. Verification passes. Committed to a local git repository (no remote, nothing pushed).

## Critical review against the original goal

The manual covers every required topic:
- What employers can see ✓
- Opting out of training ✓
- Never paste patient or payroll info ✓
- Safe sharing ✓
- Workplace checklist ✓
- Education only, not legal advice ✓ (disclaimers in README, docs/index.md, docs/disclaimer.md, and every HTML page)

Style targets met:
- Plain English, step by step, warm ("like a friend would"), never condescending ✓
- Beginner-friendly, no technical background assumed ✓
- Local-first (static HTML, no build step, no dependencies) ✓
- No secrets, API keys, or personal data in files ✓
- MIT LICENSE with exact line `Copyright (c) 2026 Asdale Dynamics, LLC` ✓
- Asdale Dynamics, LLC credited in README ✓
- No `.github/workflows` files ✓
- Existing git identity only, plain commit messages, no Co-authored-by trailers ✓

Improvements made during review:
- README rewritten to be warmer and more substantive: credits Asdale Dynamics prominently, mentions Dylan Asdale (registered nurse turned AI author), the book *The Massive AI Manual*, and hub site dylanasdale.github.io; adds "Where to start," "Who this is for," "About Asdale Dynamics, LLC," and "How to run" sections.
- Added `@media print` CSS to `site/css/style.css` so the workplace checklist prints cleanly (hides nav/buttons, keeps checklist boxes).
- Re-ran verification after changes; still passes.

## What was built

1. `docs/` — Markdown manual (7 files):
   - `index.md` — introduction, who it is for, disclaimer
   - `what-employers-can-see.md` — company devices/networks, work-provided AI tools, personal accounts, what "can see" means in practice
   - `opting-out-of-training.md` — how to opt out, enterprise vs. free accounts, non-retroactive nature, what opt-out does not protect against
   - `never-paste-patient-payroll.md` — patient/health data (HIPAA context), payroll data, other confidential data, made-up-example alternatives, what to do if something is pasted
   - `safe-sharing.md` — what is okay to share, what to keep out, de-identification table, approved tools, keeping work/personal separate
   - `workplace-checklist.md` — printable before/during/after/incident checklist
   - `disclaimer.md` — education-only disclaimer

2. `site/` — static HTML version of the same manual (open `site/index.html` in any browser):
   - `index.html`, `employers.html`, `opting-out.html`, `never-paste.html`, `safe-sharing.html`, `checklist.html`, `disclaimer.html`
   - `css/style.css` — responsive, accessible styling + print stylesheet
   - `js/app.js` — nav highlight for current page, print-checklist button

3. `scripts/verify-site.py` — verification script (parses HTML with `html.parser`, checks all internal links resolve, required pages/assets/docs/license/README present).

4. `LICENSE` — MIT License with copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`.
5. `README.md` — credits Asdale Dynamics, LLC; lists contents, topics, how to run, education-only disclaimer.
6. `STATUS.md` — this file.

## How to run it

- Open the site: `site/index.html` in any browser (or any page in `site/`).
- Print the checklist: open `site/checklist.html` and use your browser's Print command (print CSS applied automatically).
- Read the manual text directly in `docs/`.
- Run verification: `python3 scripts/verify-site.py` (from the project root).

## Verification results

- `python3 scripts/verify-site.py` → **PASS**: 7 HTML pages verified; all pages parse, all internal links resolve, all required pages/assets/docs/license/README present. Exit code 0.
- Manual scan: no secrets, API keys, passwords, SSNs, or personal data in any file. The only matches for secret-like terms are the guide's own warnings instructing users *not* to paste such data.
- No `.github` directory or workflow files. No remote repository. No push. Commit uses the existing git identity (`Dylan Asdale <dylanasdale@users.noreply.github.com>`) with plain commit messages and no Co-authored-by trailers.

## Known gaps

- The HTML site is hand-maintained; it is intentionally separate from `docs/`, so edits must be made in both places. A static-site generator was deliberately avoided to keep the project dependency-free and portable.
- The guide is education only and is not legal advice; it does not replace employer policies, HIPAA guidance, or qualified legal counsel.
- Content is U.S.-law oriented (HIPAA, common U.S. workplace tools); rules differ by jurisdiction and employer.
- No live link checking against the external web; the verification script only checks internal links and file presence.
- Accessibility: the site follows basic patterns (skip link, semantic nav, focus-visible styling) but has not been audited with an automated accessibility tool.
- The broader LLC catalog (AI tools, agents/MCP, local AI, free AI coding, GitHub, automation, small-business/author tools, life-admin helpers, healthcare-worker aids, FFXIV/chess tools) is referenced in the README but not yet built — this repo covers the privacy manual only.
