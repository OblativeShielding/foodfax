from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import easyocr, re

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app, resources={r"/*": {"origins": "*"}})

reader = easyocr.Reader(['en'], gpu=False, verbose=False)

def parse_nutrition(text: str):
    t = text.lower()

    def gi(pat):
        m = re.search(pat, t, flags=re.I)
        return int(m.group(1)) if m else 0

    def gf_first(patterns):
        for pat in patterns:
            m = re.search(pat, t, flags=re.I)
            if m:
                return float(m.group(1))
        return 0.0

    fat_g = gf_first([
        r'\btotal\s+fat\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*g',          
        r'^(?:\s*)total\s+fat\s*(\d+(?:\.\d+)?)\s*g',              
        r'\bfat\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*g(?!.*trans)',        
    ])

    carbs_g = gf_first([
        r'\btotal\s+carbohydrate(?:s)?\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*g',
        r'\bcarb(?:ohydrate|s)?\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*g',
    ])

    protein_g = gf_first([
        r'\bprotein\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*g',
    ])

    return {
        "calories": gi(r'\bcalories?\s*[:\-]?\s*(\d{1,4})'),
        "fat_g": fat_g,
        "carbs_g": carbs_g,
        "protein_g": protein_g,
    }
@app.post("/ocr")
def ocr():
    f = request.files.get("image")
    if not f or f.filename == "":
        return jsonify({"error": "No file provided under form field 'image'."}), 400

    img_bytes = f.read()
    try:
        lines = reader.readtext(img_bytes, detail=0)
    except Exception as e:
        return jsonify({"error": f"OCR failed: {e}"}), 500

    text = "\n".join(lines)
    return jsonify({
        "parsed": parse_nutrition(text),
        "raw_text": text,
        "filename": f.filename
    })

@app.get("/")
def index():
    return send_from_directory(".", "foodFax.html")

if __name__ == "__main__":
    app.run(debug=True)