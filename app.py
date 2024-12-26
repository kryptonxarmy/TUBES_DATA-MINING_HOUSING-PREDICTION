import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

# Streamlit App
st.title('California Housing Price Prediction')

st.write("""
## Input Features
""")

longitude = st.number_input('Longitude', value=-122.23)
latitude = st.number_input('Latitude', value=37.88)
housing_median_age = st.number_input('Housing Median Age', value=41)
total_rooms = st.number_input('Total Rooms', value=880)
total_bedrooms = st.number_input('Total Bedrooms', value=129)
population = st.number_input('Population', value=322)
households = st.number_input('Households', value=126)
median_income = st.number_input('Median Income', value=8.3252)

input_data = np.array([[longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income]])

prediction = model.predict(input_data)

st.write(f'## Predicted Median House Value: ${prediction[0]:,.2f}')