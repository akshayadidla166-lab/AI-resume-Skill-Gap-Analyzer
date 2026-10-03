from pypdf import PdfReader

# Read the resume PDF
reader = PdfReader("Akshaya.pdf")

resume_text = ""

# Extract text from every page
for page in reader.pages:
    text = page.extract_text()

    if text:
        resume_text += text

# Display extracted text
print("========== RESUME TEXT ==========")
print(resume_text)
print("=================================")