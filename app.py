import os

import streamlit as st
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# configure genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
    "response_mime_type": "text/plain",
}

safety_settings={
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

system_prompt="""
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowed hospital. Your expertise is crucial in identifiying any anomalies, diseases, or health issue that may be present in the images.

Your Responsibilities include:
1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggess potential next steps, including further tests or treatmets.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

Important Notes:
1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with Doctor before making any medical decisions."
4. Your Insight are Invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above.
"""

model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest", generation_config=generation_config, safety_settings=safety_settings)

# set page config
st.set_page_config(page_title="Medical Image Analysis", page_icon=":robot:")

# set title
st.title("👨‍⚕️ Medical Image Analysis")

# set subtitle
st.subheader("An AI-powered tool to analyze medical images")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

submit_button = st.button("Analyze")
if submit_button:
    
    # process image
    image_data = uploaded_file.getvalue()    
    files = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        }
    ]
    response = model.generate_content([
        files[0],
        system_prompt
    ])
    
    print(response.text)