# Printable Automation Planner

Print this page and fill it in by hand. It's your weekly reminder of which
author-admin tasks to do, when, and with which tool.

*Designed for Letter / A4 paper. Print from your browser:*
`File → Print → Landscape` (or Portrait — both look fine).

## Your week at a glance

| Day | Task | Tool | Done |
|-----|------|------|------|
| Monday | Draft this week's newsletter | `draft_newsletter.py` | [ ] |
| Monday | Draft social posts for the week | `draft_social_posts.py` | [ ] |
| Wednesday | Check KDP upload checklist | `kdp_upload_prep.py` | [ ] |
| Friday | Draft a reader email | `draft_reader_email.py` | [ ] |
| Sunday | Rest — nothing required | — | [ ] |

You don't have to do every task every week. Pick one day, pick one task.

## Monthly check-in

| Task | When | Done |
|------|------|------|
| Review last month's drafts — what got sent, what didn't | First Sunday of month | [ ] |
| Update `books.example.json` → your real `my-book.json` metadata | First Sunday of month | [ ] |
| Back up your `drafts/`, `kdp-prep/`, and `reader-emails/` folders | First Sunday of month | [ ] |
| Check your book's KDP page for sales and reviews | First Sunday of month | [ ] |

## Automation quick reference

| Task | Command (dry-run) | Command (write file) |
|------|-------------------|----------------------|
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
