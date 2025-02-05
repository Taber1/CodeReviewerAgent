from crewai import Agent

def code_analyzer_agent(llm):
    return Agent(
        role="Code Quality Analyzer",
        goal="Analyze the codebase and ensure it follows company guidelines.",
        backstory="You are an AI agent trained to review code and ensure it adheres to best practices.",
        verbose=True,
        llm=llm
    )