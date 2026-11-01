# Welcome to Automating Author Admin

You wrote a book. Congratulations — that's the hard part.

Now comes the admin: newsletter drafts, social posts, KDP uploads, reader
emails. It can feel like a second job. This guide walks you through
automating those tasks with free tools, step by step, in plain English.
Nothing here requires coding experience, API keys, or paid subscriptions.

## Who this is for

Dylan Asdale is a registered nurse turned AI author and founder of
**Asdale Dynamics, LLC** (Indiana, formed October 2026). His book *The
Massive AI Manual* and hub site dylanasdale.github.io explain AI "like a
friend would": plain English, step by step, never condescending.

This guide is published by **Asdale Dynamics, LLC** as part of its
beginner-friendly AI education line. It's written for authors who want to
spend less time on admin and more time writing.

## The four automations

| Automation | What it does | Where |
|------------|--------------|-------|
| Newsletter drafts | Draft newsletter emails locally before you send | `docs/newsletter-drafts.md` |
| Social posts | Draft posts for multiple platforms with character counts | `docs/social-posts.md` |
| KDP uploads | Prep your book metadata with a pre-upload checklist | `docs/kdp-uploads.md` |
| Reader emails | Draft thank-you, ARC, and new-release emails locally | `docs/reader-emails.md` |

Plus:

- **Printable automation planner** — a weekly checklist you can print and fill
  in by hand: `docs/automation-planner.md` (also in `static/automation-planner.html`)
- **Glossary** — plain English terms: `docs/glossary.md`

## How this guide works

1. **Read safety first** — `docs/safety.md` explains the golden rules.
2. **Pick one automation** and read its page. Each page walks you through it
   step by step with example commands you can copy and paste.
3. **Try it in dry-run mode** — every script prints what it would do without
   changing anything.
4. **Run it for real** with `--apply` when you're comfortable. Scripts write
   local draft files only; they never send email, never post to social media,
   and never upload to KDP.

## What you need

- A computer (Windows, Mac, or Linux)
- Python 3 (built-in on Mac and Linux; free from python.org on Windows)
- A web browser (to open the static HTML site, and to visit KDP yourself)
- A text editor (Notepad, TextEdit, VS Code, or whatever you already use)
- About an hour to walk through everything

## Local-first, always

Everything in this guide runs on your computer. No uploads, no cloud accounts,
no secrets. Your drafts stay in folders on your machine until *you* decide to
copy them into your newsletter tool, social app, email app, or KDP.

This guide is published by **Asdale Dynamics, LLC** — tested, local-first, no
secrets. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
