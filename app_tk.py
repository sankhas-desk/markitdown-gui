import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from markitdown import MarkItDown

md = MarkItDown()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MarkItDown GUI")
        self.geometry("900x650")

        bar = tk.Frame(self)
        bar.pack(fill="x", padx=8, pady=8)
        tk.Button(bar, text="Open file...", command=self.open_file).pack(side="left")
        self.url = tk.Entry(bar)
        self.url.pack(side="left", fill="x", expand=True, padx=8)
        tk.Button(bar, text="Convert URL", command=self.convert_url).pack(side="left")
        tk.Button(bar, text="Save .md", command=self.save).pack(side="left", padx=(8, 0))

        self.text = scrolledtext.ScrolledText(self, wrap="word")
        self.text.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self.status = tk.Label(self, text="Ready", anchor="w")
        self.status.pack(fill="x", padx=8)

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.run(path)

    def convert_url(self):
        url = self.url.get().strip()
        if url:
            self.run(url)

    def run(self, source):
        self.status.config(text=f"Converting {source} ...")
        threading.Thread(target=self.worker, args=(source,), daemon=True).start()

    def worker(self, source):
        try:
            result = md.convert(source).text_content
            self.after(0, self.show, result)
        except Exception as e:
            msg = str(e)  # capture now; 'e' is deleted after this block
            self.after(0, self.fail, msg)

    def show(self, content):
        self.text.delete("1.0", "end")
        self.text.insert("1.0", content)
        self.status.config(text="Done")

    def fail(self, msg):
        messagebox.showerror("Error", msg)
        self.status.config(text="Failed")

    def save(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".md", filetypes=[("Markdown", "*.md")]
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", "end-1c"))
            self.status.config(text=f"Saved {path}")


if __name__ == "__main__":
    App().mainloop()