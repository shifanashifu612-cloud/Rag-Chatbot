from fastapi import FastAPI
from routes.chat_routes import router as chat_router
from routes.upload_routes import router as upload_router
from memory.chat_memory import init_db

app = FastAPI(
    title="Production RAG Chatbot",
    version="1.0.0"
)
init_db()
app.include_router(chat_router)
app.include_router(upload_router)


@app.get("/")
async def root():
    return {"message": "RAG Chatbot API Running"}