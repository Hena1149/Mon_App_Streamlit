import fitz  # PyMuPDF
import docx
from typing import Union

def extract_text_from_pdf(file_path: str) -> str:
    """Extrait le texte d'un fichier PDF."""
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_path: str) -> str:
    """Extrait le texte d'un fichier Word."""
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def process_uploaded_file(file_path: str) -> str:
    """Traite le fichier uploadé selon son type."""
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Type de fichier non supporté. Veuillez uploader un PDF ou DOCX.")

def extract_text_from_txt(file_path: str) -> str:
    """Extrait le texte d'un fichier TXT."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def process_uploaded_file(file_path: str) -> str:
    """Traite le fichier uploadé selon son type."""
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Type de fichier non supporté. Veuillez uploader un PDF, DOCX ou TXT.")
