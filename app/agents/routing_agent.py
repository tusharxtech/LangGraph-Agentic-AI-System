from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def route_query(query: str) -> Literal["math", "search"]:
    prompt = f"""
    Classify the query strictly as:
    - math
    - search

    Query: {query}
    """
    decision = llm.invoke(prompt).content.lower()

    return "math" if "math" in decision else "search"