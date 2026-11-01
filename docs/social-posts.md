# Social Posts

Posting about your book on Instagram, Facebook, X/Twitter, TikTok, Bluesky,
Mastodon, Threads, or LinkedIn takes time — especially when you're rewriting
the same announcement for every app. This automation drafts all of them from
one hook, one link, and your hashtags.

## What it does

`scripts/draft_social_posts.py` creates draft posts for six platforms at once,
each with a rough character count so you can see if a post is too long. It
never posts anywhere — it just gives you drafts to copy into each app.

## Step by step

### 1. Try it in dry-run mode

```bash
python3 scripts/draft_social_posts.py \
  --book "The Massive AI Manual" \
  --hook "New cover reveal — what do you think?" \
  --link "https://example.com/book" \
  --hashtags "#amreading #indieauthor #newbook"
```

Review the drafts on screen. Nothing is saved yet.

### 2. Write the drafts to a file

```bash
python3 scripts/draft_social_posts.py \
  --book "The Massive AI Manual" \
  --hook "New cover reveal — what do you think?" \
  --link "https://example.com/book" \
  --hashtags "#amreading #indieauthor #newbook" \
  --apply
```

This creates `drafts/social-posts-draft.md`. Open it in any text editor.
Each platform has its own block:

- X / Twitter (~280 chars)
- Mastodon / Bluesky / Threads (~280 chars)
- Instagram caption (~2200 chars)
- Facebook post (~500 chars)
- TikTok caption (~150 chars)
- LinkedIn post (~1300 chars)

Character counts are approximate — check each platform's current limit before
you post.

### 3. Copy and post yourself

Open each app, paste the matching block, and hit post. Vary the wording a
little for each platform so it doesn't look identical everywhere. Never share
personal data (addresses, phone numbers, order IDs) in a public post.

## Options you can use

| Option | What it does | Example |
|--------|--------------|---------|
| `--book` | Book title (required) | `--book "My Book"` |
| `--hook` | Opening line (required) | `--hook "Cover reveal!"` |
| `--link` | Link to your book (required) | `--link "https://example.com"` |
| `--hashtags` | Hashtags appended to each draft | `--hashtags "#indieauthor"` |
| `--out` | Where to write the drafts | `--out drafts/socials.md` |
| `--apply` | Actually write the file | (no value needed) |

## A simple weekly rhythm

If you're not sure how often to post, start small:

| Day | What to post |
|-----|--------------|
| Monday | One line about what you're writing this week |
| Wednesday | A quote or tip from your book |
| Friday | Link to your book with a one-sentence blurb |
| Sunday | Rest — no posting required |

Consistency beats volume. One post a week is fine.

## No-code alternative

Open your notes app and write one "master post" per week. Copy it into each
app, tweaking the first sentence for that platform. The script automates the
copying and character counting; the ideas still come from you.

Published by **Asdale Dynamics, LLC** — tested, local-first, no secrets.
