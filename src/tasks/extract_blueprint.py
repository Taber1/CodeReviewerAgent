from crewai import Task

def extract_blueprint_task(agent, document_directory):
    return Task(
        description=f"Analyze and extract technical requirements from documents in {document_directory}",
        expected_output="Structured technical requirements document in markdown format with clear sections and specifications.",
        agent=agent,
        inputs={"document_directory": document_directory},
        output_file="blueprint_summary.md"
    )