## This is what the rest of the application will use.


class KnowledgeService:

    def __init__(self,retriever):
        self.retriever = retriever

    def search(self, query: str):
        return self.retriever.invoke(query)

    