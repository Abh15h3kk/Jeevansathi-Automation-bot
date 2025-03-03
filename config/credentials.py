from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
MESSAGE = os.getenv("MESSAGE")

if not EMAIL or not PASSWORD or not MESSAGE:
    raise ValueError("Missing EMAIL or PASSWORD or MESSAGE in .env file")