import re

skills_db = [
    "python",
    "javascript",
    "react",
    "node js",
    "mongodb",
    "sql",
    "docker",
    "aws",
    "git",
    "ai",
    "rag",
    "llm",
    "langchain",
    "genai",
    "agenticai"
]

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_skills(text):
    text = normalize_text(text)
    found_skills = []

    for skill in skills_db:
        normalized_skill = normalize_text(skill)

        if re.search(r"\b" + re.escape(normalized_skill) + r"\b", text):
            found_skills.append(skill)

    return found_skills

# text = "Technical Skills Programming: Python, JavaScript • Web Technologies: HTML, CSS, React.JS, Node.JS, Express JS Databases: MySQL, MongoDB • Tools: GIT and GITHUB, Vs CODE"

# print(extract_skills(text))