import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_exercise_plan(fitness_level, goal):
    try:
        prompt = f"""
        I am a {fitness_level.lower()} and my goal is to {goal}. Please create a 5-day workout plan, 
        including type of exercises, duration, and rest days. Also, include warm-up and cool-down suggestions.
        """
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating exercise recommendations: {e}"
