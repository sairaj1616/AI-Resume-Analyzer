# import sys
# import streamlit as st
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from utils.resume_parser import extract_text_from_pdf
# from utils.skill_extractor import extract_skills

# st.title("AI resume analyzer")

# uploaded_file = st.file_uploader("upload your resume(PDF):", type="pdf")
# if uploaded_file is not None:
#      temp_path = "temp_resume.pdf"

#      with open(temp_path, "wb") as f:
#           f.write(uploaded_file.read())

#      text = extract_text_from_pdf(temp_path)


#      skills = extract_skills(text)

#      st.subheader("extracted skills")
#      for skills in skills:
#           st.write("-", skills)

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.job_matcher import match_skills


st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

job_description = st.text_area("Paste Job Description")

if uploaded_file is not None:

    temp_path = "temp_resume.pdf"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    # Resume text
    resume_text = extract_text_from_pdf(temp_path)

    # Resume skills
    resume_skills = extract_skills(resume_text)

    st.subheader("Extracted Resume Skills")
#     st.write(resume_skills)
      
     #  improvising to show resume skills
    for skill in resume_skills:
        st.write("✅", skill)

    if job_description:

        job_skills = extract_skills(job_description)

        score, matched, missing = match_skills(resume_skills, job_skills)

     #    st.subheader("Job Match Score")
     #    st.write(f"{score:.2f}%")

     #  improvising score display
        st.subheader("Job Match Score")
        st.progress(int(score))
        st.write(f"### {score:.2f}% Match")

        st.subheader("Matched Skills")
     #    st.write(matched)    use this instead

          # improvising matched skills
        for skill in matched:
            st.write("🟢", skill)

        st.subheader("Missing Skills")
     #    st.write(missing)

     # improvising missing skkils section
        for skill in missing:
            st.write("🔴", skill)

     #  enhancing resume analyzer 

        st.subheader("resume Improvement Suggestions")

        if missing:
            for skill in missing:
                st.write(f"- consider learning **{skill}**")
        else:
            st.write("No missing skills. Your resume is a good match for the job description!")