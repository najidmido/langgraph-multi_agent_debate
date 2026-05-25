from langgraph.graph import StateGraph, END
from .state import DebateState
from .nodes import pro_agent_node, con_agent_node, judge_node
from .router import debate_router

# ==========================================================
# 5. BUILD THE LANGGRAPH
# ==========================================================
workflow = StateGraph(DebateState)

workflow.add_node("Pro_Agent", pro_agent_node)
workflow.add_node("Con_Agent", con_agent_node)
workflow.add_node("Judge", judge_node)

workflow.set_entry_point("Pro_Agent")
workflow.add_edge("Pro_Agent", "Con_Agent")

workflow.add_conditional_edges(
    "Con_Agent",
    debate_router,
    {
        "next_round": "Pro_Agent",   
        "go_to_judge": "Judge"       
    }
)

workflow.add_edge("Judge", END)
debate_app = workflow.compile()
