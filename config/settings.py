import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Settings:
    def __init__(self):
        self.__api_key = os.getenv("GROQ_API_KEY")

    def load_api_key(self):

        if not self.__api_key:
            raise ValueError("API key not found.")
        else:
            return self.__api_key
