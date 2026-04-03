🚀 AI – Multi-Document Knowledge Base Search Engine

AI-powered document assistant that lets you chat with multiple PDFs using Retrieval-Augmented Generation (RAG)

📌 Overview

KnowledgeBase AI is an intelligent document search system that allows users to upload multiple PDF files and ask questions in natural language.
The system retrieves relevant information from documents and generates accurate, context-aware answers using AI.

This project is built based on the concept of RAG (Retrieval-Augmented Generation) as described in the assignment .


#How it Works

(![Image of Assignment](./docs/Knowledgebase_img.png>))

#<video controls src="20260402-1754-32.4092328.mp4" title="Live Demo"></video>

The application follows these steps to provide responses to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.


🎯 Features

✅ Chat with multiple PDFs
✅ AI-powered question answering
✅ Semantic search using embeddings
✅ No OpenAI billing (uses HuggingFace models)
✅ Fast retrieval with FAISS
✅ Clean Streamlit UI
✅ Context-aware conversation memory

🧠 How It Works (RAG Pipeline)
PDF Loading
Extracts text from uploaded PDF documents
Text Chunking
Splits text into smaller chunks for efficient processing
Embeddings Generation
Converts text into vector representations using HuggingFace models
Vector Storage (FAISS)
Stores embeddings for fast similarity search
User Query Processing
Finds most relevant chunks using semantic similarity
Response Generation
Uses LLM (Flan-T5) to generate contextual answers

🏗️ Tech Stack
Frontend: Streamlit
Backend: Python
LLM: HuggingFace (Flan-T5)
Embeddings: Sentence Transformers (all-MiniLM-L6-v2)
Vector DB: FAISS
Framework: LangChain
📂 Project Structure
📦 SmartDoc-AI
 ┣ 📜 app.py
 ┣ 📜 htmlTemplates.py
 ┣ 📜 requirements.txt
 ┣ 📁 docs
 ┣ 📁 data
 ┣ 📁 vectorstore
 ┗ 📜 README.md
⚙️ Installation
1️⃣ Clone Repository

cd smartdoc-ai
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
🖥️ Usage
Upload one or more PDF documents
Click Process
Ask questions like:
"Summarize the document"
"What are key findings?"
"Explain in simple terms"
Get AI-generated answers instantly
🎨 UI Preview

