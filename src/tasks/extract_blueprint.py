from crewai import Task

def extract_blueprint_task(agent, pdf_directory):
    return Task(
        description=f"Extract and summarize guidelines from the PDFs in the directory: {pdf_directory}.",
        expected_output="A clear and concise summary of the guidelines.",
        agent=agent
    )