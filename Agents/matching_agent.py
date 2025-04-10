from difflib import SequenceMatcher
from fuzzywuzzy import fuzz

# Match CV to Job Description
def match_cv_to_jd(cv_data: dict, jd: dict) -> int:
    """
    Improved matching algorithm using fuzzy string matching for both
    job title and skills, resulting in a more accurate match score.
    """
    # Normalize and extract skills lists
    cv_skills = {skill.lower().strip() for skill in cv_data.get("skills", [])}
    jd_skills = {skill.lower().strip() for skill in jd.get("skills", [])}
    
    # Calculate skills matching score as the fraction of matching skills
    if jd_skills:
        matching_skills = cv_skills.intersection(jd_skills)
        skills_match_score = len(matching_skills) / len(jd_skills)
    else:
        skills_match_score = 0

    # Use fuzzy matching for job titles
    cv_title = cv_data.get("title", "").lower().strip()
    jd_title = jd.get("title", "").lower().strip()
    title_similarity = fuzz.token_set_ratio(cv_title, jd_title) / 100 if cv_title and jd_title else 0

    # Combine the scores with weights: 70% skills matching, 30% title similarity
    overall_score = (skills_match_score * 0.7 + title_similarity * 0.3) * 100
    return int(overall_score)
