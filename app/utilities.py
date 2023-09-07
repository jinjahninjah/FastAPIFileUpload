import io

from pypdf import PdfReader


def extract_text(text):
    all_text = []
    reader = PdfReader(text)
    pages = reader.pages
    for page in pages:
        all_text.append(page.extract_text())
    return " ".join(all_text)