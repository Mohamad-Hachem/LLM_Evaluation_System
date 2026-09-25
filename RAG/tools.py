
from .indexing import vectore_store
from langchain.tools import tool

@tool
def collecting_info(query: str) -> str:
    """
    Search the PDF knowledge base and return relevant information
    for the user's question.
    """

    docs = vectore_store.similarity_search(query, k=3)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

#print(collecting_info("what is the food of penguins")) 

