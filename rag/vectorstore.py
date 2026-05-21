from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def create_vector_store(
        chunks,
        embedding_model,
        company_name="Unknown Company"
):

    """
    Create FAISS vector store
    with finance metadata.
    """

    documents = []

    for i, chunk in enumerate(chunks):

        doc = Document(
            page_content=chunk,

            metadata={
                "company": company_name,
                "chunk_id": i
            }
        )

        documents.append(doc)

    vector_store = FAISS.from_documents(
        documents,
        embedding_model
    )

    return vector_store