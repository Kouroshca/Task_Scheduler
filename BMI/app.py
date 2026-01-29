import streamlit as st
from Main import calculate_bmi, bmi_category

st.set_page_config(page_title="BMI Calculator for everyone", layout="centered")

st.title(" BMI Calculator ")

# Input weight and height
weight_unit = st.radio("Select Weight Unit:", ["Kilograms (kg)", "Pounds (lbs)"], horizontal =True)
height_unit = st.radio("Select Height Unit:", ["Centimeters (cm)", "Inches (in)"], horizontal =True)

if weight_unit == "Kilograms (kg)":
    weight = st.number_input("Enter your weight (kg):", min_value=1.0)
    weight_kg = weight
else:
    weight = st.number_input("Enter your weight (lbs):", min_value=1.0)
    weight_kg = weight * 0.453592


# height input
if height_unit == "Centimeters (cm)":
    height = st.number_input("Enter your height (cm):", min_value=0.5)
    height_m = height / 100

else: # Inches
    height = st.number_input("Enter your height (in):", min_value=0.5)
    height_m = height * 0.0254

#buttons

if st.button("Calculate BMI"):
    bmi, category = calculate_bmi(weight_kg, height_m)

    if bmi is None:
        st.error("Please enter valid weight and height values.")

    else: 
        st.subheader("Your BMI Results:")
        st.metric("BMI Value:", f"{bmi:.2f}")

        if category == "Underweight":
            st.info(category)
        elif category == "Normal":
            st.success(category)
        elif category == "Overweight":
            st.warning(category)
        elif category == "Obese":
            st.error(category)