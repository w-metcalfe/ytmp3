# ytmp3 — YouTube → MP3 (Lightweight CLI)

A tiny, cross‑platform command‑line tool that converts a YouTube link into an MP3 file using `yt-dlp` + FFmpeg. It’s fast, minimal, and easy to install without extra services.

> **Legal**: Only download audio you have the rights to (your own content, Creative Commons, or where permitted). You are responsible for complying with YouTube’s Terms of Service and local laws.

---

## Features

* 🎯 **Simple**: one command + a URL → MP3
* ⚡ **Fast**: uses `yt-dlp` with FFmpeg for reliable extraction & conversion
* 🧰 **Portable**: just Python + FFmpeg
* 🧪 **Scriptable**: batch convert multiple URLs or from a text file
* 🧹 **Clean outputs**: filenames based on video title; choose bitrate

---

## Prerequisites

* **Python** 3.9+ (Windows/macOS/Linux)
* **FFmpeg** in your `PATH` (or set `FFMPEG_PATH` env var)
* **yt-dlp** (installed via `pip` below)

---

## Repository layout

```
.
├── ytmp3.py         # The CLI script
└── README.md        # This file
```

---

## Quick start

Choose your OS and follow the steps. If you’re comfortable with virtual environments, you can create one before installing `yt-dlp`.

### macOS (Terminal)

1. **Install Python & FFmpeg** (Homebrew):

```bash
brew install python ffmpeg
```

2. **Clone & cd**:

```bash
git clone https://github.com/<you>/ytmp3.git
cd ytmp3
```

3. **Install dependency**:

```bash
python3 -m pip install --upgrade pip
pip3 install yt-dlp
```

4. **Run**:

```bash
python3 ytmp3.py "https://youtu.be/VIDEO_ID"
# or choose output dir + bitrate
python3 ytmp3.py --out ~/Music --bitrate 192 "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Linux (Terminal)

1. **Install FFmpeg**:

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y ffmpeg python3 python3-pip
# Fedora
sudo dnf install -y ffmpeg python3-pip
# Arch
sudo pacman -S --noconfirm ffmpeg python
```

2. **Clone & cd**:

```bash
git clone https://github.com/<you>/ytmp3.git
cd ytmp3
```

3. **Install dependency**:

```bash
python3 -m pip install --upgrade pip
pip3 install yt-dlp
```

4. **Run**:

```bash
python3 ytmp3.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Windows — PowerShell

1. **Install Python** ([https://python.org](https://python.org)) → check **Add Python to PATH**.
2. **Install FFmpeg** via `winget`:

```powershell
winget install --id=Gyan.FFmpeg -e
```

3. **Clone & cd**:

```powershell
git clone https://github.com/<you>/ytmp3.git
cd ytmp3
```

4. **Install dependency**:

```powershell
python -m pip install --upgrade pip
pip install yt-dlp
```

5. **Run**:

```powershell
python ytmp3.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Windows — Git Bash (MINGW64)

1. **Python availability**:

```bash
python --version || py --version || python3 --version
```

Use whichever exists (`python`, `py`, or `python3`).

2. **Install FFmpeg** (call the Windows tool from Git Bash):

```bash
winget.exe install --id=Gyan.FFmpeg -e
```

3. **Clone & cd**:

```bash
git clone https://github.com/<you>/ytmp3.git
cd ytmp3
```

4. **Install dependency**:

```bash
python -m pip install --upgrade pip
pip install yt-dlp
```

5. **Run**:

```bash
python ytmp3.py 'https://www.youtube.com/watch?v=VIDEO_ID'
# In Bash, you can also escape the ?
python ytmp3.py https://www.youtube.com/watch\?v=VIDEO_ID
```

> **Note on quoting in Bash**: URLs with `?` and `&` may need quotes or escaping (e.g., `\?`). PowerShell usually doesn’t need quotes for typical YouTube URLs.

---

## Usage

```bash
# Single link
python ytmp3.py https://youtu.be/ID

# Choose output folder and bitrate (kbps)
python ytmp3.py --out "~/Music" --bitrate 192 https://youtube.com/watch\?v=ID

# Multiple links in one go
python ytmp3.py URL1 URL2 URL3

# From a text file (one URL per line; lines starting with # are ignored)
python ytmp3.py --from-file links.txt --out ~/Music --bitrate 320

# Verbose logs (diagnostics)
python ytmp3.py -v https://youtu.be/ID
```

### CLI options

* `--out, -o`: output directory (default: current directory)
* `--bitrate, -b`: MP3 bitrate: `128`, `160`, `192`, `256`, `320` (default: `192`)
* `--from-file, -f`: read URLs from a text file (one per line; `#` comments allowed)
* `--verbose, -v`: show `yt-dlp` logs

---

## Optional: virtual environment

Recommended to keep your global Python clean.

```bash
# macOS/Linux/Git Bash
python3 -m venv .venv
source .venv/bin/activate
pip install yt-dlp

# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install yt-dlp
```

Deactivate with `deactivate`.

---

## Add a convenient alias

Make `ytmp3` a single command in your shell. Adjust paths if your repo lives elsewhere.

### macOS / Linux (zsh or bash)

Append this to your shell rc (`~/.zshrc` or `~/.bashrc`):

```bash
alias ytmp3='python3 ~/path/to/ytmp3/ytmp3.py'
```

Reload and use:

```bash
source ~/.zshrc   # or ~/.bashrc
ytmp3 https://youtu.be/VIDEO_ID
```

### Windows — PowerShell profile

Open your profile and add a function that mirrors arguments:

```powershell
notepad $PROFILE
```

Paste:

```powershell
function ytmp3 {
  python "C:\\path\\to\\ytmp3\\ytmp3.py" $args
}
```

Save, restart PowerShell (or run `. $PROFILE`), then:

```powershell
ytmp3 https://youtu.be/VIDEO_ID
```

### Windows — Git Bash alias

Append to `~/.bashrc`:

```bash
echo "alias ytmp3='python /c/path/to/ytmp3/ytmp3.py'" >> ~/.bashrc
source ~/.bashrc

ytmp3 'https://youtu.be/VIDEO_ID'
```

> **Tip**: On Git Bash, Windows paths map like `C:\\Users\\you\\...` → `/c/Users/you/...`.

---

## Keeping things up to date

* Update `yt-dlp` periodically (YouTube changes often):

```bash
pip install -U yt-dlp
```

* If you fork this repo, pull latest changes as needed:

```bash
git pull origin main
```

---

## Uninstall / removal

* Delete the cloned folder
* Remove the alias/function lines from your shell profile
* Optionally uninstall `yt-dlp` from the venv (or globally):

```bash
pip uninstall yt-dlp
```

* Remove FFmpeg if you installed it solely for this

---

## Troubleshooting

**`ffmpeg: command not found`**

* Ensure FFmpeg is installed and in PATH (`ffmpeg -version` should print info)
* Or set an env var so `yt-dlp` can find it:

  * macOS/Linux/Git Bash:

    ```bash
    export FFMPEG_PATH=/usr/local/bin   # adjust to your FFmpeg bin dir
    ```
  * Windows PowerShell:

    ```powershell
    $env:FFMPEG_PATH = "C:\\ffmpeg\\bin"
    ```

**`python: command not found` (Git Bash)**

* Try `py` or `python3` instead of `python`
* Confirm Python is installed and added to PATH

**Age‑restricted/private videos**

* This CLI doesn’t pass cookies; such videos may fail by design

**Slow or throttled downloads**

* Try again later or a different network; `yt-dlp` is resilient but bandwidth can vary

**Quoting in Bash**

* Use single quotes `'...'` or escape special characters (`\?`, `\&`), e.g.:

  ```bash
  python ytmp3.py 'https://www.youtube.com/watch?v=ID'
  # or
  python ytmp3.py https://www.youtube.com/watch\?v=ID
  ```

---

## FAQ

**Can I point outputs to a network drive or NAS?**  Yes — pass `--out` to any mounted path.

**Does it work on Unraid?**  Yes — install Python + FFmpeg via NerdTools, or run inside Docker. You can also SSH from another machine and execute the CLI on Unraid.

**Can I change the default bitrate?**  Yes — pass `--bitrate 128|160|192|256|320` per call. You can also wrap an alias that includes your preferred bitrate.

**Can I convert multiple links at once?**  Yes — pass multiple URLs or use `--from-file` with one URL per line.

---

## License

MIT (or your preferred license). Add a `LICENSE` file if you want to open‑source this.

---

## Credits

* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for robust extraction
* [FFmpeg](https://ffmpeg.org/) for audio transcoding
# ytmp3
