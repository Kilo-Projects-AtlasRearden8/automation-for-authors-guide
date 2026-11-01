#!/usr/bin/env python3
"""Prepare your book for a KDP upload.

Safety first: by default this runs in dry-run mode (prints a checklist, changes
nothing). With --apply it writes a prep checklist and a machine-readable
manifest to local files. It never uploads to KDP and never touches the internet.

This is a checklist helper, not a KDP uploader. You still log into
kdp.amazon.com yourself and click "Publish." No API keys or passwords are
ever needed.

Free tools used: this script plus any text editor.
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

DEFAULT_OUT_DIR = Path("kdp-prep")
MAX_DESCRIPTION_CHARS = 4000
MAX_KEYWORDS = 7
MAX_CATEGORIES = 2
VALID_MANUSCRIPT_EXTENSIONS = {".pdf", ".docx", ".doc", ".rtf", ".html", ".txt", ".epub"}
VALID_COVER_EXTENSIONS = {".jpg", ".jpeg", ".tif", ".tiff", ".png"}


def load_metadata(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate(metadata: dict) -> list:
    """Return a list of human-readable issues (empty when all good)."""
    issues = []

    title = (metadata.get("title") or "").strip()
    if not title:
        issues.append("Title is missing or empty.")

    author = (metadata.get("author") or "").strip()
    if not author:
        issues.append("Author / contributor name is missing or empty.")

    description = metadata.get("description") or ""
    if len(description) > MAX_DESCRIPTION_CHARS:
        issues.append(
            f"Description is {len(description)} characters; KDP allows "
            f"up to {MAX_DESCRIPTION_CHARS}."
        )

    keywords = metadata.get("keywords") or []
    if not isinstance(keywords, list):
        issues.append("Keywords must be a list.")
    elif len(keywords) > MAX_KEYWORDS:
        issues.append(
            f"You have {len(keywords)} keywords; KDP allows up to "
            f"{MAX_KEYWORDS}."
        )
    else:
        for i, kw in enumerate(keywords):
            if not isinstance(kw, str) or not kw.strip():
                issues.append(f"Keyword #{i + 1} is empty.")

    categories = metadata.get("categories") or []
    if not isinstance(categories, list):
        issues.append("Categories must be a list.")
    elif len(categories) > MAX_CATEGORIES:
        issues.append(
            f"You have {len(categories)} categories; KDP allows up to "
            f"{MAX_CATEGORIES}."
        )

    isbn = (metadata.get("isbn") or "").strip()
    if isbn:
        digits = "".join(ch for ch in isbn if ch.isdigit())
        if len(digits) not in (10, 13):
            issues.append(
                f"ISBN '{isbn}' doesn't look like a 10- or 13-digit ISBN."
            )

    manuscript = (metadata.get("manuscript_file") or "").strip()
    cover = (metadata.get("cover_file") or "").strip()

    if manuscript:
        ext = Path(manuscript).suffix.lower()
        if ext not in VALID_MANUSCRIPT_EXTENSIONS:
            issues.append(
                f"Manuscript '{manuscript}' has extension '{ext}'. "
                f"KDP accepts: {', '.join(sorted(VALID_MANUSCRIPT_EXTENSIONS))}."
            )
    else:
        issues.append("No manuscript_file listed.")

    if cover:
        ext = Path(cover).suffix.lower()
        if ext not in VALID_COVER_EXTENSIONS:
            issues.append(
                f"Cover '{cover}' has extension '{ext}'. KDP recommends "
                f"JPEG or TIFF."
            )
    else:
        issues.append("No cover_file listed.")

    return issues


def checklist_markdown(metadata: dict, issues: list, out_dir: Path) -> str:
    title = (metadata.get("title") or "Untitled").strip()
    lines = [
        f"# KDP Upload Prep — {title}",
        f"*Prepared {date.today().isoformat()}. Published by Asdale Dynamics, LLC — MIT License.*",
        "",
        (
            "This checklist helps you gather everything before you log into "
            "kdp.amazon.com and click Publish. This script never uploads to KDP."
        ),
        "",
        "## Your metadata",
        "",
        f"- **Title:** {title}",
        f"- **Subtitle:** {(metadata.get('subtitle') or '').strip() or '_(none)_'}",
        f"- **Author:** {metadata.get('author') or '_(none)_'}",
        (
            f"- **Description:** {len(metadata.get('description') or '')} characters "
            f"(KDP limit: {MAX_DESCRIPTION_CHARS})"
        ),
        (
            f"- **Keywords:** {len(metadata.get('keywords') or [])} "
            f"(KDP limit: {MAX_KEYWORDS})"
        ),
        (
            f"- **Categories:** {len(metadata.get('categories') or [])} "
            f"(KDP limit: {MAX_CATEGORIES})"
        ),
        f"- **ISBN:** {metadata.get('isbn') or '_(none — KDP can assign one free)_'}",
        f"- **Manuscript file:** {metadata.get('manuscript_file') or '_(none)_'}",
        f"- **Cover file:** {metadata.get('cover_file') or '_(none)_'}",
        "",
        "## Before you upload",
        "",
        "- [ ] Manuscript is formatted and proofread",
        (
            "- [ ] Cover meets KDP specs (JPEG/TIFF, 2500+ pixels on the longest "
            "side recommended)"
        ),
        "- [ ] Description is under 4000 characters",
        "- [ ] You have up to 7 keywords",
        "- [ ] You have up to 2 categories",
        "- [ ] ISBN ready (or let KDP assign a free one)",
        "- [ ] You're logged into kdp.amazon.com",
        "",
        "## Results",
        "",
    ]

    if issues:
        lines.append(f"Issues to fix before upload: {len(issues)}")
        lines.append("")
        for i, issue in enumerate(issues, 1):
            lines.append(f"{i}. {issue}")
        lines.append("")
        lines.append("Fix these items, then re-run this script to confirm "
                     "the checklist is clean.")
    else:
        lines.append("No issues found. Your metadata looks ready for the KDP "
                     "upload form.")
        lines.append("")
        lines.append("You still need to log into kdp.amazon.com and complete "
                     "the upload yourself.")

    lines.extend([
        "",
        "---",
        "Asdale Dynamics, LLC — tested, local-first, no secrets.",
    ])
    return "\n".join(lines) + "\n"


def manifest_json(metadata: dict, issues: list) -> dict:
    return {
        "prepared_on": date.today().isoformat(),
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "description_length": len(metadata.get("description") or ""),
        "keyword_count": len(metadata.get("keywords") or []),
        "category_count": len(metadata.get("categories") or []),
        "issues": issues,
        "ready": len(issues) == 0,
    }


def run(metadata_path: Path, out_dir: Path, apply: bool) -> int:
    metadata = load_metadata(metadata_path)
    issues = validate(metadata)

    mode = "APPLY (writing prep files)" if apply else "DRY-RUN (nothing changes)"
    print(f"KDP upload prep: {metadata.get('title') or 'Untitled'}")
    print(f"Mode: {mode}")
    print(f"Issues found: {len(issues)}")
    print()

    if apply:
        out_dir.mkdir(parents=True, exist_ok=True)
        md_path = out_dir / "kdp-prep-checklist.md"
        json_path = out_dir / "kdp-prep-manifest.json"
        md_path.write_text(checklist_markdown(metadata, issues, out_dir),
                           encoding="utf-8")
        json_path.write_text(json.dumps(manifest_json(metadata, issues),
                                        indent=2, ensure_ascii=False),
                             encoding="utf-8")
        print(f"Checklist written to: {md_path}")
        print(f"Manifest written to: {json_path}")
        print("Review the checklist, fix any issues, then upload at "
              "kdp.amazon.com yourself.")
    else:
        print(checklist_markdown(metadata, issues, out_dir))
        print()
        print("Dry-run complete. Re-run with --apply to write the prep files.")

    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Prepare your book for a KDP upload. Dry-run by default."
    )
    parser.add_argument("--metadata", required=True,
                        help="Path to book metadata JSON (see books.example.json)")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT_DIR,
                        help="Output folder for prep files "
                             "(default: kdp-prep/)")
    parser.add_argument("--apply", action="store_true",
                        help="Actually write the prep files. Without this, "
                             "only the checklist is printed.")
    args = parser.parse_args(argv)
    return run(Path(args.metadata), args.out, args.apply)


if __name__ == "__main__":
    sys.exit(main())
