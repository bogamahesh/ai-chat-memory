import os

from dotenv import load_dotenv


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def validate_config() -> None:
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is missing from your environment.")
