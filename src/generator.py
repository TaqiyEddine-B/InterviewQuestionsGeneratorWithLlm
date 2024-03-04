""" Main module for the project"""
import os

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class Generator:
    def __init__(self, data):
        os.environ["OPENAI_API_KEY"] = st.secrets["openai_key"]

        self.data = data

    def generate(self):

        prompt = ChatPromptTemplate.from_template("analyze the following cv and job description and generate 10 questions to prepare for the interview. \n\nCV: {cv}\n\nJob Description: {job}")
        model = ChatOpenAI(model="gpt-4")
        output_parser = StrOutputParser()

        chain = prompt | model | output_parser

        result = chain.invoke({"cv": self.data['cv'], "job": self.data['job']})
        return result
