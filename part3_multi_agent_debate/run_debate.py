import os
import sys

# Ensure the root of part3_multi_agent_debate is in path so we can import 'debate'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from debate import debate_app

# ==========================================================
# 6. RUN THE DEBATE
# ==========================================================
if __name__ == "__main__":
    
    initial_state = {
        "topic": "Artificial Intelligence should be allowed to grade university exams.",
        "history":[],
        "current_round": 0,
        "max_rounds": 2 
    }
    
    print("========================================")
    print(f"DEBATE TOPIC: {initial_state['topic']}")
    print("========================================")
    
    final_state = debate_app.invoke(initial_state)
    
    print("\n\n" + "="*40)
    print("FULL DEBATE TRANSCRIPT:")
    print("="*40)
    for message in final_state["history"]:
        print(message + "\n")
