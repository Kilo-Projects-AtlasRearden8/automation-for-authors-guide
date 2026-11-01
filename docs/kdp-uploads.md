# KDP Uploads

KDP (Kindle Direct Publishing) is Amazon's free self-publishing platform.
Uploading a book means filling in metadata, uploading your manuscript and
cover, and setting a price. This automation doesn't upload for you — it
prepares everything so the actual upload takes minutes instead of hours.

## What it does

`scripts/kdp_upload_prep.py` reads a small metadata JSON file, checks it
against KDP's public limits (description under 4000 characters, up to 7
keywords, up to 2 categories, valid ISBN shape, accepted file types), and
writes a pre-upload checklist plus a machine-readable manifest. It never
contacts Amazon and never uploads anything.

## Step by step

### 1. Look at the example metadata

`scripts/books.example.json` shows the shape. It uses a fictional book —
change every value to your own:

```json
{
  "title": "The Massive AI Manual",
  "subtitle": "AI explained like a friend would explain it",
  "author": "Dylan Asdale",
  "description": "A plain-English, step-by-step guide ...",
  "keywords": ["AI for beginners", "plain English AI"],
  "categories": ["Computers & Technology", "Self-Help"],
  "isbn": "",
  "manuscript_file": "manuscript.docx",
  "cover_file": "cover.jpg"
}
```

Save your own copy as `scripts/my-book.json` and fill in your real details.

**No personal data:** use your author name (pen names are fine), not your
home address or phone number.

### 2. Run the prep check (dry-run)

```bash
python3 scripts/kdp_upload_prep.py --metadata scripts/my-book.json
```

You'll see a checklist and any issues: too many keywords, a too-long
description, an unrecognized file extension, etc.

### 3. Fix issues, then write the prep files

```bash
python3 scripts/kdp_upload_prep.py --metadata scripts/my-book.json --apply
```

This writes:

- `kdp-prep/kdp-prep-checklist.md` — a human-readable checklist
- `kdp-prep/kdp-prep-manifest.json` — a machine-readable summary

Re-run until the checklist says "No issues found."

### 4. Upload at KDP yourself

Log into kdp.amazon.com and fill in the form. Copy your title, subtitle,
description, keywords, and categories from `kdp-prep/kdp-prep-checklist.md`.
Upload your manuscript file and cover file yourself. Set your price and click
Publish. The script never touches your KDP account.

## KDP limits to remember

| Field | Limit |
|-------|-------|
| Description | Up to 4,000 characters |
| Keywords | Up to 7 |
| Categories | Up to 2 |
| Manuscript | DOCX, PDF, EPUB, HTML, TXT, RTF, DOC |
| Cover | JPEG or TIFF recommended; 2500+ pixels on the longest side |
| ISBN | 10 or 13 digits (KDP can assign one free) |

## What the manifest looks like

```json
{
  "prepared_on": "2026-11-01",
  "title": "The Massive AI Manual",
  "author": "Dylan Asdale",
  "description_length": 187,
  "keyword_count": 7,
  "category_count": 2,
  "issues": [],
  "ready": true
}
```

## No-code alternative

Copy the checklist headings into a notebook or a notes app and tick them off
by hand before you log into KDP:

- [ ] Title and subtitle
- [ ] Author name
- [ ] Blurb under 4,000 characters
- [ ] Up to 7 keywords
- [ ] Up to 2 categories
- [ ] Manuscript file ready
- [ ] Cover file ready
- [ ] ISBN decided

Published by **Asdale Dynamics, LLC** — tested, local-first, no secrets.
