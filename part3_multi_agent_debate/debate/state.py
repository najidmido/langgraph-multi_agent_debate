import operator
from typing import TypedDict, Annotated

# ==========================================================
# 1. THE STATE (The Notepad passed between agents)
# ==========================================================
class DebateState(TypedDict):
    topic: str
    # 'Annotated[list, operator.add]' means every time an agent speaks, 
    # it APPENDS their message to the history, rather than erasing it!
    history: Annotated[list, operator.add] 
    current_round: int
    max_rounds: int
