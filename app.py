import streamlit as st
import google.generativeai as genai

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# set page config
st.set_page_config(page_title="Medical Image Analysis", page_icon=":robot:")

# set title
st.title("👨‍⚕️ Medical Image Analysis")

# set subtitle
st.subheader("An AI-powered tool to analyze medical images")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

submit_button = st.button("Analyze")
if submit_button:
    pass