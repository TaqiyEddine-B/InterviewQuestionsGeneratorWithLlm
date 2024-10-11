""" Main file for the project"""

import streamlit as st
from dotenv import load_dotenv

from src.generator import Generator

load_dotenv()
from src.utils import load_openai_key

st.set_page_config(page_title="Interview Prep App", page_icon=":)", layout="wide", initial_sidebar_state="expanded")

st.title("Interview Preparation App with Streamlit")
st.write("This is a simple app to help you prepare for your next interview. It will compare your CV with the job description and give you a list of questions to prepare for.")


openai_key = load_openai_key()

# read the md file
with open("data/cv.md", "r") as file:
    cv_desc = file.read()

# with open("data/job.md", "r") as file:
#     job_desc = file.read()
job_desc=""

col_cv, col_job, col_questions = st.columns(3)
with col_cv:
    st.subheader("CV",divider ="green")
    st.markdown(cv_desc)
with col_job:
    st.subheader("Job Description", divider="green")
    if st.button("Load an example"):
        with open("data/job.md", "r") as file:
            job_desc = file.read()
        st.text_area("Enter your job description here", value=job_desc, height=800, key="updated_job_desc")
    else:
        job_desc = st.text_area("Enter your job description here", height=800)
with col_questions:
    st.subheader("Questions",divider ="green")
    st.write("List of questions to prepare for")
    if st.button("Generate Questions"):
        data = {"cv": cv_desc, "job": job_desc}


        gen = Generator(data=data)

        questions = gen.generate()
        st.write(questions)
