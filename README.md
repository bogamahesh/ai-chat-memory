# AI Chat Assistant with Memory

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-app-ff4b4b)

A context-aware GenAI chat assistant with short-term conversational memory.

## Features

- Multi-turn memory with LangChain `ConversationBufferWindowMemory`
- Context-aware replies powered by Google Gemini
- Chat history UI with Streamlit chat components
- Clear chat button that resets the visible history and model memory

## Architecture

```text
User → Streamlit → LangChain → ConversationBufferWindowMemory → Gemini API
```

## Tech Stack

- Python 3.9+
- Streamlit
- LangChain
- Google Gemini API
- python-dotenv

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/ai-chat-memory.git
   cd ai-chat-memory
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:

   ```bash
   copy .env.example .env
   ```

5. Add your Gemini API key to `.env`:

   ```env
   GEMINI_API_KEY=your_key_here
   ```

6. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Screenshot

![Screenshot placeholder](https://via.placeholder.com/1200x700?text=AI+Chat+Assistant+with+Memory)

## License

This project is licensed under the MIT License.
