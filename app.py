import tempfile
import zipfile
from pathlib import Path

import gradio as gr
from markitdown import MarkItDown


def make_converter(api_key: str = "", model: str = "gpt-4o") -> MarkItDown:
    if api_key:
        from openai import OpenAI  # needs: python -m pip install openai
        return MarkItDown(llm_client=OpenAI(api_key=api_key), llm_model=model)
    return MarkItDown()


def convert_one(source: str, converter: MarkItDown) -> str:
    return converter.convert(source).text_content


def convert_many(paths, converter):
    out_dir = Path(tempfile.mkdtemp())
    log = []
    for p in map(Path, paths):
        try:
            text = convert_one(str(p), converter)
            (out_dir / f"{p.stem}.md").write_text(text, encoding="utf-8")
            log.append(f"OK  {p.name}")
        except Exception as e:
            log.append(f"FAIL {p.name}: {e}")
    zip_path = out_dir / "converted.zip"
    with zipfile.ZipFile(zip_path, "w") as z:
        for f in out_dir.glob("*.md"):
            z.write(f, f.name)
    return str(zip_path), "\n".join(log)


def single(file_path, url, api_key):
    url = (url or "").strip()
    source = url or file_path
    if not source:
        return "Provide a file or a URL.", None
    try:
        text = convert_one(source, make_converter(api_key))
    except Exception as e:
        return f"Error: {e}", None
    name = Path(file_path).stem if file_path and not url else "output"
    out = Path(tempfile.mkdtemp()) / f"{name}.md"
    out.write_text(text, encoding="utf-8")
    return text, str(out)


def batch(files, api_key):
    if not files:
        return None, "No files selected."
    return convert_many(files, make_converter(api_key))


with gr.Blocks(title="MarkItDown GUI") as demo:
    gr.Markdown("# MarkItDown GUI")
    api_key = gr.Textbox(label="OpenAI API key (optional, for image descriptions)",
                         type="password")

    with gr.Tab("Single"):
        f = gr.File(label="File", type="filepath")
        u = gr.Textbox(label="...or URL")
        btn = gr.Button("Convert", variant="primary")
        out_text = gr.Textbox(label="Markdown", lines=25)
        out_file = gr.File(label="Download .md")
        btn.click(single, [f, u, api_key], [out_text, out_file])

    with gr.Tab("Batch"):
        files = gr.File(label="Files", file_count="multiple", type="filepath")
        btn2 = gr.Button("Convert all", variant="primary")
        zip_out = gr.File(label="Download .zip")
        log = gr.Textbox(label="Log", lines=10)
        btn2.click(batch, [files, api_key], [zip_out, log])

if __name__ == "__main__":
    demo.launch()