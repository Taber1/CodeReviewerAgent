from crewai import Agent
from llm_config import llm

def blueprint_extractor_agent():
    return Agent(
        role="Technical Documentation Analyst",
        goal="Extract technical requirements from blueprint documents",
        backstory="Expert in analyzing technical documentation and architecture specifications.",
        llm=llm,
        verbose=True
    )