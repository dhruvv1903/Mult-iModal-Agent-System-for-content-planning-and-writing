
import os
from dotenv import load_dotenv

load_dotenv()


def get_apiKey():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. "
            "Please add it to your .env file."
        )

    return api_key
