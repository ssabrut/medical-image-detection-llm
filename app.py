import streamlit as st
import google.generativeai as genai

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# set page config
st.set_page_config(page_title="VitalImage Analysis", page_icon=":robot:")