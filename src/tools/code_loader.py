import os

def load_codebase(codebase_path: str) -> list:
    """Validates and loads code files with error tracking"""
    code_files = []
    
    if not os.path.exists(codebase_path):
        raise FileNotFoundError(f"Codebase path not found: {codebase_path}")

    for root, _, files in os.walk(codebase_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        code_files.append({
                            "path": file_path,
                            "content": f.read()
                        })
                except Exception as e:
                    print(f"🚨 Error reading {file}: {str(e)}")
                    
    return code_files