from crewai import Task

def analyze_code_task(agent):
    return Task(
        description="""Analyze codebase against extracted technical guidelines from blueprint documents.
        Context: {blueprint_summary}""",
        expected_output="List of code violations with file paths and specific fixes.",
        agent=agent,
        output_file="code_analysis_report.md"
    )