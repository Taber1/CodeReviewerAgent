import os

def load_codebase(codebase_path):
    code_files = []
    for root, _, files in os.walk(codebase_path):
        for file in files:
            if file.endswith(".py"):  # Adjust for your language
                with open(os.path.join(root, file), "r") as f:
                    code_files.append({"filename": file, "content": f.read()})
    return code_files
