# backend/app/pdf_utils.py
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text
