"""
Agent LLM
"""

import os

from langchain_openai import ChatOpenAI

if not os.environ.get("OPENAI_API_KEY"):
    raise RuntimeError("Missing OPENAI_API_KEY")

print("Initializing LLM")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
print(llm)
