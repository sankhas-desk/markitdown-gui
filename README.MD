<div align="center">

# 📝 MarkItDown GUI

### Drop in a messy document. Get clean Markdown out.

A friendly point-and-click front end for
[Microsoft MarkItDown](https://github.com/microsoft/markitdown), so you never have to touch the command line to convert files for LLMs, notes, or docs.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![UI](https://img.shields.io/badge/UI-Tkinter%20%7C%20Gradio-orange)

</div>

---

## ✨ What it does

Pick a file or paste a link, press a button, and get Markdown you can copy or save.

| 📄 Documents | 🌐 Web | 🖼️ Media & more |
|---|---|---|
| PDF | Web pages | Images (with optional AI descriptions) |
| Word (.docx) | YouTube URLs | Audio (needs ffmpeg) |
| PowerPoint | HTML | ZIP, EPub |
| Excel, CSV, JSON, XML | | |

The actual conversion is done by MarkItDown, so the supported formats are the ones it supports.

## 🧰 Two ways to use it

| | 🖥️ Desktop app | 🌍 Browser app |
|---|---|---|
| **File** | `app_tk.py` | `app.py` |
| **Built with** | Tkinter | Gradio |
| **Best for** | Quick, single conversions. Can be built into a `.exe` | Batch conversion (downloads a `.zip`) and optional OpenAI key for image descriptions |
| **Run it** | `python app_tk.py` | `python app.py`, then open http://127.0.0.1:7860 |

## 🚀 Quick start

```powershell
# 1. Get the code
git clone https://github.com/sankhas-desk/markitdown-gui.git
cd markitdown-gui

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Install dependencies
python -m pip install -r requirements.txt

# 4. Launch (pick one)
python app_tk.py     # desktop
python app.py        # browser
```

> **Tip:** If PowerShell blocks the activate script, run
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and try again.

## 📦 Build your own `.exe`

Turn the desktop app into a standalone Windows program:

```powershell
python -m pip install pyinstaller
pyinstaller --onefile --windowed --collect-all markitdown --collect-all magika app_tk.py
```

Your app appears at `dist\app_tk.exe`.

<details>
<summary>🛠️ Troubleshooting the build</summary>

- **The exe closes instantly:** rebuild without `--windowed` and run it from PowerShell to see the error.
- **Missing module errors:** add `--collect-all <module>` or `--hidden-import <module>` to the build command.
- **Weird failures on very new Python versions:** try Python 3.12 or 3.13 in a fresh venv.
- **Exe too big:** install `markitdown[pdf,docx]` instead of `[all]` in a fresh venv.
- **SmartScreen warning:** common for unsigned PyInstaller apps.

</details>

## 🔐 A note on safety

- Run the browser app on `localhost` only. Don't use `share=True` unless you really mean to expose it.
- Treat unknown files and URLs as untrusted, since conversion runs with your user's permissions.
- Never commit API keys. Enter them in the app at runtime.

## 🗺️ Roadmap

- [ ] Drag and drop files onto the window
- [ ] Batch-convert a whole folder from the desktop app
- [ ] Progress indicator for large files
- [ ] Settings for OpenAI / Azure Document Intelligence
- [ ] Custom app icon

Ideas and pull requests are welcome.

## 🙏 Credits

All the heavy lifting is done by [MarkItDown](https://github.com/microsoft/markitdown) from Microsoft.
This project is an independent GUI wrapper and is not affiliated with Microsoft.

---

<div align="center">
Made with ☕ by <a href="https://github.com/sankhas-desk">sankhas-desk</a>
</div>
