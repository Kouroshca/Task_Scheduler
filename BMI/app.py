import streamlit as st
from Main import calculate_bmi, bmi_category

st.set_page_config(page_title="BMI Calculator for everyone", layout="centered")

st.title("💪 BMI Calculator")
st.write("Enter your details below to calculate your Body Mass Index.")

with st.form("bmi_form"):
    weight = st.number_input("Weight (kg)", min_value=1.0, step=0.5)
    height = st.number_input("Height (cm)", min_value=50.0, step=1.0)

    submitted = st.form_submit_button("Calculate BMI")

if submitted:
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    st.success(f"Your BMI is **{bmi}**")
    st.info(f"Category: **{category}**")
