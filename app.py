import streamlit as st
from api.lifestyle_api import generate_lifestyle_recommendations
from api.nutrition_api import generate_nutrition_plan
from api.exercise_api import generate_exercise_plan
from api.symptom_risk_api import analyze_symptom_risk
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Must be the first Streamlit command
st.set_page_config(page_title="CureSense - AI Health Assistant", layout="wide")

st.markdown("<h1 style='text-align: center; color: #2D9CDB;'>🧠 CureSense - AI Health Assistant</h1>", unsafe_allow_html=True)
st.markdown("Enter your symptoms and health preferences below to receive personalized AI-powered recommendations.", unsafe_allow_html=True)
st.write("---")

# Layout: Two columns
col1, col2 = st.columns(2)

# --- Lifestyle Recommendations ---
with col1:
    st.subheader("🔍 Personalized Lifestyle Recommendations")
    symptoms = st.text_input("Enter your symptoms:")
    health_conditions = st.text_input("Any health conditions:")
    preferences = st.text_input("Your preferences (e.g., vegetarian, likes yoga):")

    if st.button("Get Lifestyle Recommendations"):
        with st.spinner("Generating lifestyle tips..."):
            lifestyle_output = generate_lifestyle_recommendations(symptoms, health_conditions, preferences)
        st.success("Lifestyle Tips:")
        st.write(lifestyle_output)

# --- Nutrition Plan ---
with col2:
    st.subheader("🍎 AI-Powered Nutrition Plan")
    nutrition_goals = st.text_input("Your nutrition goal (e.g., gain weight, improve gut health):")
    dietary_preferences = st.text_input("Dietary preferences (e.g., vegetarian, dairy-free):")

    if st.button("Get Nutrition Plan"):
        with st.spinner("Generating nutrition plan..."):
            nutrition_output = generate_nutrition_plan(nutrition_goals, dietary_preferences)
        st.success("Nutrition Plan:")
        st.write(nutrition_output)

st.write("---")

# Layout: Bottom Section (Exercise & Symptom Risk)
col3, col4 = st.columns(2)

with col3:
    st.subheader("💪 Exercise Recommendations")
    fitness_level = st.selectbox("Select your fitness level:", ["Beginner", "Intermediate", "Advanced"])
    exercise_goal = st.text_input("Your goal (e.g., build stamina, flexibility, weight loss):")

    if st.button("Get Exercise Plan"):
        with st.spinner("Generating exercise recommendations..."):
            exercise_output = generate_exercise_plan(fitness_level, exercise_goal)
        st.success("Exercise Plan:")
        st.write(exercise_output)

with col4:
    st.subheader("🧬 Symptom Risk Analyzer")
    risk_input = st.text_input("Enter your symptoms to check for risks (cancer, disease, deficiency):")

    if st.button("Analyze Symptom Risk"):
        if risk_input.strip():
            with st.spinner("Analyzing symptoms..."):
                risk_analysis = analyze_symptom_risk(risk_input)
            st.success("Symptom Risk Analysis:")
            st.write(risk_analysis)
        else:
            st.warning("Please enter your symptoms to analyze risk.")