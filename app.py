import streamlit as st
import re

st.set_page_config(page_title="AI Job Match Assistant")

st.title(" AI Job Match Assistant")

st.write("Welcome! This app will compare your resume to a job description.")

resume = st.text_area("Paste Resume")

job = st.text_area("Paste Job Description")

if st.button("Analyze"):

    resume_words = set(re.findall(r"\b[a-zA-Z0-9+#.-]+\b", resume.lower()))
    job_words = set(re.findall(r"\b[a-zA-Z0-9+#.-]+\b", job.lower()))
    stop_words = {"and", "for", "the", "a", "an", "to", "of", "in", "with", "looking", "experience"}

    resume_words = resume_words.difference(stop_words)
    job_words = job_words.difference(stop_words)
    matches = resume_words.intersection(job_words)
    missing_keywords = job_words.difference(resume_words)

    score = int((len(matches) / max(len(job_words), 1)) * 100)

    st.subheader("Analysis Results")

    st.metric("Match Score", f"{score}%")

    st.write("### Matching Keywords")
    st.write(", ".join(sorted(matches)))

    st.write("### Missing Keywords")
    st.write(", ".join(sorted(missing_keywords)))