""" Main file for the project"""

import streamlit as st

from src.generator import Generator

from src.utils import load_openai_key

st.set_page_config(page_title="Interview Prep App", page_icon=":)", layout="wide", initial_sidebar_state="expanded")

st.title("Interview Questions Generator")
st.write("This app analyse the provided CV & job description and propose a list of pertinent questions to prepare an interview.")


openai_key,is_provided = load_openai_key()


st.sidebar.divider()
st.sidebar.subheader("Steps")
st.sidebar.write("1. Enter your OpenAI API key")
st.sidebar.info("""Get an OpenAI API key from https://platform.openai.com/api-keys, then you have two options: add it directly in the sidebar OR add it to the secrets section of the Streamlit app.""")

st.sidebar.write("2. Enter your CV")
st.sidebar.write("3. Enter the job description")
st.sidebar.write("4. Click on 'Generate Questions'")


st.sidebar.divider()

st.sidebar.subheader("About")
st.sidebar.link_button("GitHub Repo of the project", "https://github.com/TaqiyEddine-B/InterviewQuestionsGeneratorWithLlm")
st.sidebar.link_button("My website", "https://taqiyeddine.com")

if 'cv_desc' not in st.session_state:
    with open("data/cv.md", "r") as file:
        st.session_state.cv_desc =  file.read()
if 'job_desc' not in st.session_state:
    with open("data/job.md", "r") as job_file:
        st.session_state.job_desc =  job_file.read()

height = 800
col_cv, col_job, col_questions = st.columns([1, 1, 1.5])
with col_cv:
    st.subheader("CV",divider ="blue")
    with st.container():
        @st.fragment
        def update_cv_text_area():
            """Update the text area of the CV"""
            st.session_state.cv_desc =  st.text_area("Enter your CV here", value=st.session_state.cv_desc, height=height)
        update_cv_text_area()
with col_job:
    st.subheader("Job Description", divider="blue")
    with st.container():
        @st.fragment
        def update_job_description():
            """Update the text area of the job description"""
            st.text_area("Enter your job description here", value=st.session_state.job_desc, height=height, key="updated_job_desc")

        update_job_description()
with col_questions:
    st.subheader("Generated Questions",divider ="green")
    with st.container(border=True,height=height+32):
        @st.fragment
        def generate_questions_fragment():
            """Generate questions"""
            if st.button("Generate Questions", key="generate_questions"):
                if is_provided:
                    data = {"cv": st.session_state.cv_desc, "job": st.session_state.job_desc}
                    if len(st.session_state.cv_desc) == 0:
                        st.error("Please enter your CV")
                    elif len(st.session_state.job_desc) == 0:
                        st.error("Please enter the job description")
                    else:
                        gen = Generator(data=data,key=openai_key)
                        questions = gen.generate()
                        st.write(questions)
                else:
                    st.error("Please enter your OpenAI key")

        generate_questions_fragment()
