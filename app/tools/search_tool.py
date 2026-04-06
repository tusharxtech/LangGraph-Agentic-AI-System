import requests
import os
from langchain.tools import tool

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

@tool
def search_web(query: str) -> str:
    """
    Perform real-time web search using Serper API.
    """
    url = "https://google.serper.dev/search"

    payload = {"q": query}
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    results = []
    for item in data.get("organic", [])[:3]:
        results.append(item.get("snippet", ""))

    return "\n".join(results)