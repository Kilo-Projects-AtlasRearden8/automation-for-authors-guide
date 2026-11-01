# STATUS

## What was built

A beginner-friendly manual and static HTML site for automating author admin,
published by Asdale Dynamics, LLC. Covers four automations using free tools,
step by step, plain English, local-first: newsletter drafts, social posts,
KDP uploads, and reader emails. Includes a printable automation planner.

**Project contents**

| Folder | Contents |
|--------|----------|
| `docs/` | Eight Markdown manuals: intro, safety, glossary, newsletter-drafts, social-posts, kdp-uploads, reader-emails, automation-planner |
| `static/` | A small HTML site: `index.html`, `intro.html`, `safety.html`, `glossary.html`, `newsletter-drafts.html`, `social-posts.html`, `kdp-uploads.html`, `reader-emails.html`, `automation-planner.html`, plus `style.css` (print styles for the planner) |
| `scripts/` | Four Python scripts: `draft_newsletter.py`, `draft_social_posts.py`, `kdp_upload_prep.py`, `draft_reader_email.py` — dry-run by default, write local drafts only, never send/post/upload |
| `scripts/` | Example data: `books.example.json`, `readers.example.json` (fictional data only) |
| `tests/` | Eighteen unit tests using the standard-library `unittest` framework |

**Safety design (core requirement)**

- Every script runs in dry-run mode by default: it prints what it would do and changes nothing.
- With `--apply`, scripts write local draft files only. Originals are never moved, overwritten, or deleted.
- Scripts never send email, never post to social media, never upload to KDP, and never touch the internet.
- No secrets, API keys, or personal data anywhere. Example data files use clearly fictional names.

## How to run it

**Prerequisites:** Python 3 (Windows, Mac, or Linux). No external packages required.

```bash
# 1. Read the safety rules first
#    (docs/safety.md or static/safety.html)

# 2. Run any script in dry-run mode (safe, nothing changes):
python3 scripts/draft_newsletter.py --book "My Book" --update "Chapter 3 done"
python3 scripts/draft_social_posts.py --book "My Book" --hook "Hook" --link "https://example.com"
python3 scripts/kdp_upload_prep.py --metadata scripts/books.example.json
python3 scripts/draft_reader_email.py --type thank-you --reader "Alex" --book "My Book"

# 3. When comfortable, back up your folder and run with --apply to write a local draft file:
python3 scripts/draft_newsletter.py --book "My Book" --update "Chapter 3 done" --apply
```

**Static site:** open any file in `static/` (e.g. `static/index.html`)
directly in a web browser. No build step required.

**Printable planner:** open `static/automation-planner.html` and choose
File → Print.

## Verification results

- `python3 -m py_compile scripts/*.py` → compile OK
- `python3 -m unittest discover -s tests` → **18 tests, 18 passed, 0 failed** (OK)
- `ruff check scripts/ tests/` → All checks passed
- `scripts/books.example.json` → valid JSON; prep check reports 0 issues
- End-to-end smoke tests with `--apply` on all four scripts → draft files written to `drafts/`, `kdp-prep/`, `reader-emails/`; dry-runs write nothing
- All ten `static/*.html` files → parse as valid HTML

## Known gaps

- Scripts prepare drafts and checklists locally; the final send/post/upload step is always done by the author in their own app or at kdp.amazon.com (intentional — no secrets, no network).
- No linter config file beyond running `ruff check` manually.
- KDP limits documented are public limits as of 2026; Amazon may change them — always double-check on kdp.amazon.com before publishing.
- Social character counts are approximate guides, not platform guarantees.
- `kdp_upload_prep.py` validates metadata shape and limits only; it does not inspect manuscript or cover file contents.
- Site is static HTML only; no search, no build pipeline.

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
