import pandas as pd
import os

def extract_skills(text):

    # Get project root directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Path to skills.csv
    skills_path = os.path.join(BASE_DIR, "data", "skills.csv")

    skills_df = pd.read_csv(skills_path)

    skills_list = skills_df["skills"].tolist()

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))