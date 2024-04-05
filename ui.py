"""
Ask the Agent using Streamlit UT
"""
import streamlit as st
import os
import pickle

from app.llm import llm
from app.agent import ask

MEMORY_FILE_PATH = 'chat.pk'

# Load conversation history from a file
def load_conversation_history():
    try:
        with open(MEMORY_FILE_PATH, 'rb') as file_handler:
            return pickle.load(file_handler)
    except FileNotFoundError:
        return []

def save_conversation_history(history):
    with open(MEMORY_FILE_PATH, 'wb') as file_handler:
        pickle.dump(history, file_handler)

def handle_new_message():
    new_message = st.session_state.user_input.strip()
    if new_message:
        st.session_state.conversation_history.append(f"You: {new_message}")
        with st.spinner("Agent is thinking..."):
            response = ask(new_message)
            st.session_state.conversation_history.append(f"Agent: {response}")
        save_conversation_history(st.session_state.conversation_history)
        st.session_state.user_input = ""

st.title("Your Legal Agent")

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = load_conversation_history()

for message in st.session_state.conversation_history:
    st.write(message)

st.text_input("Ask a question:", key="user_input", value="")
st.button("Submit", on_click=handle_new_message)
