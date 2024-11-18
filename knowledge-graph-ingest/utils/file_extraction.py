import re

from docx import Document
import pymupdf4llm


def extract_pdf(file_path: str) -> str:
    """Return the text of a PDF file as a single string."""
    return pymupdf4llm.to_markdown(file_path)


def extract_docx(file_path: str) -> str:
    """Return the text of a PDF file as a single string."""
    reader = Document(file_path)
    text = "\n".join([para.text for para in reader.paragraphs])
    return text


def extract_patterns(text: str, pattern: str) -> list:
    """Extract the whole lines from a PDF file in which the specified pattern is found."""
    lines = text.split("\n")
    matches = [
        line.replace(".", "") for line in lines if re.search(pattern, line)
    ]
    return matches
