from groq import Groq
import streamlit as st

client = Groq(
    api_key = st.secrets["groq_key"]
)
def generate_feedback(
    resume_text,
    job_description,
    missing_skills
):
    prompt = f"""
    Analyze this resume against the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Missing Skills:
    {missing_skills}

    Give:

    1. Resume improvement suggestions
    2. ATS optimization tips
    3. Better resume bullet points
    4. Skills to add
    5. Weak areas in resume
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content