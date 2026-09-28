from dotenv import load_dotenv
from .filereader import extract_paragraphs
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import TextSplitter

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large")
vectore_store = InMemoryVectorStore(embedding)

chunks = extract_paragraphs("RAG/pdfs/Penguins_ACL.pdf")

vectore_store.add_texts(texts=chunks)
print(f"indexed {len(chunks)} chunks")
