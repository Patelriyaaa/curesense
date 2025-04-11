import streamlit as st
from api.symptom_api import check_symptoms
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# App title and description
st.set_page_config(page_title="CureSense - Symptom Checker", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #2D9CDB;'>🩺 CureSense - AI Symptom Checker</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "Enter your symptoms below. CureSense will provide possible common causes and recommend next steps — powered by AI.",
    unsafe_allow_html=True,
)

# Input section
user_symptoms = st.text_area(
    "Describe your symptoms (e.g., 'sore throat, fever, fatigue')",
    height=120,
    placeholder="Start typing here..."
)

if st.button("Check Symptoms"):
    if user_symptoms.strip() != "":
        with st.spinner("Analyzing symptoms..."):
            result = check_symptoms(user_symptoms)
        st.success("AI Response:")
        st.markdown(result)
    else:
        st.warning("Please enter your symptoms.")
