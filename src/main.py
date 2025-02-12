from dotenv import load_dotenv
from crewai import Crew
import os
from llm_config import llm

# Load env first
load_dotenv()

# Configure LiteLLM for Gemini
os.environ["LITELLM_MODEL"] = "gemini/gemini-1.5-flash-latest"
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

def main():
    # Configuration
    document_directory = "../blueprints"
    codebase_path = r"E:\Projects\Final Project\VPI_IMC_Front"
    
    # Load data first
    from tools.blueprint_loader import load_blueprint
    from tools.code_loader import load_codebase
    
    blueprint_data = load_blueprint(document_directory)
    codebase_data = load_codebase(codebase_path)

    # Initialize agents
    from agents.blueprint_extractor_agent import blueprint_extractor_agent
    from agents.code_analyzer_agent import code_analyzer_agent
    blueprint_agent = blueprint_extractor_agent()
    code_agent = code_analyzer_agent()

    # Create tasks with explicit data
    from tasks.extract_blueprint import extract_blueprint_task
    from tasks.analyze_code import analyze_code_task
    extraction_task = extract_blueprint_task(
        agent=blueprint_agent,
        document_directory=document_directory
    )
    
    analysis_task = analyze_code_task(agent=code_agent)
    analysis_task.context = [extraction_task]

    # Configure crew with direct inputs
    crew = Crew(
        agents=[blueprint_agent, code_agent],
        tasks=[extraction_task, analysis_task],
        verbose=True,
        manager_llm=llm
    )

    # Execute workflow with both inputs
    result = crew.kickoff(inputs={
        "codebase": codebase_data,
        "blueprint_summary": blueprint_data
    })
    
    print("\nFinal Analysis Report:")
    print(result)

if __name__ == "__main__":
    main()