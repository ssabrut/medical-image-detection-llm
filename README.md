# AI-Powered Medical Image Analysis Tool

This project leverages Google Gemini and Streamlit to build an advanced AI-powered tool for analyzing medical images. By integrating Google's cutting-edge AI capabilities with Streamlit's user-friendly interface, this tool aims to assist healthcare professionals in diagnosing and evaluating medical conditions from images efficiently and accurately.

#### Installation

To install the required packages, run:

```bash
pip install -r requirements.txt
```

#### Setting Up Google Gemini API
1. ##### Create Google Gemini API Key:
   - Visit the Google Cloud Console and create a new project.
   - Enable the Google Gemini API for your project.
   - Create credentials (API key) and copy it.
2. ##### Create .env File:
   - Create a file named .env in the root directory of your project.
   - Add the following line to the .env file:
     ```bash
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

#### Running the Application

To run the application, execute the following command:

```bash
streamlit run app.py
```

##### Contributors
- Michael (ssabrut) - Project Lead & Developer
