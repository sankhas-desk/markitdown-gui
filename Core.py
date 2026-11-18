import tempfile
import zipfile
from pathlib import Path
from markitdown import MarkItDown


def make_converter(api_key: str = "", model: str = "gpt-4o") -> MarkItDown:
    """Optional LLM support for image descriptions."""
    if api_key:
        from openai import OpenAI  # pip install openai
        return MarkItDown(llm_client=OpenAI(api_key=api_key), llm_model=model)
    return MarkItDown()


def convert_one(source: str, converter: MarkItDown) -> str:
    return converter.convert(source).text_content


def convert_many(paths: list[str], converter: MarkItDown):
    out_dir = Path(tempfile.mkdtemp())
    log = []
    for p in map(Path, paths):
        try:
            text = convert_one(str(p), converter)
            (out_dir / f"{p.stem}.md").write_text(text, encoding="utf-8")
            log.append(f"✔ {p.name}")
        except Exception as e:
            log.append(f"✘ {p.name}: {e}")
    zip_path = out_dir / "converted.zip"
    with zipfile.ZipFile(zip_path, "w") as z:
        for f in out_dir.glob("*.md"):
            z.write(f, f.name)
    return str(zip_path), "\n".join(log)