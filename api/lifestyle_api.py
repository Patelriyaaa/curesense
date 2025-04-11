import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_lifestyle_recommendations(symptoms, health_conditions, preferences):
    try:
        prompt = f"""
        Based on the symptoms: {symptoms}, health conditions: {health_conditions}, and preferences: {preferences}, 
        give me a list of 5 personalized lifestyle recommendations to improve overall health and well-being.
        """
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating lifestyle recommendations: {e}"
