import streamlit as st
import datetime

from Agents.db_agent import init_db, save_match, get_matches
from Agents.jd_parser_agent import parse_xlsx_jd
from Agents.cv_parser_agent import parse_pdf_cv
from Agents.matching_agent import match_cv_to_jd
from Agents.interview_scheduler_agent import schedule_interview, get_upcoming_interviews

# Initialize the database
init_db()

# Streamlit app configuration
st.set_page_config(page_title="AI Job Screener", layout="wide", initial_sidebar_state="expanded")

# App title and header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 AI-Powered Job Screener</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar for JD Upload and Selection
st.sidebar.header("Job Description")
jd_file = st.sidebar.file_uploader("Upload Job Description (Excel)", type=["xlsx"])
jd_data = []
selected_title = None

if jd_file:
    jd_data = parse_xlsx_jd(jd_file)
    st.sidebar.success("JD Parsed Successfully!")
    job_titles = [jd['title'] for jd in jd_data]
    selected_title = st.sidebar.selectbox("Select Job Title", job_titles)

with st.container():
    # Step 1: CV Upload and Filtering Section
    if selected_title:
        st.subheader(f"Candidate Filtering for *{selected_title}*")
        filtered_jd_data = [jd for jd in jd_data if jd['title'] == selected_title]

        cv_files = st.file_uploader("Upload Candidate CVs (PDF)", type=["pdf"], accept_multiple_files=True)
        show_interview_scheduling = False

        if cv_files:
            results = []
            progress_bar = st.progress(0)
            num_files = len(cv_files)
            for index, cv_file in enumerate(cv_files):
                cv_data = parse_pdf_cv(cv_file)
                score = 0
                for jd in filtered_jd_data:
                    score = match_cv_to_jd(cv_data, jd)
                    save_match(cv_data["name"], score)
                    results.append((cv_data["name"], score, jd['title'], jd['skills']))
                progress_bar.progress((index + 1) / num_files)
            progress_bar.empty()

            st.subheader("Shortlisted Candidates")
            results.sort(key=lambda x: x[1], reverse=True)
            for name, score, job_title, skills in results:
                candidate_col, details_col = st.columns([1, 3])
                with candidate_col:
                    st.markdown(f"**{name}**")
                with details_col:
                    st.markdown(f"*Job Title:* {job_title}")
                    st.markdown(f"*Match Score:* {score}")
                    st.markdown(f"*Matched Skills:* {', '.join(skills)}")
            st.success("CV Parsing Completed!")

            if results:
                show_interview_scheduling = True

        # Step 2: Interview Scheduling using Tabs
        if show_interview_scheduling:
            st.subheader("Interview Scheduling")
            tab1, tab2 = st.tabs(["Schedule Interview", "Upcoming Interviews"])
            
            with tab1:
                candidate = st.text_input("Candidate Name")
                interviewer = st.text_input("Interviewer Name")
                interview_date = st.date_input("Interview Date", datetime.date.today())
                interview_time = st.time_input("Interview Time", datetime.datetime.now().time())
                
                if st.button("Schedule Interview"):
                    interview_datetime = datetime.datetime.combine(interview_date, interview_time)
                    interview_details = schedule_interview(candidate, interviewer, interview_datetime)
                    st.success(
                        f"Interview scheduled for {candidate} with {interviewer} on "
                        f"{interview_datetime.strftime('%Y-%m-%d %H:%M')}"
                    )
            
            with tab2:
                st.markdown("### Upcoming Interviews")
                interviews = get_upcoming_interviews()
                if interviews:
                    for interview in interviews:
                        st.write(interview)
                else:
                    st.info("No upcoming interviews found.")

    # History Viewer in an Expandable Section
    with st.expander("📜 Past Match History"):
        history = get_matches()
        for name, score in history:
            st.write(f"{name} — {score}")
