from crewai import Agent
from llm_config import llm

def code_analyzer_agent():
    return Agent(
        role="Senior Code Quality Engineer",
        goal="Ensure code compliance with technical specifications",
        backstory="Expert in static code analysis and architectural compliance checking.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
        memory=True
    )