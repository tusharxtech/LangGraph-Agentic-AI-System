from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def run_math_agent(query: str):
    prompt = f"Solve this math problem and return only answer: {query}"
    return llm.invoke(prompt).content.strip()