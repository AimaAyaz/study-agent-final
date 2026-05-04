import os
import faiss
import numpy as np
from embeddings_setup import embed_text

# Path to your notes folder
NOTES_PATH = "data/notes"

def load_notes():
    """Load all text files from data/notes."""
    notes = []
    filenames = []

    for filename in os.listdir(NOTES_PATH):
        if filename.endswith(".txt"):
            with open(os.path.join(NOTES_PATH, filename), "r", encoding="utf-8") as f:
                notes.append(f.read())
                filenames.append(filename)

    return notes, filenames


def build_vector_db():
    """Embed all notes and store them in a FAISS index."""
    notes, filenames = load_notes()

    embeddings = [embed_text(n) for n in notes]

    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

    return index, notes, filenames


def search_vector_db(query, index, notes, filenames, k=3):
    """Search for the top-k most relevant notes."""
    query_vec = embed_text(query)
    query_vec = np.array([query_vec]).astype("float32")

    distances, indices = index.search(query_vec, k)

    results = []
    for i in indices[0]:
        results.append(notes[i])

    return results
