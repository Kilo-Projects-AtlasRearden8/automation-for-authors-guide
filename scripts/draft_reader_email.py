#!/usr/bin/env python3
"""Draft reader emails (thank-you, ARC, new release).

Safety first: by default this runs in dry-run mode (prints the draft, changes
nothing). With --apply it writes the draft to a local Markdown file. It never
sends email and never touches the internet.

Free tools used: this script plus any text editor or email app. No API keys
required, and never your readers' real addresses.
"""

import argparse
import sys
from pathlib import Path

DEFAULT_OUT = Path("reader-emails") / "email-draft.md"

TEMPLATES = {
    "thank-you": """Subject: Thank you for reading {book_title}

Hi {reader_name},

Thank you for reading {book_title}. It means a lot to me that you spent your
time with this story.

If you enjoyed it, a quick review on Amazon, Goodreads, or wherever you buy
books helps other readers find it — and it takes just a couple of minutes.

What are you reading next? I'd love to hear from you.

Warmly,
{author_name}

---

Asdale Dynamics, LLC — beginner-friendly AI education for authors.
""",
    "arc": """Subject: Advance reader copy: {book_title}

Hi {reader_name},

I'm putting together advance reader copies (ARCs) of {book_title} before it
launches, and I'd love to send you one.

In exchange, I only ask for an honest review when the book goes live — and
you're under no obligation to review if the book isn't your thing.

Would you like a copy? Reply to this email and I'll send the file your way.

Warmly,
{author_name}

---

Asdale Dynamics, LLC — beginner-friendly AI education for authors.
""",
    "new-release": """Subject: New release: {book_title} is live

Hi {reader_name},

{book_title} is now available! You can find it here: {link}

Thank you for being a reader. If you have a moment to leave a review, it
helps more readers discover the book.

Happy reading,
{author_name}

---

Asdale Dynamics, LLC — beginner-friendly AI education for authors.
""",
}


def draft(email_type, reader_name, book_title, author_name, link) -> str:
    if email_type not in TEMPLATES:
        raise ValueError(f"Unknown email type: {email_type}")
    return TEMPLATES[email_type].format(
        reader_name=reader_name,
        book_title=book_title,
        author_name=author_name,
        link=link or "[your book link]",
    )


def run(email_type, reader_name, book_title, author_name, link, out: Path,
        apply: bool) -> int:
    content = draft(email_type, reader_name, book_title, author_name, link)

    mode = "APPLY (writing draft file)" if apply else "DRY-RUN (nothing changes)"
    print(f"Reader email ({email_type}): {book_title}")
    print(f"Mode: {mode}")
    print(f"Reader: {reader_name}")
    print()

    if apply:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(f"Draft written to: {out}")
        print("Copy the draft into your email app, personalize, and send "
          "yourself. This script never sends email.")
    else:
        print(content)
        print()
        print("Dry-run complete. Re-run with --apply to write the draft file.")

    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Draft reader emails. Dry-run by default."
    )
    parser.add_argument("--type", choices=sorted(TEMPLATES),
                        default="thank-you",
                        help="Email type: thank-you, arc, or new-release")
    parser.add_argument("--reader", default="Reader",
                        help="Reader's name (use a test name, not real data)")
    parser.add_argument("--book", required=True, help="Book title")
    parser.add_argument("--author", default="Asdale Dynamics, LLC",
                        help="Author name used in the sign-off")
    parser.add_argument("--link", default="",
                        help="Book link for new-release emails")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help="Output draft file "
                             "(default: reader-emails/email-draft.md)")
    parser.add_argument("--apply", action="store_true",
                        help="Actually write the draft file. Without this, "
                             "only the draft is printed.")
    args = parser.parse_args(argv)
    return run(args.type, args.reader, args.book, args.author, args.link,
               args.out, args.apply)


if __name__ == "__main__":
    sys.exit(main())
