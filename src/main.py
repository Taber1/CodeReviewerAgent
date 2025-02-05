from dotenv import load_dotenv
import os
from agents.blueprint_extractor_agent import blueprint_extractor_agent
from agents.code_analyzer_agent import code_analyzer_agent
from tasks.extract_blueprint import extract_blueprint_task
from tasks.analyze_code import analyze_code_task
from crewai import Crew
from tools.code_loader import load_codebase

# Load environment variables
load_dotenv()

# Gemini Flash 1.5 setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def main():
    # Step 1: Load PDFs and codebase
    pdf_directory = "../blueprints"  # Folder containing your PDFs
    codebase_path = "C:\Users\Taber\Desktop\IMC"  # Folder containing your codebase

    # Step 2: Create agents
    blueprint_extractor_agent = blueprint_extractor_agent(llm=GEMINI_API_KEY)
    code_analyzer_agent = code_analyzer_agent(llm=GEMINI_API_KEY)

    # Step 3: Create tasks
    extract_blueprint_task = extract_blueprint_task(guideline_extractor_agent, pdf_directory)
    analyze_codebase_task = analyze_code_task(code_analyzer_agent, "")

    # Step 4: Set up crew
    crew = Crew(
        agents=[blueprint_extractor_agent, code_analyzer_agent],
        tasks=[extract_blueprint_task, analyze_codebase_task]
    )

    # Step 5: Run the crew
    analysis_result = crew.kickoff(inputs={"codebase": load_codebase(codebase_path)})

    # Step 6: Output the issues
    print("Codebase Analysis Results:")
    print(analysis_result)

if __name__ == "__main__":
    main()