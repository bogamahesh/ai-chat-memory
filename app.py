import streamlit as st

from chat_engine import ChatEngine
from config import validate_config


st.set_page_config(
    page_title="AI Chat Assistant with Memory",
    page_icon="💬",
    layout="centered",
)


def initialize_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat_engine" not in st.session_state:
        st.session_state.chat_engine = ChatEngine()


def clear_chat() -> None:
    st.session_state.messages = []
    st.session_state.chat_engine.clear_memory()


initialize_session_state()

st.title("AI Chat Assistant with Memory")
st.caption("A context-aware chatbot powered by LangChain, Gemini, and Streamlit.")

with st.sidebar:
    st.header("Chat Controls")
    st.button("Clear chat", on_click=clear_chat, use_container_width=True)
    st.markdown("Memory window: last 10 conversation turns")

try:
    validate_config()
except ValueError as error:
    st.error(str(error))
    st.info("Create a .env file from .env.example and add your Gemini API key.")
    st.stop()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_engine.ask(prompt)
                st.markdown(response)
            except Exception as error:
                response = (
                    "I ran into an issue while generating a response. "
                    f"Details: {error}"
                )
                st.error(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
