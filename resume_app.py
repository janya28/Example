import os
import docx2txt
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

# Function to extract main information from resume
def extract_information(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    else:
        return "Unsupported file format"

    # Use BeautifulSoup to parse HTML and extract headings and contents
    soup = BeautifulSoup(text, 'html.parser')
    candidate_name = ""
    experience = ""
    skills = []

    # Find candidate name
    name_heading = soup.find(lambda tag: tag.name.startswith('h') and 'name' in tag.text.lower())
    if name_heading:
        candidate_name = name_heading.text.strip()
    print("Candidate Name:", candidate_name)

    # Find experience
    exp_heading = soup.find(lambda tag: tag.name.startswith('h') and 'experience' in tag.text.lower())
    if exp_heading:
        experience = exp_heading.find_next('p').text.strip()
    print("Experience:", experience)

    # Find skills
    skills_heading = soup.find(lambda tag: tag.name.startswith('h') and 'skills' in tag.text.lower())
    if skills_heading:
        skills_list = skills_heading.find_next('ul')
        if skills_list:
            skills = [li.text.strip() for li in skills_list.find_all('li')]
    print("Skills:", skills)

    return candidate_name, experience, skills

# Main function to traverse resumes and generate HTML
def main(folder_path):
    # Create HTML content
    html_content = '<html><head><title>Resume Summary</title></head><body>'

    # Traverse resumes in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            file_path = os.path.join(folder_path, filename)
            candidate_name, experience, skills = extract_information(file_path)
            html_content += f'<h1>{filename}</h1>'
            html_content += f'<p><strong>Candidate Name:</strong> {candidate_name}</p>'
            html_content += f'<p><strong>Experience:</strong> {experience}</p>'
            html_content += '<p><strong>Skills:</strong></p>'
            html_content += '<ul>'
            for skill in skills:
                html_content += f'<li>{skill}</li>'
            html_content += '</ul>'

    html_content += '</body></html>'

    # Write HTML content to a file
    with open('resume_summary.html', 'w') as html_file:
        html_file.write(html_content)

# Run main function with the specified folder path
main('C:/Users/Janya/Desktop/resume_search_app/Resume_search/uploads')
