import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model, scaler, and input columns
model = joblib.load('knn_model.pkl')
scaler = joblib.load('scaler.pkl')
input_columns = joblib.load('columns.pkl')

# Page config
st.set_page_config(page_title="MindCheck AI - Mental Health Predictor", layout="wide")

# ---------- CSS Styling ----------
st.markdown("""
<style>
/* Background */
.main { background-color: #f5f9ff; }

/* Slider and input color */
div[data-baseweb="slider"] > div > div > div {
    background: #4B8BBE !important;
}
div[data-baseweb="slider"] [role="slider"] {
    background-color: #4B8BBE !important;
}
.css-1cpxqw2, .stSlider > div > div {
    color: #4B8BBE !important;
}
.css-16huue1 span {
    color: #4B8BBE !important;
}
.stRadio > div, .stSelectbox > div {
    border-color: #4B8BBE !important;
}
</style>
""", unsafe_allow_html=True)

# --------- Sidebar ---------
with st.sidebar:
    st.image("mental.jpg", width=100)

    st.markdown("<h2 style='color:#4B8BBE; text-align:center;'> MindCheck AI</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; font-size: 15px;'>
    A smart ML-based tool to help distinguish between:<br><br>
     <b>Depression</b><br>
     <b>ME/CFS</b><br><br>
    Based on lifestyle & mental health inputs.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("###  Highlights")
    st.markdown("""
    - No login needed  
    - Private & secure  
    - Built using KNN Model  
    - Designed for awareness
    """)

    st.markdown("---")
    st.markdown("<small style='text-align:center; display:block; color:gray;'>Built with ❤️ using Streamlit</small>", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("<h1 style='text-align:center; color:lightblue;'>Mind Health Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:darkgray;'>Enter your health details to get a real-time diagnosis using AI.</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------- Input Section ----------
st.markdown("""
    <h3 style='text-align: center; color:lightblue;'>🧾 Personal & Health Details</h3>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.slider("🔢 Age", 10, 100, 30)
    gender = st.selectbox("⚧️ Gender", ["Male", "Female"])
    sleep_quality_index = st.slider("😴 Sleep Quality (0–10)", 0.0, 10.0, 5.0)
    brain_fog_level = st.slider("🌫️ Brain Fog Level (0–10)", 0.0, 10.0, 5.0)
    physical_pain_score = st.slider("🩻 Physical Pain (0–10)", 0.0, 10.0, 5.0)
    stress_level = st.slider("😰 Stress Level (0–10)", 0.0, 10.0, 5.0)
    pem_present = st.radio("⚡ PEM Present?", ["Yes", "No"])

with col2:
    depression_score = st.slider("📉 PHQ-9 Score (0–27)", 0.0, 27.0, 10.0)
    fatigue_score = st.slider("🥱 Fatigue Score (0–10)", 0.0, 10.0, 5.0)
    pem_duration = st.slider("🕒 PEM Duration (hrs)", 0.0, 72.0, 10.0)
    sleep_hours = st.slider("🛌 Sleep Hours/Night", 0.0, 12.0, 7.0)
    meditation = st.radio("🧘 Do You Meditate?", ["Yes", "No"])
    work_status = st.selectbox("💼 Work Status", ['Working', 'Not working', 'Partially working'])

# ---------- Encode Inputs ----------
gender = 1 if gender == "Male" else 0
pem_present = 1 if pem_present == "Yes" else 0
meditation = 1 if meditation == "Yes" else 0

# Dummy variables
dummy_inputs = {
    'work_status_Partially working': 1 if work_status == 'Partially working' else 0,
    'work_status_Not working': 1 if work_status == 'Not working' else 0,
    'social_activity_level_Medium': 0,
    'social_activity_level_Very high': 0,
    'exercise_frequency_Daily': 0,
    'exercise_frequency_Often': 0,
    'exercise_frequency_Rarely': 0,
    'exercise_frequency_Never': 0
}

# Base inputs
base_inputs = {
    'age': age,
    'gender': gender,
    'sleep_quality_index': sleep_quality_index,
    'brain_fog_level': brain_fog_level,
    'physical_pain_score': physical_pain_score,
    'stress_level': stress_level,
    'depression_phq9_score': depression_score,
    'fatigue_severity_scale_score': fatigue_score,
    'pem_duration_hours': pem_duration,
    'hours_of_sleep_per_night': sleep_hours,
    'pem_present': pem_present,
    'meditation_or_mindfulness': meditation
}

# Combine inputs
final_inputs = {**base_inputs, **dummy_inputs}
for col in input_columns:
    if col not in final_inputs:
        final_inputs[col] = 0

# Prediction preparation
input_df = pd.DataFrame([final_inputs])[input_columns]
scaled_input = scaler.transform(input_df)

# ---------- Prediction ----------
st.markdown("---")
if st.button("🔍 Predict"):
    prediction = model.predict(scaled_input)[0]
    label = " Depression" if prediction == 0 else " ME/CFS"
    color = "Red" if prediction == 0 else "lightblue"

    st.markdown(f"""
    <div style='padding: 20px; border-radius: 10px; background-color: {color}; color: white; text-align: center;'>
        <h2>Predicted Diagnosis: {label}</h2>
    </div>
    """, unsafe_allow_html=True)
