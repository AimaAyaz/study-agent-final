from sentence_transformers import SentenceTransformer

# Load a real embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
    """Return a vector embedding for the given text."""
    return model.encode(text).tolist()
