from services.file_service import (
    read_txt,
    chunk_text
)

from vectorstore.chroma_store import add_documents

text = read_txt("data/sample.txt")

chunks = chunk_text(text)

add_documents(chunks)

print(f"{len(chunks)} chunks stored successfully")