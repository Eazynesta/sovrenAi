# backend/app/llm.py
import requests

def generate_answer(chunks, question):
    context = "\n".join(chunks)
    prompt = f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    data = response.json()
    return data.get("response", "No response from LLM").strip()
