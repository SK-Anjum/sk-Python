import streamlit as st

# App setup
st.set_page_config(page_title="BMI Calculator", page_icon="💪")
st.title("💪 BMI Calculator")
st.write("Enter your height and weight to calculate your Body Mass Index (BMI).")

# Input fields
input_height_cm = st.number_input("Height (in centimeters):", min_value=30.0, format="%.1f")
input_weight_kg = st.number_input("Weight (in kilograms):", min_value=1.0, format="%.2f")

# BMI Calculation
if st.button("Calculate BMI"):
    if input_height_cm > 0 and input_weight_kg > 0:
        height_in_meters = input_height_cm / 100  # Convert cm to meters
        calculated_bmi = input_weight_kg / (height_in_meters ** 2)
        st.success(f"Your BMI is: {calculated_bmi:.2f}")

        # BMI Category
        if calculated_bmi < 18.5:
            st.warning("You're underweight. ")
        elif 18.5 <= calculated_bmi < 24.9:
            st.success("You have a normal weight. ")
        elif 25 <= calculated_bmi < 29.9:
            st.info("You're overweight. ")
        else:
            st.error("You're obese. ⚠️ Consider consulting a health expert.")
    else:
        st.error("Please enter valid height and weight.")
