# Safety First

Before you run any script in this guide, read this page once. It takes three
minutes, and it's the most important page here.

If anything feels overwhelming, that's OK. Start small. Try the scripts on
dummy files first. You're in control.

## The golden rules

1. **Dry-run by default.** Every script shows you what it *would* do before it
   changes anything. Run it without `--apply` first, every time.
2. **Copies, never originals.** Scripts in this guide create new draft files.
   They never move, overwrite, or delete your manuscripts, cover files, or
   reader lists.
3. **Local only.** Nothing here connects to the internet. No email is sent, no
   post is published, no file is uploaded to KDP by a script. You do those
   steps yourself, when you're ready.
4. **No secrets.** Never put passwords, API keys, credit card numbers, or real
   reader addresses in any file in this guide. Example data files are clearly
   marked and contain fictional names only.
5. **Test on copies first.** Try each script on a small folder of dummy files
   before you point it at your real book files.

## What "dry-run" means

When you run a script like this:

```bash
python3 scripts/draft_newsletter.py --book "My Book" --update "Chapter 3 done"
```

it prints the draft to your screen and changes nothing on disk. Add
`--apply` to actually write the draft file:

```bash
python3 scripts/draft_newsletter.py --book "My Book" --update "Chapter 3 done" --apply
```

## Why local-first

Cloud tools are convenient, but they mean your drafts live on someone else's
server. This guide keeps everything on your computer: drafts, checklists, and
planners stay in folders you control. You copy them into MailerLite, Substack,
Amazon KDP, or your email app only when *you* choose to.

## What this guide is not

- It's not medical advice.
- It's not legal, tax, or publishing advice.
- It doesn't replace Amazon KDP — you still log into kdp.amazon.com yourself
  and click Publish.

Published by **Asdale Dynamics, LLC** — tested, local-first, no secrets.
