def match_skills(resume_skills, job_skills):
    
    resume_set = set([skill.lower() for skill in resume_skills])
    job_set = set([skill.lower() for skill in job_skills])

    matched_skills = resume_set.intersection(job_set)
    missing_skills = job_set - resume_set

    if len(job_set) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(job_set)) * 100
    return score, list(matched_skills), list(missing_skills)
