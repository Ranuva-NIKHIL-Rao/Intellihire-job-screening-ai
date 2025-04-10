import pandas as pd

# Parse Job Description from XLSX
def parse_xlsx_jd(file):
    df = pd.read_excel(file)

    skill_bank = [
        "Python", "Java", "C++", "C#", "Spring", "Spring Boot", "Flask", "Django", "Node.js", "React",
        "SQL", "MySQL", "NoSQL", "Data Warehousing", "BigQuery",
        "AI", "AI Ethics", "Data Science", "Data Scientist", "Predictive Modeling",
        "Machine Learning", "Deep Learning", "NLP", "Reinforcement Learning",
        "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "A/B Testing",
        "Cloud", "AWS", "Azure", "Azure DevOps", "Google Cloud", "CI/CD", "Docker", "Kubernetes",
        "Infrastructure as Code", "Cloud-native Tools", "Linux",
        "Cybersecurity", "Penetration Testing", "Risk Assessment", "Network Security",
        "Secure Architecture", "Incident Response", "Security Assessments",
        "Git", "JIRA", "Confluence", "Figma", "Sketch", "Adobe XD", "Tableau", "Kafka", "Hadoop", "Spark",
        "Robotics", "Embedded Systems", "Microcontrollers", "Real-Time Operating Systems",
        "Motion Planning", "Sensor Integration",
        "Full-Stack", "Full-Stack Developer", "REST APIs",
        "Agile", "Scrum", "Product Management", "Roadmapping", "Technical Leadership",
        "User Research", "Wireframing", "Prototyping", "Stakeholder Management",
        "Blockchain", "Smart Contracts", "Cryptography", "Consensus Algorithms",
        "Quality Assurance", "Test Automation", "Bug Reporting",
        "Business Intelligence", "BI Tools", "Dashboards", "Data Visualization"
    ]
    
    jd_data = []
    for _, row in df.iterrows():
        title = row.get("Job Title", "Unknown")
        description = str(row.get("Job Description", ""))

        found_skills = []
        for skill in skill_bank:
            if skill.lower() in description.lower():
                found_skills.append(skill)

        jd_data.append({
            "title": title,
            "skills": found_skills,
            "experience": row.get("Experience", ""),
            "domain": row.get("Domain", "")
        })
    
    return jd_data
