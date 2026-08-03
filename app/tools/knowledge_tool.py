"""
Tool 1 — Knowledge Tool
Responsibility

Search the company knowledge base.
"""

from langchain_core.tools import tool

from app.rag.retriever import get_retriever
from app.services.knowledge_service import KnowledgeService

knowledge_service = KnowledgeService(
    retriever=get_retriever()
)


@tool
def search_knowledge(query: str) -> str:
    """
    Search internal company documents.
    """

    print("=" * 60)
    print("Knowledge Tool Called")
    print("Query:", query)
    print("=" * 60)

    documents = knowledge_service.search(query)

    return "\n\n".join(
        doc.page_content
        for doc in documents
    )