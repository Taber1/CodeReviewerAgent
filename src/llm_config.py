from crewai import LLM
import os

llm = LLM(
    model="gemini/gemini-1.5-flash-latest",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)