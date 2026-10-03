from pypdf import PdfReader

# --------------------------------
# STEP 1: Read Resume PDF
# --------------------------------

reader = PdfReader("Akshaya.pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        resume_text += text


# --------------------------------
# STEP 2: Skills Database
# --------------------------------

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


# --------------------------------
# STEP 3: Job Roles
# --------------------------------

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


# --------------------------------
# STEP 4: Detect Resume Skills
# --------------------------------

found_skills = []

for skill in skills:

    if skill.lower() in resume_text.lower():
        found_skills.append(skill)


# --------------------------------
# STEP 5: Select Job Role
# --------------------------------

print("\nAvailable Job Roles:")

for role in job_roles:
    print("-", role)

target_role = input("\nEnter target job role: ")

if target_role not in job_roles:
    print("\nInvalid job role.")
    exit()


required_skills = job_roles[target_role]


# --------------------------------
# STEP 6: Skill Gap Analysis
# --------------------------------

matched_skills = []
missing_skills = []

for skill in required_skills:

    if skill.lower() in [s.lower() for s in found_skills]:
        matched_skills.append(skill)

    else:
        missing_skills.append(skill)


# --------------------------------
# STEP 7: Calculate Match Percentage
# --------------------------------

total_required = len(required_skills)
total_matched = len(matched_skills)

skill_match_percentage = (
    total_matched / total_required
) * 100


# --------------------------------
# STEP 8: Recommendations
# --------------------------------

recommendations = {

    "Python":
        "Learn Python programming and problem solving.",

    "SQL":
        "Learn SQL queries, joins and database concepts.",

    "Git":
        "Learn Git, GitHub, commits and branches.",

    "Django":
        "Learn Django and build a simple web application.",

    "FastAPI":
        "Learn FastAPI and build a REST API.",

    "Java":
        "Learn Java, OOP concepts and basic DSA.",

    "HTML":
        "Learn HTML structure, forms and semantic elements.",

    "CSS":
        "Learn CSS, Flexbox, Grid and responsive design.",

    "JavaScript":
        "Learn JavaScript fundamentals and DOM.",

    "React":
        "Learn React components, props, state and hooks.",

    "Machine Learning":
        "Learn ML algorithms, preprocessing and model evaluation.",

    "Deep Learning":
        "Learn neural networks and deep learning fundamentals.",

    "Docker":
        "Learn Docker containers and basic deployment."
}


# --------------------------------
# STEP 9: Final Report
# --------------------------------

print("\n")
print("========================================")
print("      AI RESUME SKILL GAP ANALYZER")
print("========================================")

print("\nTarget Job Role:")
print(target_role)

print("\nSkills Found in Resume:")

for skill in found_skills:
    print("✓", skill)

print("\nMatched Skills:")

for skill in matched_skills:
    print("✓", skill)

print("\nMissing Skills:")

for skill in missing_skills:
    print("✗", skill)

print("\nSkill Match Percentage:")
print(round(skill_match_percentage, 2), "%")

print("\nLearning Recommendations:")

for skill in missing_skills:

    if skill in recommendations:
        print("\n", skill)
        print("→", recommendations[skill])

print("\n========================================")
print("             END OF REPORT")
print("========================================")