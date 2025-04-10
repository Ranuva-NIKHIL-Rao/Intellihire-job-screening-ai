# AI Job Screener

An AI-powered job screener application with interview scheduling capabilities using Streamlit and Python. The project parses job descriptions and candidate CVs, matches them using fuzzy logic, and schedules interviews via a modern UI.

## Features

- **Job Description Upload:** Parse Excel files containing Job Descriptions.
- **Candidate CV Parsing:** Upload and parse PDFs to extract candidate names and skills.
- **Intelligent Matching:** Fuzzy matching between candidate skills and job requirements.
- **Interview Scheduling:** Schedule and view upcoming interviews.
- **Database Storage:** Store match history using SQLite.

## Setup

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the app:
   ```sh
   streamlit run app.py
   ```

## Directory Structure

```
app.py
database.db
Agents/
    cv_parser_agent.py
    db_agent.py
    interview_scheduler_agent.py
    jd_parser_agent.py
    matching_agent.py
    interview-scheduler/
data/
    [Candidate PDFs]
```
## 🤝 Team

This project was developed as part of the Gen AI Hackathon (Accenture x GeeksforGeeks) by:

- [Nikhil Rao Ranuva](https://github.com/Ranuva-NIKHIL-Rao) – Lead Developer, Streamlit UI, Matching Agent, Architecture
- [UV Krishna Teja](https://github.com/UVKrishnaTeja) – JD/CV Parsing, Database Agent, Interview Scheduler

