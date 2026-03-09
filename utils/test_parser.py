import os
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills

# Find project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build resume path
resume_path = os.path.join(BASE_DIR, "resume.pdf")

# Extract text
text = extract_text_from_pdf(resume_path)

# Extract skills
skills = extract_skills(text)

print("Extracted Skills:", skills)