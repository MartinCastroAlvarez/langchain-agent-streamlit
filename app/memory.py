"""
Agent Memory
"""

import os
import pickle

from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories.in_memory import \
    ChatMessageHistory

from .llm import llm

MEMORY_FILE_PATH = "memory.pk"


def initialize_memory(memory_file_path=MEMORY_FILE_PATH) -> ConversationBufferMemory:
    messages = []
    if os.path.isfile(MEMORY_FILE_PATH):
        with open(MEMORY_FILE_PATH, "rb") as file_handler:
            messages = pickle.load(file_handler)
    chat_history = ChatMessageHistory(messages=messages)
    return ConversationBufferMemory(llm=llm, chat_memory=chat_history)


def persist_memory(agent_executor: AgentExecutor, memory_file_path=MEMORY_FILE_PATH):
    with open(MEMORY_FILE_PATH, "wb") as file_handler:
        pickle.dump(agent_executor.memory.chat_memory.messages, file_handler)
