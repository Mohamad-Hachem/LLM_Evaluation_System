from dotenv import load_dotenv
from .file_reader import extract_paragraphs
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings


load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large")
vectore_store = InMemoryVectorStore(embedding)

chunks = extract_paragraphs("pdfs/Penguins_ACL.pdf")
vectore_store.add_texts(texts=chunks)
print(f"indexed {len(chunks)} chunks")
