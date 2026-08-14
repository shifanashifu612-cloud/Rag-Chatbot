from fastapi import APIRouter, UploadFile
import os

from services.file_service import (
    read_pdf,
    read_txt,
    read_docx,
    read_csv,
    read_excel
)

from rag.chunking import split_text
from vectorstore.chroma_store import add_documents

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    extension = file.filename.split(".")[-1].lower()

    if extension == "pdf":
        text = read_pdf(file_path)

    elif extension == "txt":
        text = read_txt(file_path)

    elif extension == "docx":
        text = read_docx(file_path)

    elif extension == "csv":
        text = read_csv(file_path)

    elif extension in ["xlsx", "xls"]:
        text = read_excel(file_path)

    else:
        return {
            "error": "Unsupported file type"
        }

    chunks = split_text(text)

    add_documents(chunks)

    return {
        "message": "File uploaded successfully",
        "chunks_added": len(chunks)
    }