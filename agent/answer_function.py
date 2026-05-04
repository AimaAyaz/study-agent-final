from vector_db_setup import search_vector_db, build_vector_db
from local_llm_setup import run_llm

# Build the vector DB once when the agent starts
index, notes, filenames = build_vector_db()

def generate_answer(query: str):
    """Full pipeline: retrieve notes + run LLM."""
    
    # 1. Retrieve relevant notes
    retrieved_notes = search_vector_db(query, index, notes, filenames, k=3)

    # 2. Build the LLM prompt
    context_block = "\n\n".join(retrieved_notes)
    prompt = f"""
You are a helpful study assistant. 
Give a short, simple 2–3 sentence answer. 
Do NOT add extra details. 
Use only the most relevant note.


NOTES:
{context_block}

QUESTION:
{query}

ANSWER:
"""

    # 3. Run the LLM
    response = run_llm(prompt)

    return response

