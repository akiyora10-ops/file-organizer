"""File organizer: sort files into folders by extension or date."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable

EXTENSION_GROUPS = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff"},
    "documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".odt"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"},
    "audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
    "video": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"},
    "code": {".py", ".js", ".ts", ".java", ".c", ".cpp", ".go", ".rs", ".html", ".css"},
}


def group_for_ext(ext: str) -> str:
    ext = ext.lower()
    for group, exts in EXTENSION_GROUPS.items():
        if ext in exts:
            return group
    return "other"


def organize_by_extension(src: Path, dry_run: bool = False) -> list[tuple[Path, Path]]:
    moves: list[tuple[Path, Path]] = []
    for item in src.iterdir():
        if not item.is_file():
            continue
        group = group_for_ext(item.suffix)
        dest_dir = src / group
        dest = dest_dir / item.name
        moves.append((item, dest))
        if not dry_run:
            dest_dir.mkdir(exist_ok=True)
            if dest.exists() and dest != item:
                stem, suffix = item.stem, item.suffix
                i = 1
                while (dest_dir / f"{stem}_{i}{suffix}").exists():
                    i += 1
                dest = dest_dir / f"{stem}_{i}{suffix}"
            shutil.move(str(item), str(dest))
    return moves


def organize_by_date(src: Path, dry_run: bool = False) -> list[tuple[Path, Path]]:
    moves: list[tuple[Path, Path]] = []
    for item in src.iterdir():
        if not item.is_file():
            continue
        mtime = datetime.fromtimestamp(item.stat().st_mtime)
        folder = f"{mtime.year:04d}-{mtime.month:02d}"
        dest_dir = src / folder
        dest = dest_dir / item.name
        moves.append((item, dest))
        if not dry_run:
            dest_dir.mkdir(exist_ok=True)
            if dest.exists() and dest != item:
                stem, suffix = item.stem, item.suffix
                i = 1
                while (dest_dir / f"{stem}_{i}{suffix}").exists():
                    i += 1
                dest = dest_dir / f"{stem}_{i}{suffix}"
            shutil.move(str(item), str(dest))
    return moves


def find_duplicates(src: Path) -> dict[str, list[Path]]:
    by_hash: dict[str, list[Path]] = defaultdict(list)
    for item in src.rglob("*"):
        if not item.is_file():
            continue
        h = hashlib.sha256()
        with item.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        by_hash[h.hexdigest()].append(item)
    return {k: v for k, v in by_hash.items() if len(v) > 1}


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Organize files in a directory.")
    parser.add_argument("path", nargs="?", default=".", help="directory to organize")
    parser.add_argument("--by", choices=["ext", "date"], default="ext", help="grouping strategy")
    parser.add_argument("--dry-run", action="store_true", help="print moves without doing them")
    parser.add_argument("--duplicates", action="store_true", help="find duplicate files")
    args = parser.parse_args(list(argv) if argv is not None else None)

    src = Path(args.path).resolve()
    if not src.is_dir():
        print(f"error: {src} is not a directory")
        return 1

    if args.duplicates:
        dupes = find_duplicates(src)
        if not dupes:
            print("No duplicates found.")
            return 0
        for h, files in dupes.items():
            print(h[:12], "->", ", ".join(str(f) for f in files))
        return 0

    if args.by == "ext":
        moves = organize_by_extension(src, dry_run=args.dry_run)
    else:
        moves = organize_by_date(src, dry_run=args.dry_run)

    for src_p, dst_p in moves:
        print(f"{src_p.name} -> {dst_p.relative_to(src)}")
    print(f"Organized {len(moves)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
