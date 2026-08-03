from langchain_chroma import Chroma

from app.config.settings import settings
from app.rag.embeddings import get_embeddings

def get_vector_store():
    return Chroma(
        persist_directory=settings.chroma_db_path,
        embedding_function=get_embeddings(),
    )

