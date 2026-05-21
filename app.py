import streamlit as st
import os

from rag.loader import load_pdf
from rag.chunker import split_text
from rag.embeddings import get_embedding_model
from rag.vectorstore import create_vector_store
from rag.retriever import retrieve_docs
from rag.qa_chain import generate_answer

st.set_page_config(page_title="FinRAG")

st.title("📈 FinRAG")
st.subheader("AI-Powered Financial Report Analysis")

uploaded_file = st.file_uploader(
    "Upload Financial Report PDF",
    type="pdf"
)

company_name = st.text_input(
    "Enter Company Name"
)

if uploaded_file and company_name:

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Financial PDF Uploaded")

    # STEP 1 — Extract Text
    text = load_pdf(pdf_path)

    # STEP 2 — Chunking
    chunks = split_text(text)

    st.write(f"Total chunks created: {len(chunks)}")

    # STEP 3 — Embedding Model
    embedding_model = get_embedding_model()

    st.write("Embedding model loaded")

    # STEP 4 — Vector Store
    vector_store = create_vector_store(
        chunks,
        embedding_model,
        company_name
    )

    st.success("Financial vector database created")

    # User Question
    query = st.text_input(
        "Ask financial questions about the report"
    )

    if query:

        # STEP 5 — Retrieve Relevant Chunks
        docs = retrieve_docs(
            vector_store,
            query
        )

        st.subheader("Retrieved Financial Chunks")

        for i, doc in enumerate(docs):

            st.write(f"### Chunk {i+1}")

            st.write(doc.page_content)

            st.write("Metadata:")

            st.json(doc.metadata)

            st.write("-------------------")

        # STEP 6 — Final Answer
        answer = generate_answer(
            query,
            docs
        )

        st.subheader("Financial Analysis")

        st.write(answer)