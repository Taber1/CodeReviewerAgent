from crewai import Task

def analyze_code_task(agent, guidelines):
    return Task(
        description=f"Analyze the following codebase and compare it against these guidelines: {guidelines}. Identify any violations or areas for improvement.",
        expected_output="A list of code violations, including the filename, description of the issue, and suggested fixes.",
        agent=agent
    )