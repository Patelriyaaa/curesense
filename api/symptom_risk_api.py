import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro-latest")

def analyze_symptom_risk(symptoms: str) -> str:
    try:
        prompt = f"""
        The user has the following symptoms: {symptoms}.
        Based on this, analyze the risk of:
        1. Potential cancer-related symptoms (if any)
        2. Other possible diseases
        3. Any likely nutritional deficiencies
        
        Provide the analysis in a clear, user-friendly way with actionable advice. Be honest if symptoms do not clearly indicate anything serious.
        """
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating symptom risk analysis: {e}"
