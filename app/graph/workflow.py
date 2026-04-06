from langgraph.graph import StateGraph, START, END
from typing import TypedDict

from app.agents.search_agent import run_search_agent
from app.agents.math_agent import run_math_agent
from app.agents.routing_agent import route_query


class AgentState(TypedDict):
    user_query: str
    answer: str
    route: str


def router_node(state: AgentState):
    return {"route": route_query(state["user_query"])}


def search_node(state: AgentState):
    return {"answer": run_search_agent(state["user_query"])}


def math_node(state: AgentState):
    return {"answer": run_math_agent(state["user_query"])}


def route_decision(state: AgentState):
    return state["route"]


def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("router", router_node)
    workflow.add_node("search", search_node)
    workflow.add_node("math", math_node)

    workflow.add_edge(START, "router")
    workflow.add_conditional_edges("router", route_decision)
    workflow.add_edge("search", END)
    workflow.add_edge("math", END)

    return workflow.compile()