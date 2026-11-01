# Printable Automation Planner

Print this page and fill it in by hand. It's your weekly reminder of which
author-admin tasks to do, when, and with which tool.

*Designed for Letter / A4 paper. Print from your browser:*
*File → Print → Landscape* (Portrait works fine too).

## A low-energy, ADHD-friendly approach

You don't have to do every task every week. In fact, please don't. Pick
**one day, pick one task**. Rest is built into the plan. If you miss a week,
that's fine — just start again where you are.

Energy tip: if a task feels too big, shrink it. "Draft a newsletter" can
become "write one sentence about what I'm working on." Small steps count.

## Your week at a glance

| Day | Task | Tool | Done |
|-----|------|------|------|
| Monday | Draft this week's newsletter (one paragraph is enough) | `draft_newsletter.py` | [&nbsp;] |
| Monday | Draft social posts for the week (one post is enough) | `draft_social_posts.py` | [&nbsp;] |
| Wednesday | Check KDP upload checklist (just look, no pressure to upload) | `kdp_upload_prep.py` | [&nbsp;] |
| Friday | Draft a reader email (thank-you, ARC, or new-release) | `draft_reader_email.py` | [&nbsp;] |
| Sunday | Rest — nothing required | — | [&nbsp;] |

## Monthly check-in

| Task | When | Done |
|------|------|------|
| Review last month's drafts — what got sent, what didn't (no guilt) | First Sunday of month | [&nbsp;] |
| Update `books.example.json` → your real `my-book.json` metadata | First Sunday of month | [&nbsp;] |
| Back up your `drafts/`, `kdp-prep/`, and `reader-emails/` folders | First Sunday of month | [&nbsp;] |
| Check your book's KDP page for sales and reviews | First Sunday of month | [&nbsp;] |

## Automation quick reference

| Task | Command (dry-run — safe, try this first) | Command (write file — add `--apply`) |
|------|------------------------------------------|--------------------------------------|
| Newsletter draft | `python3 scripts/draft_newsletter.py --book ... --update ...` | add `--apply` |
| Social posts | `python3 scripts/draft_social_posts.py --book ... --hook ... --link ...` | add `--apply` |
| KDP prep | `python3 scripts/kdp_upload_prep.py --metadata scripts/my-book.json` | add `--apply` |
| Reader email | `python3 scripts/draft_reader_email.py --type thank-you --reader ... --book ...` | add `--apply` |

## Notes

Use this space for ideas, link reminders, or reader names (first names only —
no addresses or order IDs):

______________________________________________________________

______________________________________________________________

______________________________________________________________

---

Planner published by **Asdale Dynamics, LLC** — tested, local-first, no
secrets. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
