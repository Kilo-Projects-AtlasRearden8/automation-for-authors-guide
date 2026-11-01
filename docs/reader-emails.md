# Reader Emails

Readers reply to books. Thank-you emails, advance reader copy (ARC) offers,
and new-release announcements build relationships — but writing each one from
scratch drains energy. This automation drafts them locally so you always have
a starting point.

## What it does

`scripts/draft_reader_email.py` drafts one of three email types:

- **thank-you** — for a reader who bought or read your book
- **arc** — offering an advance reader copy before launch
- **new-release** — announcing your book is live with a link

It never sends email — it writes a draft file you open, personalize, and send
from your own email app.

## Step by step

### 1. Try a thank-you draft (dry-run)

```bash
python3 scripts/draft_reader_email.py \
  --type thank-you \
  --reader "Alex" \
  --book "The Massive AI Manual"
```

Review it on screen. Nothing is saved yet.

### 2. Write the draft to a file

```bash
python3 scripts/draft_reader_email.py \
  --type thank-you \
  --reader "Alex" \
  --book "The Massive AI Manual" \
  --apply
```

This creates `reader-emails/email-draft.md`. Open it in any text editor,
change the wording to sound like you, then copy it into your email app and
send.

### 3. Try the other types

ARC offer:

```bash
python3 scripts/draft_reader_email.py \
  --type arc \
  --reader "Alex" \
  --book "The Massive AI Manual" \
  --apply
```

New-release announcement:

```bash
python3 scripts/draft_reader_email.py \
  --type new-release \
  --reader "Alex" \
  --book "The Massive AI Manual" \
  --link "https://example.com/book" \
  --apply
```

### 4. Use test names, not real data

While practicing, use names like "Alex" or "Example Reader." Never paste real
reader addresses, order IDs, or personal details into these files. When you
send for real, copy the draft into your email app and add the real address
there.

## Options you can use

| Option | What it does | Example |
|--------|--------------|---------|
| `--type` | Email type: thank-you, arc, new-release | `--type arc` |
| `--reader` | Reader's name | `--reader "Alex"` |
| `--book` | Book title (required) | `--book "My Book"` |
| `--author` | Name in the sign-off | `--author "Dylan Asdale"` |
| `--link` | Book link for new-release emails | `--link "https://example.com"` |
| `--out` | Where to write the draft | `--out reader-emails/august.md` |
| `--apply` | Actually write the file | (no value needed) |

## Example output (thank-you)

```md
Subject: Thank you for reading The Massive AI Manual

Hi Alex,

Thank you for reading The Massive AI Manual. It means a lot to me that you
spent your time with this story.

If you enjoyed it, a quick review on Amazon, Goodreads, or wherever you buy
books helps other readers find it — and it takes just a couple of minutes.

What are you reading next? I'd love to hear from you.

Warmly,

Dylan Asdale

---

Asdale Dynamics, LLC — beginner-friendly AI education for authors.
```

## A low-energy system

If email feels overwhelming, try this:

1. Keep one drafts folder (`reader-emails/`).
2. Draft one email per week with this script.
3. Send it on the same day each week (Tuesday mornings work well for many
   people).
4. If you don't hear back, that's fine — the email still did its job.

Published by **Asdale Dynamics, LLC** — tested, local-first, no secrets.
