import os
from langchain_groq import ChatGroq

# --- SETUP: Set your FREE Groq API Key ---
os.environ["GROQ_API_KEY"] = "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"

# ==========================================================
# 2. THE MODELS (The AI Personalities)
# ==========================================================
# We use Meta's Llama 3 model hosted on Groq for FREE!
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
