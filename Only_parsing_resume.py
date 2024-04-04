import os
import docx
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with fitz.open(file_path) as pdf_file:
            for page in pdf_file:
                text += page.get_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text

def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
    except Exception as e:
        print(f"Error extracting text from DOCX: {e}")
    return text

def main(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            print("Resume:", filename)
            text = extract_text_from_pdf(file_path)
            print("Text:")
            print(text)
            print("-" * 50)
        elif filename.endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            print("Resume:", filename)
            text = extract_text_from_docx(file_path)
            print("Text:")
            print(text)
            print("-" * 50)

if __name__ == "__main__":
    main('C:/Users/Janya/Desktop/resume_search_app/Resume_search/uploads')
