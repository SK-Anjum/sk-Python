import streamlit as st


st.set_page_config(page_title="Universal Unit Converter", layout="centered")

#title
st.title("Universal Unit Converter")
st.markdown("###### Effortlessly convert units of Length, Weight, or Temperature.")

st.divider()

# Select conversion category
category = st.selectbox("Pick a category:", ["Length", "Temperature", "Weight"])

# LENGTH CONVERSION
if category == "Length":
    st.subheader("Length Conversion")

    length_units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Inches": 0.0254,
        "Feet": 0.3048,
        "Yards": 0.9144,
        "Miles": 1609.34
    }

    with st.expander("Choose units and enter a value"):
        input_unit = st.selectbox("Convert from:", list(length_units.keys()))
        output_unit = st.selectbox("Convert to:", list(length_units.keys()))
        user_value = st.number_input("Enter length value:", min_value=0.0, step=0.1)

    if st.button("Convert"):
        result = user_value * length_units[input_unit] / length_units[output_unit]
        st.success(f"{user_value} {input_unit} = {result:.2f} {output_unit}")
        st.caption(f"Formula: {user_value} × ({length_units[input_unit]} / {length_units[output_unit]})")

# WEIGHT
elif category == "Weight":
    st.subheader("Weight Conversion")

    weight_units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    with st.expander("Choose units and enter a value"):
        input_unit = st.selectbox("Convert from:", list(weight_units.keys()))
        output_unit = st.selectbox("Convert to:", list(weight_units.keys()))
        user_value = st.number_input("Enter weight value:", min_value=0.0, step=0.1)

    if st.button("Convert"):
        result = user_value * weight_units[input_unit] / weight_units[output_unit]
        st.success(f"{user_value} {input_unit} = {result:.2f} {output_unit}")
        st.caption(f"Formula: {user_value} × ({weight_units[input_unit]} / {weight_units[output_unit]})")

# TEMPERATURE
elif category == "Temperature":
    st.subheader("Temperature Conversion")

    with st.expander("Choose units and enter a value"):
        input_unit = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
        output_unit = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])
        user_value = st.number_input("Enter temperature:", step=0.1)

    def temp_convert(v, src, tgt):
        if src == tgt:
            return v
        if src == "Celsius":
            return v + 273.15 if tgt == "Kelvin" else v * 9 / 5 + 32
        if src == "Fahrenheit":
            return (v - 32) * 5 / 9 if tgt == "Celsius" else (v - 32) * 5 / 9 + 273.15
        if src == "Kelvin":
            return v - 273.15 if tgt == "Celsius" else (v - 273.15) * 9 / 5 + 32

    if st.button("Convert"):
        result = temp_convert(user_value, input_unit, output_unit)
        st.success(f"{user_value} {input_unit} = {result:.2f} {output_unit}")

        #formula
        if input_unit == output_unit:
            st.caption("Formula: No conversion needed.")
        elif input_unit == "Celsius" and output_unit == "Fahrenheit":
            st.caption("Formula: (°C × 9/5) + 32")
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            st.caption("Formula: (°F - 32) × 5/9")
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            st.caption("Formula: °C + 273.15")
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            st.caption("Formula: K - 273.15")
        elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
            st.caption("Formula: ((°F - 32) × 5/9) + 273.15")
        elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
            st.caption("Formula: ((K - 273.15) × 9/5) + 32")
