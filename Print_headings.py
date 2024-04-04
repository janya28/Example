import os
import textract

def extract_headings(file_path):
    headings = []
    _, file_extension = os.path.splitext(file_path)

    if file_extension == '.pdf':
        try:
            text = textract.process(file_path).decode('utf-8')
            headings = [line.strip() for line in text.split('\n') if line.strip().isupper()]
        except Exception as e:
            print(f"Error extracting headings from PDF: {e}")
    elif file_extension == '.docx':
        try:
            text = textract.process(file_path).decode('utf-8')
            headings = [line.strip() for line in text.split('\n') if line.strip().isupper()]
        except Exception as e:
            print(f"Error extracting headings from DOCX: {e}")

    return headings

def main(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for file in files:
        file_path = os.path.join(directory, file)
        print(f"File: {file}")
        headings = extract_headings(file_path)
        print("Headings:")
        for heading in headings:
            print(heading)
        print("-" * 50)

if __name__ == "__main__":
    main('C:/Users/Janya/Desktop/resume_search_app/Resume_search/uploads')
