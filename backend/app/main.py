# backend/app/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.models import Question
from app.pdf_utils import extract_text_from_pdf
from app.embedder import embed_and_index, get_relevant_chunks
from app.llm import generate_answer

app = FastAPI()

# CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    embed_and_index(text)
    return {"message": "PDF uploaded and indexed successfully"}

@app.post("/ask")
async def ask_question(q: Question):
    chunks = get_relevant_chunks(q.question)
    answer = generate_answer(chunks, q.question)
    return {"answer": answer}
