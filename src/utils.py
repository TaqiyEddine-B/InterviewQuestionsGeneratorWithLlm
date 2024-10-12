""" Utils module for the Streamlit app."""

import os
import streamlit as st


def load_openai_key()->str:
    """
    Load the OpenAI API key from the environment variable or user input.

    This function checks for the OpenAI API key in the following order:
    1. Streamlit secrets (secrets.toml file)
    2. User input via Streamlit sidebar

    Returns:
        tuple[str, bool]: A tuple containing:
            - str: The OpenAI API key
            - bool: A flag indicating whether a valid key was provided
    """
    key =""
    is_provided = False
    if "OPENAI_API_KEY" in st.secrets :
        key = st.secrets["OPENAI_API_KEY"]
        st.sidebar.success('Using OpenAI Key from sectrets.toml')
        is_provided = True
    else:
        key = st.sidebar.text_input('Enter your OpenAI API key', type="password")
        if len(key) > 0:
            os.environ["OPENAI_API_KEY"] = key
            st.sidebar.success('Using the provided OpenAI Key')
            is_provided = True
        else:
            st.sidebar.error('No OpenAI Key')
    return key, is_provided
