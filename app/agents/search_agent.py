from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from app.tools.search_tool import search_web

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

# Prompt (IMPORTANT for tool usage)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant that can use tools when needed."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# Create agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=[search_web],
    prompt=prompt
)

# Executor (runs the agent)
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_web],
    verbose=True
)

def run_search_agent(query: str):
    result = agent_executor.invoke({"input": query})
    return result["output"]