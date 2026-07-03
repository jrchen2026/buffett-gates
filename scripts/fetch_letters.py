#!/usr/bin/env python3
"""Build a local corpus of Berkshire Hathaway shareholder letters (1977-2024).

Downloads from berkshirehathaway.com (HTML for early years, PDF for later
years), converts everything to plain markdown with a YAML header.

Usage:
    python fetch_letters.py [--outdir corpus/letters] [--from 1977] [--to 2024]

Dependencies (install once):
    pip install requests beautifulsoup4 lxml pypdf

The letters themselves are copyrighted by Berkshire Hathaway; this script
builds a personal research corpus and the corpus should not be redistributed.
"""

import argparse
import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

BASE = "https://www.berkshirehathaway.com/letters/"
HEADERS = {"User-Agent": "Mozilla/5.0 (corpus builder; personal research use)"}


def candidates(year: int) -> list[str]:
    """Possible file names per year -- the site's naming drifted over time."""
    if year <= 1997:
        return [f"{year}.html"]
    if year <= 2001:
        return [f"{year}htm.html", f"{year}letter.html", f"{year}.html", f"{year}pdf.pdf"]
    return [f"{year}ltr.pdf", f"{year}pdf.pdf"]


def fetch(year: int, raw_dir: Path) -> Path | None:
    for name in candidates(year):
        dest = raw_dir / name
        if dest.exists():
            return dest
        try:
            r = requests.get(BASE + name, headers=HEADERS, timeout=30)
        except requests.RequestException:
            continue
        if r.status_code == 200 and len(r.content) > 5000:
            dest.write_bytes(r.content)
            return dest
    return None


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def html_to_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8", "windows-1252", "latin-1"):
        try:
            html = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text("\n")


def pdf_to_text(path: Path) -> str:
    reader = PdfReader(str(path))
    return "\n\n".join(page.extract_text() or "" for page in reader.pages)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--outdir", default="corpus/letters", help="output root")
    ap.add_argument("--from", dest="start", type=int, default=1977)
    ap.add_argument("--to", dest="end", type=int, default=2024)
    args = ap.parse_args()

    root = Path(args.outdir)
    raw_dir = root / "raw"
    md_dir = root / "md"
    raw_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    ok, failed = 0, []
    for year in range(args.start, args.end + 1):
        src = fetch(year, raw_dir)
        if src is None:
            failed.append(year)
            print(f"{year}  FAILED to download", file=sys.stderr)
            continue
        text = pdf_to_text(src) if src.suffix == ".pdf" else html_to_text(src)
        text = clean_text(text)
        header = (
            f"---\nyear: {year}\n"
            f"title: Berkshire Hathaway Shareholder Letter {year}\n"
            f"source: berkshirehathaway.com/letters/{src.name}\n---\n\n"
        )
        (md_dir / f"{year}.md").write_text(header + text, encoding="utf-8")
        flag = "  <-- SUSPICIOUS (too short)" if len(text) < 10000 else ""
        print(f"{year}  {src.suffix[1:]:4s}  {len(text):>7,} chars{flag}")
        ok += 1

    print(f"\n{ok} letters -> {md_dir}")
    if failed:
        print(f"failed years: {failed} -- download manually into {raw_dir} and rerun")


if __name__ == "__main__":
    main()
