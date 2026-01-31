import re
import numpy as np

_model = None

def get_embedding_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(
            "sentence-transformers/paraphrase-MiniLM-L3-v2"
        )
    return _model

def scrub_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '', text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'\b\d{10,}\b', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def secure_embed(text: str):
    model = get_embedding_model()
    emb = model.encode(text)
    emb = emb / np.linalg.norm(emb)
    noise = np.random.normal(0, 0.01, emb.shape)
    return (emb + noise).astype("float32")
