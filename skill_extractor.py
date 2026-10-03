resume_text = """
I am a Computer Science student.
I know Python, SQL, HTML, CSS and React.
I have basic knowledge of Machine Learning.
"""

skills = [
    "Python",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    "React",
    "Machine Learning",
    "JavaScript",
    "Django",
    "FastAPI",
    "Git",
    "Docker"
]

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
        "Git",
        "Spring Boot"
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

# Find skills from resume
found_skills = []

for skill in skills:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)

# Select target job
target_role = "Python Developer"

required_skills = job_roles[target_role]

print("Target Job Role:", target_role)

print("\nSkills found in resume:")
for skill in found_skills:
    print("-", skill)

print("\nRequired skills for", target_role, ":")
for skill in required_skills:
    print("-", skill)



# Find matched and missing skills

matched_skills = []
missing_skills = []

for skill in required_skills:
    if skill.lower() in [s.lower() for s in found_skills]:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

# Calculate skill match percentage

total_required = len(required_skills)
total_matched = len(matched_skills)

skill_match_percentage = (total_matched / total_required) * 100


# Display result

print("\n--- Skill Gap Analysis ---")

print("\nMatched Skills:")
for skill in matched_skills:
    print("✓", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("✗", skill)

print("\nSkill Match Percentage:",
      round(skill_match_percentage, 2), "%")


# Learning recommendations for missing skills

recommendations = {
    "Git": "Learn Git basics, GitHub, commits, branches and pull requests.",
    "Django": "Learn Django fundamentals and build a simple web application.",
    "FastAPI": "Learn FastAPI and build a simple REST API.",
    "Java": "Learn Java fundamentals, OOP concepts and basic problem solving.",
    "SQL": "Learn SQL queries, joins, subqueries and database concepts.",
    "HTML": "Learn HTML structure, forms, tables and semantic elements.",
    "CSS": "Learn CSS styling, Flexbox, Grid and responsive design.",
    "JavaScript": "Learn JavaScript fundamentals, DOM and basic web programming.",
    "React": "Learn React components, props, state and hooks.",
    "Machine Learning": "Learn supervised learning, classification and regression.",
    "Deep Learning": "Learn neural networks, CNNs and basic deep learning concepts.",
    "Docker": "Learn Docker images, containers and basic deployment."
}

print("\n--- Personalized Learning Recommendations ---")

for skill in missing_skills:
    if skill in recommendations:
        print("\nMissing Skill:", skill)
        print("Recommendation:", recommendations[skill])


# Final Resume Skill Gap Report

print("\n========================================")
print("       AI RESUME SKILL GAP ANALYZER")
print("========================================")

print("\nTarget Job Role:")
print(target_role)

print("\nResume Skills:")
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
        print("-", skill, ":", recommendations[skill])

print("\n========================================")
print("              END OF REPORT")
print("========================================")



from pypdf import PdfReader

# -------------------------------
# STEP 1: Read Resume PDF
# -------------------------------

reader = PdfReader("Akshaya.pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        resume_text += text


# -------------------------------
# STEP 2: Skills Database
# -------------------------------

skills = [
    "Python",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    "React",
    "JavaScript",
    "Machine Learning",
    "Deep Learning",
    "Django",
    "FastAPI",
    "Git",
    "Docker"
]


# -------------------------------
# STEP 3: Detect Skills
# -------------------------------

found_skills = []

for skill in skills:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)


# -------------------------------
# STEP 4: Display Results
# -------------------------------

print("\n==============================")
print("   RESUME SKILL ANALYSIS")
print("==============================")

if found_skills:
    print("\nSkills detected in resume:")

    for skill in found_skills:
        print("✓", skill)

else:
    print("\nNo matching skills found.")

print("\nTotal Skills Found:", len(found_skills))