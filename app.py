
import streamlit as st
import pandas as pd
import joblib

# ==========================
# Load Model
# ==========================
model = joblib.load("linear_regression_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Fill the house details and click Predict.")

# ==========================
# Input Fields
# ==========================

bedrooms = st.number_input("Bedrooms", 1, 10, 3)

bathrooms = st.number_input("Bathrooms", 1.0, 10.0, 2.0, step=0.5)

sqft_living = st.number_input("Living Area (sqft)", 500, 10000, 1800)

sqft_lot = st.number_input("Lot Area (sqft)", 500, 100000, 5000)

floors = st.selectbox("Floors", [1, 1.5, 2, 2.5, 3])

waterfront = st.selectbox("Waterfront", [0, 1])

view = st.slider("View", 0, 4, 0)

condition = st.slider("Condition", 1, 5, 3)

sqft_above = st.number_input("Sqft Above", 500, 10000, 1500)

sqft_basement = st.number_input("Sqft Basement", 0, 5000, 300)

yr_built = st.number_input("Year Built", 1900, 2025, 2000)

yr_renovated = st.number_input("Year Renovated (0 if never)", 0, 2025, 0)

month = st.selectbox("Sale Month", list(range(1, 13)))

day = st.slider("Sale Day", 1, 31, 15)

house_age = st.slider("House Age", 0, 150, 20)

renovated = st.selectbox("Renovated", [0, 1])

# ==========================
# City Dropdown
# ==========================

cities = sorted([
    c.replace("city_", "")
    for c in columns
    if c.startswith("city_")
])

city = st.selectbox("City", cities)

# ==========================
# ZIP Dropdown
# ==========================

zips = sorted([
    z.replace("statezip_", "")
    for z in columns
    if z.startswith("statezip_")
])

zipcode = st.selectbox("State ZIP", zips)

# ==========================
# Prediction
# ==========================

if st.button("Predict Price"):

    # Create dataframe with all columns = 0
    input_df = pd.DataFrame(0, index=[0], columns=columns)

    # Numerical values
    input_df["bedrooms"] = bedrooms
    input_df["bathrooms"] = bathrooms
    input_df["sqft_living"] = sqft_living
    input_df["sqft_lot"] = sqft_lot
    input_df["floors"] = floors
    input_df["waterfront"] = waterfront
    input_df["view"] = view
    input_df["condition"] = condition
    input_df["sqft_above"] = sqft_above
    input_df["sqft_basement"] = sqft_basement
    input_df["yr_built"] = yr_built
    input_df["yr_renovated"] = yr_renovated
    input_df["month"] = month
    input_df["day"] = day
    input_df["house_age"] = house_age
    input_df["renovated"] = renovated

    # One-hot encoding for city
    city_col = "city_" + city
    if city_col in input_df.columns:
        input_df[city_col] = 1

    # One-hot encoding for ZIP
    zip_col = "statezip_" + zipcode
    if zip_col in input_df.columns:
        input_df[zip_col] = 1

    # Scale
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]khewiugfcewhjke;odjewkckewjlwjfirwclkw

    st.success(f"🏠 Estimated House Price: ${prediction:,.2f}")