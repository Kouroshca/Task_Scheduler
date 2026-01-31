import streamlit as st
from Main import calculate_bmi
from ml_model import predict_bmi_category
from food_recommender import recommend_food


st.set_page_config(page_title="BMI Calculator for everyone", layout="centered")

st.title(" BMI Calculator ")

# Input weight and height
weight_unit = st.radio("Select Weight Unit:", ["Kilograms (kg)", "Pounds (lbs)"], horizontal=True)
height_unit = st.radio("Select Height Unit:", ["Centimeters (cm)", "Feet (ft)"], horizontal=True)

if weight_unit == "Kilograms (kg)":
    weight = st.number_input("Enter your weight (kg):", min_value=1.0)
    weight_kg = weight
else:
    weight = st.number_input("Enter your weight (lbs):", min_value=1.0)
    weight_kg = weight * 0.453592


# height input
if height_unit == "Centimeters (cm)":
    height = st.number_input(
        "Enter your height (cm):",
        min_value=50.0,
        max_value=250.0
    )
    height_m = height / 100
else:
    height = st.number_input(
        "Enter your height (ft):",
        min_value=3.0,
        max_value=8.0
    )
    height_m = height * 0.3048

#buttons

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight_kg, height_m)

    if bmi is None:
        st.error("Please enter valid weight and height values.")

    else:
        height_cm = height_m * 100
        ml_category, confidence = predict_bmi_category(height_cm, weight_kg)
        foods = recommend_food(ml_category)

        st.subheader("Your BMI Results")
        st.metric("BMI value", f"{bmi:.2f}")

        st.write(f"Predicted Category: **{ml_category}** (Confidence: {confidence}%)")

        if ml_category == "Underweight":
            st.info(ml_category)
        elif ml_category == "Normal weight":
            st.success(ml_category)
        elif ml_category == "Overweight":
            st.warning(ml_category)
        else:
            st.error(ml_category)

        st.subheader("Food Recommendations")
        for food in foods:
            st.write(f"- {food}")

        st.caption("Note that: This BMI calculator provides an estimate and should not replace professional medical advice.")