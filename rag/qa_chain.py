from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


def generate_answer(query, docs):

    """
    Generate finance-focused answer.
    """

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    You are FinRAG,
    an AI financial analysis assistant.

    Your responsibilities:
    - analyze annual reports
    - summarize financial statements
    - explain business risks
    - analyze revenue trends
    - explain financial metrics
    - summarize company performance

    IMPORTANT RULES:
    - Answer ONLY using the provided context
    - Do NOT hallucinate
    - If information is unavailable,
      say:
      "Information not found in financial documents."

    Context:
    {context}

    Financial Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content