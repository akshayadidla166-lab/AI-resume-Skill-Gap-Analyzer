from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
import os

app = FastAPI(
    title="AI Resume Skill Gap Analyzer"
)


# Skills database
skills = [
    "Python",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Machine Learning",
    "Deep Learning",
    "Django",
    "FastAPI",
    "Git",
    "Docker"
]


# Job roles and required skills
job_roles = {
    "Python Developer": [
        "Python",
        "SQL",
        "Git",
        "Django",
        "FastAPI"
    ],

    "Java Developer": [
        "Java",
        "SQL",
        "Git"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ],

    "AI/ML Engineer": [
        "Python",
        "Machine Learning",
        "SQL",
        "Git",
        "Deep Learning"
    ]
}


@app.get("/")
def home():
    return {
        "message": "AI Resume Skill Gap Analyzer is running"
    }


@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_role: str = "Python Developer"
):

    # Check file type
    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Please upload a PDF resume."
        }


    # Save uploaded file
    file_path = "uploaded_resume.pdf"

    with open(file_path, "wb") as f:
        f.write(await file.read())


    # Read PDF
    reader = PdfReader(file_path)

    resume_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            resume_text += text


    # Detect skills
    found_skills = []

    for skill in skills:

        if skill.lower() in resume_text.lower():
            found_skills.append(skill)


    # Check job role
    if job_role not in job_roles:

        os.remove(file_path)

        return {
            "error": "Invalid job role.",
            "available_roles": list(job_roles.keys())
        }


    required_skills = job_roles[job_role]


    # Compare skills
    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in [s.lower() for s in found_skills]:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)


    # Calculate percentage
    total_required = len(required_skills)
    total_matched = len(matched_skills)

    if total_required > 0:
        match_percentage = (
            total_matched / total_required
        ) * 100
    else:
        match_percentage = 0


    # Delete uploaded file
    os.remove(file_path)


    # Return result
    return {
        "job_role": job_role,
        "resume_skills": found_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_match_percentage": round(
            match_percentage, 2
        )
    }