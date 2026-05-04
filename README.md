# 📘 Study Agent — Retrieval‑Augmented AI Study Assistant

The **Study Agent** is a lightweight Retrieval‑Augmented Generation (RAG) system designed to help students understand machine learning concepts using their own study notes.  
It embeds your notes, stores them in a vector database, retrieves the most relevant ones, and uses a local LLM to generate clear explanations.

This project mirrors the structure and workflow of a real AI engineering pipeline — including embeddings, FAISS search, prompt construction, and local inference.

---

## 🚀 Features

### ✅ Core Functionality (Fully Implemented)
- Embeddings using `sentence-transformers`
- Vector search using FAISS
- Local LLM inference using TinyLlama
- RAG pipeline (retrieve → augment → generate)
- Terminal-based interactive agent
- Automatic note loading from `data/notes/`

### 🧠 How It Works
1. User asks a question  
2. The agent embeds the query  
3. FAISS retrieves the most relevant notes  
4. Notes + question are combined into a prompt  
5. TinyLlama generates the final answer  
6. The answer is displayed in the terminal  

---

## 📂 Project Structure

study-agent-final/
│
├── agent/
│   ├── agent_loop.py
│   ├── answer_function.py
│   ├── embeddings_setup.py
│   ├── vector_db_setup.py
│   ├── local_llm_setup.py
│   └── tools.py
│
├── data/
│   └── notes/
│       ├── gradient_descent.txt
│       ├── cnn_layers.txt
│       └── transformers.txt
│
├── demo/
│   └── demo_script.md
│
├── docs/
│   ├── final_writeup.md
│   └── architecture_diagram.png
│
├── requirements.txt
└── README.md


---

## 🛠️ Installation & Setup

### 1️⃣ Download the Repo
Click:

Code → Download ZIP


Extract it fully (don’t run from inside the ZIP).

### 2️⃣ Open CMD inside the extracted folder
In File Explorer:

- Click the address bar  
- Type: `cmd`  
- Press Enter  

### 3️⃣ Install dependencies

pip install -r requirements.txt


### 4️⃣ Run the agent

python agent/agent_loop.py


You’ll see:

Study Agent is ready!
Ask something:


---

## 🎯 Example Interaction

**User:**  
`what is gradient descent`

**Agent:**  
Explains gradient descent using your notes + TinyLlama.

---

## 🔮 Planned Future Enhancements

This project is designed to grow. Below are features I may add in future versions:

### ⭐ Advanced Features
- Chat history (multi‑turn memory)
- Long‑term memory (store new knowledge)
- Add notes from the terminal (`add note "..."`)
- Search notes (`search notes "cnn"`)
- Explain Like I’m 5 mode (`eli5: backpropagation`)
- Summarize PDF mode (upload → extract → embed)
- Quiz Me mode (auto‑generate quizzes from notes)

### ⭐ App Packaging
- Streamlit web app
- Gradio interface
- Desktop app (PyInstaller)
- CLI tool (`study-agent --ask "..."`)
- pip‑installable package (`pip install study-agent`)

These upgrades will transform the Study Agent from a terminal tool into a full AI application.

---

## 🧩 Tech Stack
- Python 3.10+
- SentenceTransformers (embeddings)
- FAISS (vector search)
- Transformers (LLM inference)
- TinyLlama (local model)
- PyTorch (backend)

---

## 🏁 Status
The core RAG pipeline is complete and fully functional.  
Additional features and UI enhancements may be added in future updates.

---

## 👤 Author
**Aima Ayaz**  
W216981450@student.hccs.edu

AI Student • ML Engineer in Training  
Houston, TX

