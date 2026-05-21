def retrieve_docs(vector_store, query):

    """
    Retrieve most relevant chunks
    from FAISS vector store.
    """

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(query)

    return docs