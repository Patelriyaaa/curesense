import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the correct Gemini model once
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def check_symptoms(symptoms: str) -> str:
    try:
        # Send the user's symptoms to Gemini
        response = model.generate_content(symptoms)

        # Extract and return the AI's text response
        if hasattr(response, 'text') and response.text:
            return response.text.strip()

        elif hasattr(response, 'candidates') and response.candidates:
            return response.candidates[0].content.parts[0].text.strip()

        else:
            return "Sorry, I couldn't generate a valid response. Please try again later."

    except Exception as e:
        return f"AI error: {str(e)}"
