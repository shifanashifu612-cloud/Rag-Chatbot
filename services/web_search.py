from dotenv import load_dotenv
import os

load_dotenv()

print("Tavily Key:", os.getenv("TAVILY_API_KEY"))