#!/usr/bin/env python3
"""
A tiny CLI to convert YouTube links to MP3.

Deps:
  pip install yt-dlp

Requires FFmpeg on PATH (https://ffmpeg.org/)
Optionally set FFMPEG_PATH env var to the FFmpeg binary directory.

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
import yt_dlp


def human_size(n: float) -> str:
    units = ["B", "KB", "MB", "GB"]
    i = 0
    while n >= 1024 and i < len(units) - 1:
        n /= 1024.0
        i += 1
    return f"{n:.1f} {units[i]}"


def build_downloader(out_dir: Path, bitrate: int, quiet: bool) -> yt_dlp.YoutubeDL:
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(out_dir / "%(title).200B.%(ext)s"),
        "noplaylist": True,  # keep CLI simple by default
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": str(bitrate),
            }
        ],
        "quiet": quiet,
        "no_warnings": quiet,
        "progress_hooks": [progress_hook],
    }
    ffmpeg_location = os.environ.get("FFMPEG_PATH")
    if ffmpeg_location:
        ydl_opts["ffmpeg_location"] = ffmpeg_location
    return yt_dlp.YoutubeDL(ydl_opts)


def progress_hook(status):
    if status.get("status") == "downloading":
        d = status
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        downloaded = d.get("downloaded_bytes", 0)
        if total:
            pct = downloaded / total * 100
            sys.stderr.write(f"\rDownloading: {pct:5.1f}%  ({human_size(downloaded)}/{human_size(total)})    ")
            sys.stderr.flush()
    elif status.get("status") == "finished":
        sys.stderr.write("\nDownloaded, converting to MP3…\n")
        sys.stderr.flush()


def parse_args():
    p = argparse.ArgumentParser(description="Convert YouTube links to MP3.")
    p.add_argument("urls", nargs="*", help="YouTube URLs")
    p.add_argument("--out", "-o", default=str(Path.cwd()), help="Output directory (default: current dir)")
    p.add_argument("--bitrate", "-b", type=int, default=192, choices=[128,160,192,256,320], help="MP3 bitrate kbps")
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


def main():
    args = parse_args()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    urls = load_urls(args)

    print(f"Output: {out_dir}")
    print(f"Bitrate: {args.bitrate} kbps")

    errors = 0
    with build_downloader(out_dir, args.bitrate, quiet=not args.verbose) as ydl:
        for url in urls:
            print(f"\n▶ {url}")
            try:
                info = ydl.extract_info(url, download=True)
                title = info.get("title", "audio")
                print(f"✓ Done: {title}.mp3")
            except yt_dlp.utils.DownloadError as e:
                errors += 1
                print(f"✗ Failed: {url}\n  → {e}")
            except Exception as e:
                errors += 1
                print(f"✗ Unexpected error: {url}\n  → {e}")

    if errors:
        sys.exit(errors)


if __name__ == "__main__":
    main()
