# Automating Author Admin

Beginner-friendly automation for author tasks: newsletter drafts, social
posts, KDP uploads, and reader emails — using free tools, step by step,
local-first. No coding experience required. No API keys, no secrets, no
personal data.

Written plain English, step by step, never condescending — like a friend
would explain it. Every script runs in dry-run mode by default: it shows
what it *would* do before changing anything.

## What's inside

| Folder | What's in it |
|--------|--------------|
| `docs/` | Beginner manuals in Markdown (plain English, step by step) |
| `static/` | A small HTML site you can open in any browser |
| `scripts/` | Small Python scripts (dry-run by default, write local drafts only) |
| `tests/` | Automated checks that prove the scripts work |

## Who this is for

Dylan Asdale is a registered nurse turned AI author and founder of
**Asdale Dynamics, LLC** (Indiana, formed October 2026). His book *The
Massive AI Manual* and hub site dylanasdale.github.io explain AI "like a
friend would." This guide is published by **Asdale Dynamics, LLC** as part
of its beginner-friendly AI education line.

## Quick start

1. Read `docs/safety.md` first — it explains the golden rules (dry-run by
   default, copies never originals, local only, no secrets).
2. Pick an automation and read its page in `docs/`:
   - `docs/newsletter-drafts.md` — newsletter drafts
   - `docs/social-posts.md` — social posts
   - `docs/kdp-uploads.md` — KDP uploads
   - `docs/reader-emails.md` — reader emails
3. Try any script in dry-run mode (safe, nothing changes):

   ```bash
   python3 scripts/draft_newsletter.py --book "My Book" --update "Chapter 3 done"
   ```

4. When you're comfortable, back up your folder and run with `--apply` to
   write a local draft file:

   ```bash
   python3 scripts/draft_newsletter.py --book "My Book" --update "Chapter 3 done" --apply
   ```

## What you need

- A computer (Windows, Mac, or Linux)
- Python 3 (built-in on Mac and Linux; free download from python.org on Windows)
- A web browser (to open the static site and visit KDP yourself)
- A text editor
- About an hour to walk through everything

## Printable automation planner

`docs/automation-planner.md` (also `static/automation-planner.html`) is a
weekly checklist you can print from your browser: File → Print.

## The four automations

- **Newsletter drafts** — draft newsletter emails locally before you send
  them (`draft_newsletter.py`)
- **Social posts** — draft posts for six platforms at once with character
  counts (`draft_social_posts.py`)
- **KDP uploads** — prep your book metadata with a pre-upload checklist
  (`kdp_upload_prep.py`)
- **Reader emails** — draft thank-you, ARC, and new-release emails locally
  (`draft_reader_email.py`)

Scripts never send email, never post to social media, and never upload to
KDP. You complete those steps yourself, when you're ready.

## Verification

```bash
python3 -m unittest discover -s tests     # 18 tests, all passing
python3 -m py_compile scripts/*.py        # compile OK
```

Open any file in `static/` directly in a web browser. No build step
required.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

## Safety promise

- Every script runs in dry-run mode by default: it prints a plan and
  changes nothing.
- Scripts write local draft files only. Originals are never moved or
  deleted.
- No secrets, API keys, or personal data are stored anywhere in this
  project. Example data files are clearly fictional.

Published by **Asdale Dynamics, LLC** — beginner-friendly AI education,
tested and local-first.
