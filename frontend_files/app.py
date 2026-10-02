
import streamlit as st
import requests
import pandas as pd

st.title("SuperKart Sales Prediction")

st.write("Enter the product and store information to predict sales.")

backend_url = st.text_input(
    "Backend URL",
    "http://host.docker.internal:7860"
)

st.subheader("Product Information")

product_weight = st.number_input("Product Weight", value=12.66)
product_sugar = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar", "Ultra Low"]
)
product_area = st.number_input(
    "Product Allocated Area",
    value=0.027
)
product_mrp = st.number_input("Product MRP", value=117.08)

product_id_char = st.text_input("Product ID Character", "FD")

product_category = st.selectbox(
    "Product Type Category",
    ["Perishables", "Non Perishables"]
)

st.subheader("Store Information")

store_size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

city_type = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    [
        "Departmental Store",
        "Food Mart",
        "Supermarket Type1",
        "Supermarket Type2",
        "Supermarket Type3"
    ]
)

store_age = st.number_input(
    "Store Age (Years)",
    value=16
)

if st.button("Predict Sales"):

    input_data = {
        "Product_Weight": product_weight,
        "Product_Sugar_Content": product_sugar,
        "Product_Allocated_Area": product_area,
        "Product_MRP": product_mrp,
        "Store_Size": store_size,
        "Store_Location_City_Type": city_type,
        "Store_Type": store_type,
        "Product_Id_char": product_id_char,
        "Store_Age_Years": store_age,
        "Product_Type_Category": product_category
    }

    try:
        response = requests.post(
            backend_url + "/v1/predict",
            json=input_data
        )

        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(
                f"Predicted Sales: {prediction:.2f}"
            )
        else:
            st.error("Prediction failed.")

    except Exception as e:
        st.error(f"Could not connect to backend: {e}")
