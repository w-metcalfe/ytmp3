# ytmp3 — YouTube → MP3 (Lightweight CLI)

A tiny, cross-platform command-line tool that converts a YouTube link into an MP3 file using `yt-dlp` + FFmpeg. It’s fast, minimal, and easy to install without extra services.

> **Legal**: Only download audio you have the rights to (your own content, Creative Commons, or where permitted). You are responsible for complying with YouTube’s Terms of Service and local laws.

---

## Features

* 🎯 **Simple**: one command + a URL → MP3
* ⚡ **Fast**: uses `yt-dlp` with FFmpeg for reliable extraction & conversion
* 🧰 **Portable**: just Python + the `yt-dlp` CLI
* 🧪 **Scriptable**: batch convert multiple URLs or from a text file
* 🧹 **Clean outputs**: filenames based on video title; choose bitrate

---

## Prerequisites

* **Python** 3.9+ (Windows/macOS/Linux)
* **FFmpeg** in your `PATH` (or set `FFMPEG_PATH` env var)
* **yt-dlp** CLI installed via:

  * macOS: `brew install yt-dlp`
  * Linux: package manager or `pipx install yt-dlp`
  * Windows: `winget install yt-dlp`

---

## Repository layout

```
.
├── ytmp3.py         # The CLI script
└── README.md        # This file
```

---

## Quick start

### macOS (Terminal)

1. **Install dependencies** (Homebrew):

   ```bash
   brew install yt-dlp ffmpeg
   ```

2. **Clone & cd**:

   ```bash
   git clone https://github.com/<you>/ytmp3.git
   cd ytmp3
   ```

3. **Run**:

   ```bash
   python3 ytmp3.py "https://youtu.be/VIDEO_ID"
   # or choose output dir + bitrate
   python3 ytmp3.py --out ~/Music --bitrate 192 "https://www.youtube.com/watch?v=VIDEO_ID"
   ```

---

### Linux (Terminal)

1. **Install dependencies**:

   ```bash
   # Ubuntu/Debian
   sudo apt update && sudo apt install -y ffmpeg yt-dlp python3
   # Fedora
   sudo dnf install -y ffmpeg yt-dlp
   # Arch
   sudo pacman -S --noconfirm ffmpeg yt-dlp
   ```

2. **Clone & cd**:

   ```bash
   git clone https://github.com/<you>/ytmp3.git
   cd ytmp3
   ```

3. **Run**:

   ```bash
   python3 ytmp3.py "https://www.youtube.com/watch?v=VIDEO_ID"
   ```

---

### Windows — PowerShell

1. **Install dependencies**:

   ```powershell
   winget install yt-dlp
   winget install Gyan.FFmpeg
   ```

2. **Clone & cd**:

   ```powershell
   git clone https://github.com/<you>/ytmp3.git
   cd ytmp3
   ```

3. **Run**:

   ```powershell
   python ytmp3.py "https://www.youtube.com/watch?v=VIDEO_ID"
   ```

---

### Windows — Git Bash (MINGW64)

1. **Check Python availability**:

   ```bash
   python --version || py --version || python3 --version
   ```

2. **Install FFmpeg**:

   ```bash
   winget.exe install --id=Gyan.FFmpeg -e
   ```

3. **Install yt-dlp**:

   ```bash
   winget.exe install yt-dlp
   ```

4. **Clone & cd**:

   ```bash
   git clone https://github.com/<you>/ytmp3.git
   cd ytmp3
   ```

5. **Run**:

   ```bash
   python ytmp3.py 'https://www.youtube.com/watch?v=VIDEO_ID'
   ```

---

## Usage

```bash
# Single link
python ytmp3.py https://youtu.be/ID

# Choose output folder and bitrate (kbps)
python ytmp3.py --out "~/Music" --bitrate 192 https://youtube.com/watch\?v=ID

# Multiple links
python ytmp3.py URL1 URL2 URL3

# From a text file
python ytmp3.py --from-file links.txt --out ~/Music --bitrate 320

# Verbose logs
python ytmp3.py -v https://youtu.be/ID
```

### CLI options

* `--out, -o`: output directory (default: current directory)
* `--bitrate, -b`: MP3 bitrate: `128`, `160`, `192`, `256`, `320` (default: `192`)
* `--from-file, -f`: read URLs from a text file (one per line; `#` comments allowed)
* `--verbose, -v`: show `yt-dlp` logs

---

## Add a convenient alias

### macOS / Linux

Add to `~/.zshrc` or `~/.bashrc`:

```bash
alias ytmp3='python3 ~/path/to/ytmp3/ytmp3.py'
```

### Windows PowerShell

Edit your `$PROFILE`:

```powershell
function ytmp3 {
  python "C:\\path\\to\\ytmp3\\ytmp3.py" $args
}
```

---

## Keeping things up to date

Update yt-dlp periodically:

```bash
brew upgrade yt-dlp     # macOS/Linux (Homebrew)
winget upgrade yt-dlp   # Windows
pipx upgrade yt-dlp     # If installed via pipx
```

---

## Troubleshooting

**`yt-dlp: command not found`**
→ Ensure it’s installed via Homebrew, winget, or pipx and in your PATH.

**`ffmpeg: command not found`**
→ Install FFmpeg and ensure it’s in PATH (`ffmpeg -version` should print info).

**Quoting in Bash**
→ Use single quotes or escape special chars:

```bash
python ytmp3.py 'https://www.youtube.com/watch?v=ID'
```

---

## FAQ

**Can I still use pip install yt-dlp?**
Yes, but this project now uses the `yt-dlp` CLI directly, which is simpler and avoids Python packaging issues.

---

## License

MIT (or your preferred license).
