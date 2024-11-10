import os, re
from pypdf import PdfReader
from docx import Document

def extract_pdfs(pdf_files: list) -> dict:
    # PDF files data extraction
    extractions_dict = {}
    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
        text = "".join([page.extract_text() for page in reader.pages])
        extractions_dict[os.path.basename(pdf_file)] = {"text": text}

    return extractions_dict

def extract_pdf(file_path: str) -> str:
    """Return the text of a PDF file as a single string."""
    reader = PdfReader(file_path)
    text = "".join("\n".join(page.extract_text() for page in reader.pages))
    return text

def extract_docx(file_path: str) -> str:
    """Return the text of a PDF file as a single string."""
    reader = Document(file_path)
    text = "\n".join([para.text for para in reader.paragraphs])
    return text


def extract_patterns(text: str, pattern: str) -> list:
    """Extract the whole lines from a PDF file in which the specified pattern is found."""
    lines = text.split("\n")
    matches = [line.replace(".", "") for line in lines if re.search(pattern, line)]
    return matches
