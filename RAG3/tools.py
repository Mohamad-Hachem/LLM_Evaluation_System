from .indexing import vectore_store
from langchain.tools import tool


last_retrieved_context = []


@tool
def collecting_info2(query: str) -> str:
    """
    Search the PDF knowledge base and return relevant information
    for the user's question.
    """

    global last_retrieved_context

    docs = vectore_store.similarity_search(query, k=1)

    # Save the REAL retrieved chunks
    last_retrieved_context = [
        doc.page_content
        for doc in docs
    ]

    return "\n\n".join(last_retrieved_context)