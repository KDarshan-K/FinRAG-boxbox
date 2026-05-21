from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):

    """
    Better chunking for finance documents.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " "
        ]
    )

    chunks = text_splitter.split_text(text)

    return chunks