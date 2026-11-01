# Newsletter Drafts

A newsletter is an email you send to readers who signed up to hear from you.
It's one of the best ways to sell books, but staring at a blank "compose"
window is hard. This automation drafts your newsletter locally, so you always
have something to work from.

## What it does

`scripts/draft_newsletter.py` writes a newsletter draft Markdown file from a
book title, an update paragraph, and a few lines you choose. It never sends
email — it just gives you a draft to open in any text editor and copy into
your newsletter tool (MailerLite, Substack, ConvertKit, or your own email
app).

## Step by step

### 1. Try it in dry-run mode

Open your terminal in this folder and run:

```bash
python3 scripts/draft_newsletter.py \
  --book "The Massive AI Manual" \
  --update "Chapter 12 is finished, and the cover proof came back today." \
  --intro "I hope you're having a good week." \
  --cta "Pre-order here: https://example.com/book"
```

You'll see the full draft printed on screen. Nothing is saved yet — this is
your chance to review it.

### 2. Write the draft to a file

When you're happy with it, run with `--apply`:

```bash
python3 scripts/draft_newsletter.py \
  --book "The Massive AI Manual" \
  --update "Chapter 12 is finished, and the cover proof came back today." \
  --first-name "Reader" \
  --apply
```

This creates `drafts/newsletter-draft.md` (or whatever path you give with
`--out`). Open it in any text editor, tweak the wording, and then copy it
into your newsletter tool.

### 3. Personalize and send yourself

Copy the draft into MailerLite, Substack, ConvertKit, or your email app.
Replace `[your book link]` with your real link. Send it to yourself first to
check how it looks, then send to your list.

## Options you can use

| Option | What it does | Example |
|--------|--------------|---------|
| `--book` | Book title to feature | `--book "My Book"` |
| `--update` | What's new (required) | `--update "New cover reveal!"` |
| `--first-name` | Name in the greeting | `--first-name "Alex"` |
| `--intro` | Opening paragraph | `--intro "Hi there,"` |
| `--cta` | Call to action / link line | `--cta "Get it: https://example.com"` |
| `--closing` | Closing paragraph | `--closing "Thanks for reading."` |
| `--signoff` | Sign-off line | `--signoff "Warmly,"` |
| `--author` | Name in the unsubscribe line | `--author "Dylan Asdale"` |
| `--title` | Newsletter title / subject idea | `--title "October News"` |
| `--out` | Where to write the draft | `--out drafts/october.md` |
| `--apply` | Actually write the file | (no value needed) |

## Example output

```md
# October News

*2026-11-01*

Hi Alex,

I hope you're having a good week.

## What's new with The Massive AI Manual

Chapter 12 is finished, and the cover proof came back today.

Pre-order here: https://example.com/book

Thanks for reading.

Warmly,

---

*You're receiving this because you signed up for updates from Dylan Asdale.
Not interested anymore? Just reply to this email and say "unsubscribe."*

Asdale Dynamics, LLC — beginner-friendly AI education for authors.
```

## No-code alternative

If you don't want a script at all, keep a "newsletter template" document in
your notes app with placeholder sections:

1. Greeting
2. What's new this month
3. Book link / call to action
4. Closing and sign-off

Fill it in each time you send. The script just automates steps 1–4 into a
file.

Published by **Asdale Dynamics, LLC** — tested, local-first, no secrets.
