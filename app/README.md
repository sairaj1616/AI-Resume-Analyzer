 # AI Resume Analyzer

## Overview

AI Resume Analyzer is a web-based application that analyzes resumes and compares them with job descriptions to determine how well a candidate's profile matches the job requirements.

The system extracts skills from a resume, identifies skills required for a job, and calculates a match score while suggesting improvements for the resume.

---

## Features

* Upload resume in **PDF format**
* Extract skills from resume automatically
* Analyze **job description**
* Calculate **resume-job match score**
* Show **matched skills**
* Identify **missing skills**
* Provide **resume improvement suggestions**
* Interactive **Streamlit web interface**

---

## System Architecture

User Uploads Resume
│
▼
Resume Parser (PDF Text Extraction)
│
▼
Skill Extraction (NLP-based keyword detection)
│
▼
Job Description Skill Extraction
│
▼
Skill Matching Algorithm
│
▼
Match Score + Suggestions

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NLP (keyword-based extraction)
* pdfplumber
* Scikit-learn (for potential ML extensions)

---

## Project Structure

```
resume_analyzer
│
├── app
│   └── app.py
│
├── data
│   └── skills.csv
│
├── utils
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── job_matcher.py
│
├── models
├── notebooks
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com//AI-Resume-Analyzer.git
```

Navigate to the project directory:

```
cd AI-Resume-Analyzer
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```
streamlit run app/app.py
```

The web interface will open in your browser.

---

## Example Output

Resume Skills:

* Python
* Machine Learning
* SQL

Job Skills:

* Python
* TensorFlow
* Deep Learning

Match Score:

```
71.43%
```

Missing Skills:

* TensorFlow
* Deep Learning

Suggestions:

* Learn TensorFlow
* Add Deep Learning projects

---

## Future Improvements

* Machine learning based skill extraction
* Resume scoring using ATS metrics
* Job role prediction
* Resume formatting analysis
* Integration with job portals

---

## Author

Developed as part of a machine learning project demonstrating resume analysis and job matching using NLP techniques.
