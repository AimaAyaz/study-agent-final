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

## 🧩 Architecture Diagram

Below is the architecture diagram for the Study Agent, adapted from my Midterm Blueprint and updated to reflect the final implementation.

<img width="340" height="508" alt="image" src="https://github.com/user-attachments/assets/9849694d-58eb-445a-be19-9939560e49ef" />

---
```markdown
## 📂 Project Structure

study-agent-final/
│
├── agent/
├── data/
│   └── notes/
│       ├── activation_functions.txt
│       ├── backpropagation.txt
│       ├── batch_normalization.txt
│       ├── cnn_layers.txt
│       ├── gradient_descent.txt
│       ├── learning_rate.txt
│       ├── overfitting.txt
│       ├── regularization.txt
│       ├── rnn_vs_lstm.txt
│       ├── transformers.txt
│       ├── optimizers.txt
│       ├── loss_functions.txt
│       ├── attention_mechanism.txt
│       ├── pooling_layers.txt
│       ├── dropout.txt
│       ├── gradient_clipping.txt
│       ├── epochs_batches_iterations.txt
│       ├── convolution_operation.txt
│       ├── normalization_layers.txt
│       ├── vanishing_gradients.txt
│       ├── gru.txt
│       ├── residual_connections.txt
│       ├── softmax.txt
│       ├── cross_entropy.txt
│       ├── multihead_attention.txt
│       ├── positional_encoding.txt
│       ├── autoencoders.txt
│       ├── gans.txt
│       ├── reinforcement_learning_basics.txt
│       ├── dropout_vs_batchnorm.txt
│
├── demo/
│   └── youtube link
├── docs/
│   └── architecture.png
│
├── README.md
└── REFLECTION.md
```



---

## 🛠️ Installation & Setup

### 1️⃣ Download the Repo
Click:

Code → Download ZIP


Extract it fully (don’t run from inside the ZIP).

### 2️⃣ Open CMD inside the extracted folder
In File Explorer:

- Double click the extracted folder (all files will be listed) 
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

## 📚 Knowledge Base Files

The Study Agent uses Retrieval-Augmented Generation (RAG) to answer questions based on my own course notes.  
All source documents are included in the `data/notes/` folder. Each `.txt` file contains short, student-friendly explanations of deep learning topics such as CNNs, RNNs, Transformers, and optimization algorithms.

If the dataset grows too large in future versions, it will be hosted externally (e.g., Google Drive or Hugging Face Datasets).  
For this submission, all sample notes are included locally for transparency.

---

| File Name | Topic |
|------------|--------|
| gradient_descent.txt | Optimization algorithm |
| cnn_layers.txt | Convolutional neural networks |
| transformers.txt | Self-attention and sequence modeling |
| regularization.txt | Overfitting prevention |
| gans.txt | Generative Adversarial Networks |
| reinforcement_learning_basics.txt | Agent-environment interaction |

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
- add a “short answer mode” toggle
- add a “bullet‑point mode”
- add a “one‑sentence mode”


### ⭐ App Packaging
- Streamlit web app
- Gradio interface
- Desktop app (PyInstaller)
- CLI tool (`study-agent --ask "..."`)
- pip‑installable package (`pip install study-agent`)

These upgrades will transform the Study Agent from a terminal tool into a full AI application.

---

## 🎥 Demo Video

The demo below shows the Study Agent handling three real-world scenarios.

▶️ https://youtu.be/V3oWfrqrHqs 

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

