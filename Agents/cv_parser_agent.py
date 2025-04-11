import fitz   # PyMuPDF
import tempfile

def parse_pdf_cv(file):
    """
    Parse a PDF file-like object and extract the name and skills from its text.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    with fitz.open(tmp_path) as doc:
        text = " ".join(page.get_text() for page in doc)

    return {
        "name": extract_name(text),
        "skills": extract_skills(text)
    }

def extract_name(text):
    """
    Extract the first non-empty line from the text as the candidate's name.
    """
    for line in text.strip().split("\n"):
        if line.strip():
            return line.strip()
    return "Unknown"

def extract_skills(text):
    """
    Extract known skills from a predefined skill bank.
    """
    skill_bank = [
        "Python", "Java", "C++", "Spring", "Spring Boot", "MySQL", "SQL", "Kafka", "Azure", "Azure DevOps",
        "Cloud", "AWS", "Google Cloud", "Docker", "Kubernetes", "Linux", "Git", "CI/CD",
        "Cybersecurity", "Penetration Testing", "Risk Assessment", "Network Security",
        "AI Ethics", "AI", "Data Science", "Data Scientist", "Full-Stack", "Full-Stack Developer",
        "Predictive Modeling", "Machine Learning", "Deep Learning", "NLP",
        "REST APIs", "Flask", "Django", "React", "Node.js", "TensorFlow", "PyTorch"
    ]
    text_lower = text.lower()
    found_skills = {skill for skill in skill_bank if skill.lower() in text_lower}
    return list(found_skills)
