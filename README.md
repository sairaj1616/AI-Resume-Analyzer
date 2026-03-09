# AI Resume Analyzer

## Overview

AI Resume Analyzer is a web-based application that analyzes resumes and compares them with job descriptions to determine how well a candidate's profile matches job requirements.

The system extracts skills from resumes, identifies skills required for a job, calculates a match score, and provides suggestions to improve the resume.

---

## Features

* Upload resume in **PDF format**
* Automatic **skill extraction**
* Analyze **job descriptions**
* Calculate **resume-job match score**
* Show **matched skills**
* Identify **missing skills**
* Provide **resume improvement suggestions**
* Interactive **Streamlit web interface**

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NLP (keyword extraction)
* pdfplumber

---

## Project Structure

```
AI-Resume-Analyzer
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
│   └── job_matcher.py
│
├── screenshots
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/sairaj1616/AI-Resume-Analyzer.git
```

Navigate to the project directory:

```
cd AI-Resume-Analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the Application

```
streamlit run app/app.py
```

---

## Example Output

Match Score Example:

```
71.43%
```

Missing Skills Example:

* TensorFlow
* Deep Learning

Suggestions:

* Learn TensorFlow
* Add Deep Learning projects

---

## Author

Developed by **Sai Rajesh** as part of a machine learning project.
