from .state import DebateState
from .models import llm

# ==========================================================
# 3. THE NODES (The Debaters and the Judge)
# ==========================================================

def pro_agent_node(state: DebateState):
    """Agent 1: Argues IN FAVOR of the topic."""
    print(f"\n--- [PRO AGENT] Thinking... ---")
    
    topic = state["topic"]
    history_text = "\n".join(state["history"])
    
    prompt = (
        f"Topic: {topic}\n"
        f"You are the PRO debater. You strongly AGREE with the topic.\n"
        f"Here is the debate history so far:\n{history_text}\n"
        f"Write a short, fierce 2-sentence argument defending your side or attacking the CON side."
    )
    
    response = llm.invoke(prompt)
    return {"history":[f"PRO: {response.content}"]}

def con_agent_node(state: DebateState):
    """Agent 2: Argues AGAINST the topic."""
    print(f"---[CON AGENT] Thinking... ---")
    
    topic = state["topic"]
    history_text = "\n".join(state["history"])
    
    prompt = (
        f"Topic: {topic}\n"
        f"You are the CON debater. You strongly DISAGREE with the topic.\n"
        f"Here is the debate history so far:\n{history_text}\n"
        f"Write a short, fierce 2-sentence counter-argument attacking the PRO side."
    )
    
    response = llm.invoke(prompt)
    
    # We append the message AND increase the round counter by 1
    return {
        "history": [f"CON: {response.content}"], 
        "current_round": state["current_round"] + 1
    }

def judge_node(state: DebateState):
    """The Judge: Summarizes the debate and declares a winner."""
    print(f"\n--- [JUDGE] Summarizing the debate... ---")
    
    history_text = "\n".join(state["history"])
    
    prompt = (
        f"You are an impartial Judge. Read the following debate:\n{history_text}\n\n"
        f"Provide a brief 3-sentence summary of the arguments, and declare who won (PRO or CON) and why."
    )
    
    response = llm.invoke(prompt)
    return {"history":[f"\n=== FINAL VERDICT ===\n{response.content}"]}
