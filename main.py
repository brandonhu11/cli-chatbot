import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    raise ValueError("No API key found. Check .env file for GEMINI_API_KEY.")
else:
    print("API key loaded:", api_key[:6] + "...")