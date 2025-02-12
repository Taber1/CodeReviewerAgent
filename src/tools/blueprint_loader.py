import os
import PyPDF2
from docx import Document

def load_blueprint(document_dir: str) -> str:
    """Validates and loads document content with error handling"""
    content = []
    
    if not os.path.isdir(document_dir):
        raise ValueError(f"Invalid document directory: {document_dir}")

    for filename in os.listdir(document_dir):
        file_path = os.path.join(document_dir, filename)
        
        try:
            if filename.endswith(".pdf"):
                with open(file_path, "rb") as f:
                    pdf = PyPDF2.PdfReader(f)
                    content.append(f"=== PDF: {filename} ===")
                    content += [f"Page {i+1}:\n{page.extract_text()}" 
                              for i, page in enumerate(pdf.pages)]
                    
            elif filename.endswith(".docx"):
                doc = Document(file_path)
                content.append(f"=== DOCX: {filename} ===")
                content += [para.text for para in doc.paragraphs if para.text.strip()]
                
            else:
                print(f"⚠️ Skipped unsupported file: {filename}")
                
        except Exception as e:
            print(f"🚨 Error processing {filename}: {str(e)}")
            continue
            
    return "\n\n".join(content) if content else ""