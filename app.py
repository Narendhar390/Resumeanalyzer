import streamlit as st
import fitz
from resumeanalyzer import generate_feedback
from extracter import extract_skills 
from matcher import match_skills
st.title("AI Resume Analyzer")
upload_file=st.file_uploader("Upload Resume",type=["pdf"])
job_description=st.text_area("Job discription")
def extract_text_from_pdf(upload_file):
    text=""
    pdf=fitz.open(
        stream=upload_file.read(),
        filetype="pdf"
    )
    for page in pdf:
        text+=page.get_text()
    return text
if st.button("Analyze"):
    resume_text=extract_text_from_pdf(upload_file)
    #st.subheader("Extracted resume text")
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)
    matched, missing, score=match_skills(resume_skills,jd_skills)
    st.subheader("Resume Skills")
    st.markdown(resume_skills)
    st.subheader("Job Description Skills")
    st.markdown(jd_skills)
    st.subheader("Matched Skills")
    st.markdown(matched)
    st.subheader("Missing Skills")
    st.markdown(missing)
    st.subheader("Match Score")
    st.markdown(f"{score:.2f}%")
    feedback = generate_feedback(
    resume_text,
    job_description,
    missing
    )
    st.markdown(feedback)
