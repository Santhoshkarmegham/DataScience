import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter property details to estimate its price in GBP.")

model_path = Path("house_price_model.pkl")

if not model_path.exists():
    st.error(
        "Model file not found. Run all cells in "
        "`house_price_prediction.ipynb` first to create "
        "`house_price_model.pkl`."
    )
    st.stop()

model = joblib.load(model_path)

location = st.selectbox(
    "Location",
    [
        "London",
        "Manchester",
        "Birmingham",
        "Leeds",
        "Liverpool",
        "Bristol",
        "Glasgow",
        "Edinburgh"
    ]
)

property_type = st.selectbox(
    "Property type",
    ["Apartment", "Terraced", "Semi-Detached", "Detached"]
)

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=6, value=2)
area_sqft = st.number_input(
    "Area in square feet",
    min_value=300,
    max_value=10000,
    value=1400
)
age_years = st.number_input(
    "Property age in years",
    min_value=0,
    max_value=200,
    value=10
)
distance_city_centre_km = st.number_input(
    "Distance from city centre in km",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1
)
has_garden = st.selectbox("Has garden?", ["Yes", "No"])
has_garage = st.selectbox("Has garage?", ["Yes", "No"])
nearby_school_rating = st.slider(
    "Nearby school rating",
    min_value=1.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)
crime_rate_index = st.slider(
    "Crime rate index",
    min_value=0.0,
    max_value=100.0,
    value=25.0,
    step=0.1
)

if st.button("Predict Price", type="primary"):
    input_data = pd.DataFrame({
        "location": [location],
        "property_type": [property_type],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "area_sqft": [area_sqft],
        "age_years": [age_years],
        "distance_city_centre_km": [distance_city_centre_km],
        "has_garden": [1 if has_garden == "Yes" else 0],
        "has_garage": [1 if has_garage == "Yes" else 0],
        "nearby_school_rating": [nearby_school_rating],
        "crime_rate_index": [crime_rate_index]
    })

    prediction = model.predict(input_data)[0]
    st.success(f"Estimated property price: £{prediction:,.2f}")
