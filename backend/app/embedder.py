# backend/app/embedder.py
from sentence_transformers import SentenceTransformer
import faiss

CHUNK_SIZE = 500

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
chunks = []

def embed_and_index(text):
    global chunks, index
    # Chunk the text
    chunks.clear()
    index.reset()
    chunks.extend([text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)])
    # Embed and index
    embeddings = model.encode(chunks)
    index.add(embeddings)

def get_relevant_chunks(query, top_k=3):
    embedding = model.encode([query])
    D, I = index.search(embedding, top_k)
    return [chunks[i] for i in I[0]]
