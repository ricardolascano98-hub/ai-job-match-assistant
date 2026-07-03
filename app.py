import streamlit as st

st.set_page_config(page_title="AI Job Match Assistant")

st.title("🤖 AI Job Match Assistant")

st.write("Welcome! This app will compare your resume to a job description.")

resume = st.text_area("Paste Resume")

job = st.text_area("Paste Job Description")

if st.button("Analyze"):

    resume_words = set(resume.lower().split())
    job_words = set(job.lower().split())

    matches = resume_words.intersection(job_words)

    score = int((len(matches) / max(len(job_words), 1)) * 100)

    st.subheader("Analysis Results")

    st.metric("Match Score", f"{score}%")

    st.write("### Matching Keywords")

    st.write(", ".join(sorted(matches)))
