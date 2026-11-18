# MarkItDown GUI

A simple GUI for converting files and URLs to Markdown using
[Microsoft MarkItDown](https://github.com/microsoft/markitdown).

- `app_tk.py`: desktop app (Tkinter)
- `app.py`: browser app (Gradio)

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app_tk.py
```

## Build the .exe

```powershell
python -m pip install pyinstaller
pyinstaller --onefile --windowed --collect-all markitdown --collect-all magika app_tk.py
```

The result is in `dist\app_tk.exe`.