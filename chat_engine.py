from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_API_KEY


class ChatEngine:
    def __init__(self) -> None:
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GEMINI_API_KEY,
            temperature=0.7,
        )
        self.memory = ConversationBufferWindowMemory(k=10)
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=False,
        )

    def ask(self, user_input: str) -> str:
        return self.conversation.predict(input=user_input)

    def clear_memory(self) -> None:
        self.memory.clear()
