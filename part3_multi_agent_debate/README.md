# Part 3: Multi-Agent Debate Simulation

This module demonstrates a multi-agent debate simulation using LangGraph. Two agents (PRO and CON) debate a given topic for a configurable number of rounds. At the end, an impartial JUDGE agent reviews the transcript, summarizes the arguments, and declares a winner.

## Directory Structure

```text
part3_multi_agent_debate/
├── README.md                     # This documentation file
├── requirements.txt              # Script dependencies
└── debate.py                     # Multi-agent debate workflow and entrypoint
```

---

## 1. How It Works (Agent Workflow)

```text
       [ Start ]
           ↓
     ( Pro_Agent )
           ↓
     ( Con_Agent )
           ↓
     [ Debate Router ] --(current_round < max_rounds)--> [ Back to Pro_Agent ]
           │
     (current_round >= max_rounds)
           │
           ↓
       ( Judge )
           ↓
        [ END ]
```

1. **State Management**: Every speaker's argument is appended to the debate history.
2. **Pro Agent**: Argues strongly in favor of the topic.
3. **Con Agent**: Counter-argues and attacks the Pro Agent's points.
4. **Moderator (Router)**: Tracks rounds. Once the maximum number of rounds is reached, routes the debate to the Judge.
5. **Judge**: Evaluates the history, outputs a summary, and declares the winner with reasoning.

---

## 2. Setup and Installation

1. Navigate to this directory and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your Groq API Key as an environment variable (or let the script use the pre-configured fallback key):
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   # On Windows PowerShell:
   $env:GROQ_API_KEY="your_groq_api_key_here"
   ```

---

## 3. Running the Debate

To kick off the debate simulation:
```bash
python debate.py
```

### Customizing the Debate Topic or Rounds
Open `debate.py` and modify the inputs in the main block:
```python
initial_state = {
    "topic": "Artificial Intelligence should be allowed to grade university exams.",
    "history": [],
    "current_round": 0,
    "max_rounds": 2  # Adjust this to change the debate length
}
```
You can change the `"topic"` string to any topic of your choice.
