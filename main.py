""" Main file for the project"""

import streamlit as st

from src.generator import Generator

from src.utils import load_openai_key

st.set_page_config(page_title="Interview Prep App", page_icon=":)", layout="wide", initial_sidebar_state="expanded")

st.title("Interview Questions Generator")
st.write("This app analyse the provided CV & job description and propose a list of pertinent questions to prepare an interview.")

st.sidebar.info("""Get an OpenAI API key from https://platform.openai.com/api-keys, then you have two options: add it directly in the sidebar OR add it to the secrets section of the Streamlit app.""")
openai_key,is_provided = load_openai_key()
st.sidebar.divider()
st.sidebar.link_button("GitHub", "https://github.com/TaqiyEddine-B/InterviewQuestionsGeneratorWithLlm")

if 'cv_desc' not in st.session_state:
    st.session_state.cv_desc = ""
if 'job_desc' not in st.session_state:
    st.session_state.job_desc = ""


with st.container(border=True):

    col_cv, col_job, col_questions = st.columns(3)
    with col_cv:
        st.subheader("CV",divider ="green")
        with st.container():
            @st.fragment
            def fragment_function():
                if st.button("Load an example", key="load_cv"):
                    with open("data/cv.md", "r") as file:
                        st.session_state.cv_desc =  file.read()

                    st.session_state.cv_desc = st.text_area("Enter your CV here", value=st.session_state.cv_desc, height=800, key="updated_cv_desc")
                else:
                    st.session_state.cv_desc =  st.text_area("Enter your CV here", height=800)
            fragment_function()
    with col_job:
        st.subheader("Job Description", divider="green")
        with st.container():
            @st.fragment
            def fragment_job():
                if st.button("Load an example", key="load_job"):
                    with open("data/job.md", "r") as file:
                        st.session_state.job_desc = file.read()
                    st.text_area("Enter your job description here", value=st.session_state.job_desc, height=800, key="updated_job_desc")
                else:
                    st.session_state.job_desc = st.text_area("Enter your job description here", height=800)
            fragment_job()
    with col_questions:
        st.subheader("Generated Questions",divider ="green")
    
        @st.fragment
        def fragment_questions():
            if st.button("Generate Questions", key="generate_questions"):
                if is_provided:
                    data = {"cv": st.session_state.cv_desc, "job": st.session_state.job_desc}
                    if len(st.session_state.cv_desc) == 0:
                        st.error("Please enter your CV")
                    elif len(st.session_state.job_desc) == 0:
                        st.error("Please enter the job description")
                    else:
                        gen = Generator(data=data)
                        questions = gen.generate()
                        st.write(questions)
                else:
                    st.error("Please enter your OpenAI key")

        fragment_questions()
