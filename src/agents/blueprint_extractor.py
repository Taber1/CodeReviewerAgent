from crewai import Agent

def blueprint_extractor_agent(llm):
    return Agent(
        role="Blueprint Extractor",
        goal="Extract and summarize blueprints from provided PDFs.",
        backstory="You are an AI agent trained to extract and summarize important information from documents.",
        verbose=True,
        llm=llm
    )