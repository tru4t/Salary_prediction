# -*- coding: utf-8 -*-
import numpy as np
import joblib
import streamlit as st
import pandas as pd

model=joblib.load("Salary_prediction_model.pkl")
encoder=joblib.load("label_encoder_sp.pkl")

st.title("Salary Prediction App")

Age	= st.number_input("Age",)
Gender = st.selectbox("Gender",encoder['Gender'].classes_)
Education_Level	= st.selectbox("Education_Level",encoder['Education Level'].classes_)
Job_Title	= st.selectbox("Job_Title",encoder['Job Title'].classes_)
Years_of_Experience = st.number_input("Years_of_Experience",0.0,40.0,2.0)

df = pd.DataFrame({
    "Age": [Age],
    "Gender": [Gender],
    "Education_Level": [Education_Level],
    "Job_Title": [Job_Title],
    "Years_of_Experience": [Years_of_Experience]
})

if st.button("Predict Salary"):
    for col in encoder:
        df[col] = encoder[col].transform(df[col])

    prediction = model.predict(df)
    st.success(f"Predicted Salary: {prediction[0]:,.2f}")
    st.success(f"Result: {result[0]}")
