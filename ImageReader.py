from pathlib import Path
import easyocr

IMAGE_PATH = "input.png"     # change this if needed (e.g., "input.jpg")

reader = easyocr.Reader(['en'], gpu=False)   # set gpu=True if you have CUDA
lines = reader.readtext(IMAGE_PATH, detail=0)  # list of strings
Path("Text.txt").write_text("\n".join(lines), encoding="utf-8")

print("Saved OCR text to Text.txt")