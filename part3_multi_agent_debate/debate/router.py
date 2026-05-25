from .state import DebateState

# ==========================================================
# 4. THE ROUTER (The Moderator)
# ==========================================================

def debate_router(state: DebateState):
    """Decides whether to keep debating or go to the judge."""
    if state["current_round"] >= state["max_rounds"]:
        print(f"    [Moderator] Max rounds reached! Sending to Judge.")
        return "go_to_judge"
    else:
        print(f"    [Moderator] Round {state['current_round']} finished. Back to PRO.")
        return "next_round"
