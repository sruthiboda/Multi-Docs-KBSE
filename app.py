import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# Updated imports
from langchain.text_splitter import CharacterTextSplitter 
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# Optional UI templates (make sure file exists)
try:
    from htmlTemplates import css, bot_template, user_template
except:
    css, bot_template, user_template = "", None, None


# -------- PDF TEXT --------
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text


# -------- TEXT CHUNKS --------
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200
    )
    return text_splitter.split_text(text)


# -------- VECTOR STORE --------
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings)


# -------- CONVERSATION CHAIN --------
def get_conversation_chain(vectorstore):
    pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512,
    do_sample=True,
    temperature=0.7
)

    llm = HuggingFacePipeline(pipeline=pipe)

    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )


# -------- HANDLE USER INPUT --------
def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("⚠️ Please upload and process documents first.")
        return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if user_template and bot_template:
            # If templates exist
            if i % 2 == 0:
                st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            # Fallback simple UI
            if i % 2 == 0:
                st.markdown(f"👤 **You:** {message.content}")
            else:
                st.markdown(f"🤖 **Bot:** {message.content}")


# -------- MAIN --------
def main():
    load_dotenv()

    st.set_page_config(page_title="KnowledgeBase.com", page_icon="🤖")

    # Custom UI styling
    st.markdown("""
    <style>
    body { background-color: #0e1117; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>🤖 MultiDoc-KBSE</h1>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align:center;'>Ask anything from your PDFs instantly 🚀</p>", unsafe_allow_html=True)

    if css:
        st.write(css, unsafe_allow_html=True)

    # Session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input
    user_question = st.text_input("💬 Ask a question:")
    if user_question:
        handle_userinput(user_question)

    # Sidebar
    with st.sidebar:
        st.subheader("📁 Your Documents")

        pdf_docs = st.file_uploader(
            "Upload PDFs",
            accept_multiple_files=True
        )

        if pdf_docs:
            for file in pdf_docs:
                st.write(f"📄 {file.name}")

        if st.button("⚡ Process"):
            if not pdf_docs:
                st.warning("⚠️ Please upload at least one PDF.")
                return

            with st.spinner("Processing documents..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)

                st.session_state.conversation = get_conversation_chain(vectorstore)

            st.success("✅ Processing complete!")

        # Clear chat button
        if st.button("🗑 Clear Chat"):
            st.session_state.chat_history = []
            st.session_state.conversation = None


if __name__ == '__main__':
    main()