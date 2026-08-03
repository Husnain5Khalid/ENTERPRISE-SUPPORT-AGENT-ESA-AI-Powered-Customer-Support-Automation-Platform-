from app.rag.vectore_store import get_vector_store

def get_retriever():
    return get_vector_store().as_retriever(
        search_kwargs={
            "k":3    ##Now every query return top 3 relevant chunks.
        }
    )

