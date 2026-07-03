import streamlit as st

st.set_page_config(page_title="AI Job Match Assistant")

st.title("🤖 AI Job Match Assistant")

st.write("Welcome! This app will compare your resume to a job description.")

resume = st.text_area("Paste Resume")

job = st.text_area("Paste Job Description")

if st.button("Analyze"):
    st.success("Great! Version 1 is working.")
