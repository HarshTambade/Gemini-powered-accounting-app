import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", "USD")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
