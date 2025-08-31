import streamlit as st
import numpy as np
import joblib

# Load your trained model
model = joblib.load("insurance_Model.pkl")

# Streamlit app
st.set_page_config(page_title="Insurance Cost Predictor", page_icon="💰", layout="centered")

st.title("💰 Insurance Cost Prediction App")
st.write("Enter your details below to predict your estimated insurance cost.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)
sex = st.selectbox("Sex", ("Male", "Female"))
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ("Yes", "No"))
region = st.selectbox("Region", ("northeast", "northwest", "southeast", "southwest"))

# Convert inputs to numeric
sex_num = 1 if sex == "Male" else 0
smoker_num = 1 if smoker == "Yes" else 0
region_dict = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region_num = region_dict[region]

# Prepare input for model
input_data = np.array([[age, sex_num, bmi, children, smoker_num, region_num]])

# Predict
if st.button("🔮 Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"💵 Estimated Insurance Cost: **${prediction[0]:.2f} USD/Year**")
st.ballons()
