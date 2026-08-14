from pypdf import PdfReader
from docx import Document
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def read_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def read_docx(file_path):
    doc = Document(file_path)

    text = "\n".join(
        [paragraph.text for paragraph in doc.paragraphs]
    )

    return text


def read_csv(file_path):
    df = pd.read_csv(file_path)

    return df.to_string(index=False)


def read_excel(file_path):
    df = pd.read_excel(file_path)

    return df.to_string(index=False)


def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_text(text)