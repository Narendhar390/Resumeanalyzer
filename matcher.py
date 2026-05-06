def match_skills(resume_skills, jd_skills):
    matched = list(
        set(resume_skills).intersection(set(jd_skills))
    )

    missing = list(
        set(jd_skills).difference(set(resume_skills))
    )

    score = 0

    if len(jd_skills) > 0:
        score = (len(matched) / len(jd_skills)) * 100

    return matched, missing, score