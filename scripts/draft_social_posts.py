#!/usr/bin/env python3
"""Draft social posts for your book.

Safety first: by default this runs in dry-run mode (prints the drafts, changes
nothing). With --apply it writes the drafts to a local Markdown file. It never
posts to any platform and never touches the internet.

Free tools used: a plain text editor and this script. No API keys required.
Character counts are rough guides — check each platform's current limit before
you post.
"""

import argparse
import sys
from pathlib import Path

DEFAULT_OUT = Path("drafts") / "social-posts-draft.md"

PLATFORMS = (
    ("Mastodon / Bluesky / Threads", 280),
    ("X / Twitter", 280),
    ("Instagram caption", 2200),
    ("Facebook post", 500),
    ("TikTok caption", 150),
    ("LinkedIn post", 1300),
)

TEMPLATE = """# Social Post Drafts — {book_title}

*Drafted {date}. Published by Asdale Dynamics, LLC — MIT License.*

These are drafts only. Copy them into each app yourself; this script never
posts anywhere. Character counts are approximate — check each platform's
current limit before publishing.

---

## {book_title}

{hook}

{link}

{hashtags}

---

## Platform drafts

{platforms}

---

**Reminder:** vary the wording a little for each platform, and never share
personal data (addresses, phone numbers, order IDs) in a public post.

Asdale Dynamics, LLC — tested, local-first, no secrets.
"""


def draft(book_title, hook, link, hashtags) -> str:
    platform_blocks = []
    for name, limit in PLATFORMS:
        body = f"{hook}\n\n{link}\n\n{hashtags}"
        platform_blocks.append(f"### {name} (limit ~{limit} chars)\n"
                               f"> {body}\n")
    return TEMPLATE.format(
        book_title=book_title,
        date="today",
        hook=hook,
        link=link,
        hashtags=hashtags,
        platforms="\n".join(platform_blocks),
    )


def run(book_title, hook, link, hashtags, out: Path, apply: bool) -> int:
    content = draft(book_title, hook, link, hashtags)

    mode = "APPLY (writing draft file)" if apply else "DRY-RUN (nothing changes)"
    print(f"Social post drafts: {book_title}")
    print(f"Mode: {mode}")
    print()

    if apply:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(f"Drafts written to: {out}")
        print("Copy each platform block into the app yourself. This script "
              "never posts to social media.")
    else:
        print(content)
        print()
        print("Dry-run complete. Re-run with --apply to write the draft file.")

    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Draft social posts for your book. Dry-run by default."
    )
    parser.add_argument("--book", required=True, help="Book title to promote")
    parser.add_argument("--hook", required=True,
                        help="The attention-grabbing opening line")
    parser.add_argument("--link", required=True,
                        help="Link to your book (Amazon, KDP, your site, etc.)")
    parser.add_argument("--hashtags", default="#amreading #indieauthor #newbook",
                        help="Hashtags to append to each draft")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help="Output draft file "
                             "(default: drafts/social-posts-draft.md)")
    parser.add_argument("--apply", action="store_true",
                        help="Actually write the draft file. Without this, "
                             "only the drafts are printed.")
    args = parser.parse_args(argv)
    return run(args.book, args.hook, args.link, args.hashtags,
               args.out, args.apply)


if __name__ == "__main__":
    sys.exit(main())
