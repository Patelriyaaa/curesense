import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_nutrition_plan(goal, preferences):
    try:
        prompt = f"""
        I'm trying to {goal}. Please generate a weekly nutrition plan with meals for each day, 
        considering my preferences: {preferences}. Be specific with meals.
        """
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating nutrition plan: {e}"
