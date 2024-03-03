""" Main file for the project"""
import streamlit as st
from generator import Generator

st.set_page_config(page_title="Interview Prep App", page_icon=":sunglasses:", layout="wide", initial_sidebar_state="expanded")

st.title("Interview Preparation App with Streamlit")
st.write("This is a simple app to help you prepare for your next interview. It will compare your CV with the job description and give you a list of questions to prepare for.")
# read the md file
with open("data/cv.md", "r") as file:
    cv_desc = file.read()

with open("data/job.md", "r") as file:
    job_desc = file.read()


col_cv, col_job, col_questions = st.columns(3)
with col_cv:
    st.subheader("CV",divider ="green")
    st.markdown(cv_desc)
with col_job:
    st.subheader("Job Description",divider ="green")
    st.markdown(job_desc)
with col_questions:
    st.subheader("Questions",divider ="green")
    st.write("List of questions to prepare for")
    if st.button("Generate Questions"):
        data = {"cv": cv_desc, "job": job_desc}


        gen = Generator(data=data)

        questions = gen.generate()
        st.write(questions)
