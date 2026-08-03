from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader


class KnowledgeLoader:

    def __init__(self, knowledge_path: str):
        self.knowledge_path = knowledge_path

    def load(self):
        loader = DirectoryLoader(
            self.knowledge_path,
            glob="**/*.md",
            loader_cls=TextLoader,
        )

        return loader.load() 