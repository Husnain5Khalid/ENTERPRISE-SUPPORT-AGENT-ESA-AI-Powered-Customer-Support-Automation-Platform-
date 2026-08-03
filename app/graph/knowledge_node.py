from app.services.knowledge_service import KnowledgeService
from app.rag.retriever import get_retriever

knowledge_service = KnowledgeService(
    retriever=get_retriever()
)


def knowledge_node(state):

    query = state["messages"][-1].content

    documents = knowledge_service.search(query)

    knowledge = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    print("=" * 70)
    print("Knowledge Retrieved")
    print(knowledge)
    print("=" * 70)

    return {
        "knowledge": knowledge
    }