from langchain.text_splitter import RecursiveCharacterTextSplitter

class knowledgeSplitter:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
        )

    def split(self, documents):
        return self.splitter.split_documents(documents)

    