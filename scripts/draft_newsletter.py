#!/usr/bin/env python3
"""Draft a newsletter for your readers.

Safety first: by default this runs in dry-run mode (prints the draft, changes
nothing). With --apply it writes the draft to a local Markdown file. It never
sends email and never touches the internet.

Free tools used: a plain text editor and this script. No API keys required.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

DEFAULT_OUT = Path("drafts") / "newsletter-draft.md"

TEMPLATE = """# {title}

*{date}*

Hi {first_name},

{intro}

## What's new with {book_title}

{update}

{cta}

{closing}

{signoff}

---

*You're receiving this because you signed up for updates from {author_name}.
Not interested anymore? Just reply to this email and say "unsubscribe."*

Asdale Dynamics, LLC — beginner-friendly AI education for authors.
"""


def draft(title, first_name, intro, book_title, update, cta, closing,
          signoff, author_name) -> str:
    return TEMPLATE.format(
        title=title,
        date=date.today().isoformat(),
        first_name=first_name,
        intro=intro,
        book_title=book_title,
        update=update,
        cta=cta,
        closing=closing,
        signoff=signoff,
        author_name=author_name,
    )


def run(title, first_name, intro, book_title, update, cta, closing, signoff,
        author_name, out: Path, apply: bool) -> int:
    content = draft(title, first_name, intro, book_title, update, cta,
                    closing, signoff, author_name)

    mode = "APPLY (writing draft file)" if apply else "DRY-RUN (nothing changes)"
    print(f"Newsletter draft: {title}")
    print(f"Mode: {mode}")
    print(f"Recipient placeholder: {first_name}")
    print(f"Book: {book_title}")
    print()

    if apply:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(f"Draft written to: {out}")
        print("Open it in any text editor, review, then copy into your "
              "newsletter tool (MailerLite, Substack, ConvertKit, etc.)")
        print("This script never sends email.")
    else:
        print(content)
        print()
        print("Dry-run complete. Re-run with --apply to write the draft file.")

    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Draft a newsletter for your readers. Dry-run by default."
    )
    parser.add_argument("--book", required=True, help="Book title to feature")
    parser.add_argument("--update", required=True,
                        help="What's new with the book (short paragraph)")
    parser.add_argument("--first-name", default="Reader",
                        help="First name to address in the draft")
    parser.add_argument("--intro", default="I hope you're doing well.",
                        help="Opening paragraph of the newsletter")
    parser.add_argument("--cta", default="Grab your copy here: [your book link]",
                        help="Call to action line")
    parser.add_argument("--closing", default="Thanks for being a reader.",
                        help="Closing paragraph")
    parser.add_argument("--signoff", default="Warmly,",
                        help="Sign-off line")
    parser.add_argument("--author", default="Asdale Dynamics, LLC",
                        help="Author name shown in the unsubscribe line")
    parser.add_argument("--title", default="Your Newsletter",
                        help="Newsletter title / subject line idea")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help="Output draft file (default: drafts/newsletter-draft.md)")
    parser.add_argument("--apply", action="store_true",
                        help="Actually write the draft file. Without this, only the draft is printed.")
    args = parser.parse_args(argv)
    return run(args.title, args.first_name, args.intro, args.book,
               args.update, args.cta, args.closing, args.signoff,
               args.author, args.out, args.apply)


if __name__ == "__main__":
    sys.exit(main())
