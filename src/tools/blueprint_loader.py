import os
import PyPDF2

def load_blueprint(pdf_directory):
    blueprint = ""
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    blueprint += page.extract_text()
    return blueprint