import streamlit as st
import google.generativeai as genai

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# set page config
st.set_page_config(page_title="Vital Image Analysis", page_icon=":robot:")

# set title
st.title("👨‍⚕️ Vital Image Analysis")

# set subtitle
st.subheader("An AI-powered tool to analyze medical images")