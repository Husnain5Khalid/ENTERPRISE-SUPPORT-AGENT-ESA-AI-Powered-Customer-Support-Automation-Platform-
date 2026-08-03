from langchain_google_genai import ChatGoogleGenerativeAI

from app.config.settings import settings
from app.tools.registry import TOOLS

llm = ChatGoogleGenerativeAI(
    model=settings.model_name,
    google_api_key=settings.google_api_key,
    temperature=0,
)

llm_with_tools = llm.bind_tools(TOOLS)
