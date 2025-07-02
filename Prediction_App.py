import streamlit as st
import pickle 
import numpy as np
import pandas as pd
from PIL import Image

# Load the trained model
try:
    with open("final_model_bagg.pkl","rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Prediction function
def predict_churn(input_data):
    try:
        pred = model.predict_proba(input_data)[:, 1][0]
        if pred > 0.5:
            return f"This customer is more likely to churn: Probability = {round(pred * 100, 2)}%"
        else:
            return f"This customer is less likely to churn: Probability = {round(pred * 100, 2)}%"
    except Exception as e:
        return f"Error during prediction: {e}"

# Main app
def main():
    st.title("Telecom Customer Churn Prediction")

    # Display telecom-related image (Optional)
    image = Image.open("telecom_image.jpg")  # Ensure this image exists in the working directory
    st.image(image, use_container_width=True)

    # User inputs
    gender = {'Male': 1, 'Female': 0}[st.radio("Select Gender", ['Male', 'Female'])]
    SeniorCitizen = st.radio("Senior Citizen", [0, 1])
    Partner = {'Yes': 1, 'No': 0}[st.radio("Has a Partner?", ['Yes', 'No'])]
    Dependents = {'Yes': 1, 'No': 0}[st.radio("Has Dependents?", ['Yes', 'No'])]
    tenure = st.number_input("Enter Tenure (Months)", min_value=0)
    PhoneService = {'Yes': 1, 'No': 0}[st.radio("Has Phone Service?", ['Yes', 'No'])]
    MultipleLines = {'No': 0, 'No phone service': 1, 'Yes': 2}[st.radio("Multiple Lines?", ['No', 'No phone service', 'Yes'])]
    InternetService = {'No': 0, 'DSL': 1, 'Fiber optic': 2}[st.radio("Internet Service Type", ['No', 'DSL', 'Fiber optic'])]
    OnlineSecurity = {'No': 0, 'No internet service': 1, 'Yes': 2}[st.radio("Online Security?", ['No', 'No internet service', 'Yes'])]
    OnlineBackup = {'No': 0, 'No internet service': 1, 'Yes': 2}[st.radio("Online Backup?", ['No', 'No internet service', 'Yes'])]
    DeviceProtection = {'No': 0, 'No internet service': 1, 'Yes': 2}[st.radio("Device Protection?", ['No', 'No internet service', 'Yes'])]
    TechSupport = {'No': 0, 'No internet service': 1, 'Yes': 2}[st.radio("Tech Support?", ['No', 'No internet service', 'Yes'])]
    StreamingTV = {'No': 0, 'No internet service': 1, 'Yes': 2}[st.radio("Streaming TV?", ['No', 'No internet service', 'Yes'])]
    StreamingMovies = {'No': 0, 'No internet service': 1, 'Yes': 2}[st.radio("Streaming Movies?", ['No', 'No internet service', 'Yes'])]
    Contract = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}[st.radio("Contract Type", ['Month-to-month', 'One year', 'Two year'])]
    PaperlessBilling = {'Yes': 1, 'No': 0}[st.radio("Uses Paperless Billing?", ['Yes', 'No'])]
    PaymentMethod = st.number_input("Enter Payment Method (Encoded as numeric)", min_value=0)
    MonthlyCharges = st.number_input("Enter Monthly Charges")
    TotalCharges = st.number_input("Enter Total Charges")

    # Preparing input data for prediction
    input_data = [[gender, SeniorCitizen, Partner, Dependents, tenure,
                   PhoneService, MultipleLines, InternetService,
                   OnlineSecurity, OnlineBackup, DeviceProtection,
                   TechSupport, StreamingTV, StreamingMovies, Contract,
                   PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges]]

    # Predict and display the result
    if st.button("Predict"):
        response = predict_churn(input_data)
        st.success(response)

if __name__ == '__main__':
    main()
