#!/usr/bin/env python3
"""
A tiny CLI to convert YouTube links to MP3 by shelling out to the yt-dlp executable.

Requires:
  - yt-dlp on PATH (e.g., brew install yt-dlp or pipx install yt-dlp)
  - FFmpeg on PATH (brew install ffmpeg)
Optional:
  - Set FFMPEG_PATH env var to the FFmpeg binary directory; it will be passed to yt-dlp.

Usage:
  python ytmp3.py https://youtu.be/ID
  python ytmp3.py --out ~/Music --bitrate 192 https://youtube.com/watch?v=ID
  # Multiple links
  python ytmp3.py URL1 URL2 URL3
  # Read links from a text file (one per line)
  python ytmp3.py --from-file links.txt

Legal: Only download audio you have rights to. Respect YouTube Terms and local laws.
"""

import argparse
import os
import sys
from pathlib import Path
import subprocess
import shutil


def parse_args():
    p = argparse.ArgumentParser(description="Convert YouTube links to MP3 (yt-dlp CLI wrapper).")
    p.add_argument("urls", nargs="*", help="YouTube URLs")
    p.add_argument("--out", "-o", default=str(Path.cwd()), help="Output directory (default: current dir)")
    p.add_argument("--bitrate", "-b", type=int, default=192,
                   choices=[128, 160, 192, 256, 320], help="MP3 bitrate kbps")
    p.add_argument("--from-file", "-f", help="Path to a text file with one URL per line")
    p.add_argument("--verbose", "-v", action="store_true", help="Show yt-dlp logs")
    return p.parse_args()


def load_urls(args) -> list[str]:
    urls = list(args.urls)
    if args.from_file:
        path = Path(args.from_file)
        if not path.exists():
            sys.exit(f"File not found: {path}")
        with path.open("r", encoding="utf-8") as fh:
            urls.extend([line.strip() for line in fh if line.strip() and not line.startswith("#")])
    if not urls:
        sys.exit("No URLs provided. Pass URLs or --from-file.")
    return urls


def ensure_binaries():
    if not shutil.which("yt-dlp"):
        sys.exit("yt-dlp not found on PATH. Try: brew install yt-dlp  (or: brew install pipx && pipx install yt-dlp)")
    if not shutil.which("ffmpeg"):
        # Not fatal, because yt-dlp will still try, but this is the most common failure.
        print("Warning: ffmpeg not found on PATH. Install with: brew install ffmpeg", file=sys.stderr)


def build_command(out_dir: Path, bitrate: int, verbose: bool) -> list[str]:
    cmd = [
        "yt-dlp",
        "-f", "bestaudio/best",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", f"{bitrate}k",
        "--no-playlist",
        "-o", str(out_dir / "%(title).200B.%(ext)s"),
    ]
    ffmpeg_location = os.environ.get("FFMPEG_PATH")
    if ffmpeg_location:
        cmd.extend(["--ffmpeg-location", ffmpeg_location])

    if not verbose:
        cmd.extend(["--quiet", "--no-warnings"])
    return cmd


def main():
    args = parse_args()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    ensure_binaries()
    urls = load_urls(args)

    print(f"Output: {out_dir}")
    print(f"Bitrate: {args.bitrate} kbps")

    base_cmd = build_command(out_dir, args.bitrate, verbose=args.verbose)

    errors = 0
    for url in urls:
        print(f"\n▶ {url}")
        try:
            # Let yt-dlp handle progress UI; inherit stdout/stderr for user-friendly output
            subprocess.run(base_cmd + [url], check=True)
            print("✓ Done")
        except subprocess.CalledProcessError as e:
            errors += 1
            print(f"✗ Failed: {url}\n  → yt-dlp exit code {e.returncode}")
        except Exception as e:
            errors += 1
            print(f"✗ Unexpected error: {url}\n  → {e}")

    if errors:
        sys.exit(errors)


if __name__ == "__main__":
    main()
