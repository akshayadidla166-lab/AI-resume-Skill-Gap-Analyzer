from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
import PyPDF2
import io
import re

app = FastAPI()

# Skills database
ALL_SKILLS = ["java", "python", "sql", "dbms", "oops", "data structures", "github", "vs code", "react", "aws", "html", "css", "javascript"]

def extract_text_from_pdf(file_bytes):
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.lower()
    except:
        return file_bytes.decode('latin1', errors='ignore').lower()

def find_skills(text):
    return [s for s in ALL_SKILLS if s in text.lower()]

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html><body style="font-family:Arial; text-align:center; padding:30px; background:#f5f7ff;">
        <h1 style="color:#4a3aff;">AI Resume Skill Gap Analyzer</h1>
        <h3>by Didla Akshaya</h3>
        <div style="background:white; padding:20px; border-radius:12px; max-width:500px; margin:20px auto; box-shadow:0 4px 12px #ccc;">
        <form action="/analyze" method="post" enctype="multipart/form-data">
            <p><b>Upload Resume (PDF)</b><br><input type="file" name="resume" required></p>
            <p><b>Paste Job Description</b><br><textarea name="job_desc" rows="6" cols="45" placeholder="Ex: Need Java, Python, React, AWS, SQL" required></textarea></p>
            <button style="background:#4a3aff; color:white; padding:10px 25px; border:none; border-radius:8px;" type="submit">Analyze Gap</button>
        </form></div>
    </body></html>
    """

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(resume: UploadFile = File(...), job_desc: str = Form(...)):
    resume_bytes = await resume.read()
    resume_text = extract_text_from_pdf(resume_bytes)
    
    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_desc)
    
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    match_percent = int(len(matched)/len(job_skills)*100) if job_skills else 0

    return f"""
    <html><body style="font-family:Arial; text-align:center; padding:30px; background:#f5f7ff;">
        <h1>Analysis Result</h1>
        <div style="background:white; padding:20px; border-radius:12px; max-width:600px; margin:auto; text-align:left;">
            <h2 style="color:green;">Match: {match_percent}%</h2>
            <p><b>Your Skills Found:</b> {', '.join(resume_skills) or 'None'}</p>
            <p><b>Job Needs:</b> {', '.join(job_skills)}</p>
            <p><b style="color:green;">Matched Skills:</b> {', '.join(matched) or 'None'}</p>
            <p><b style="color:red;">Missing Skills (Gap):</b> {', '.join(missing) or 'No Gap! You are perfect!'}</p>
            <hr>
            <p><b>Roadmap:</b> Learn -> {', '.join(missing)}</p>
            <br><a href="/">← Try Again</a>
        </div>
    </body></html>
    """
