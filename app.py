import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
import joblib
import os
import joblib



st.title("🏥 Hospital Management -Predict Disease")

# Upload data
data = pd.read_csv("hospital_data.csv")
st.sidebar.header("Filters")
dept = st.sidebar.selectbox("Select Department", data["Department"].unique())

filtered = data[data["Department"] == dept]

st.metric("Total Patients", len(filtered))
st.metric("Total Revenue", f"${filtered['Billing'].sum():,.0f}")

# Charts
fig = px.histogram(filtered, x="Age", title="Age Distribution")
st.plotly_chart(fig)

# ML Prediction Panel
st.subheader("🔮 Predict Readmission")
age = st.slider("Age", 0, 100, 50)
admissions = st.number_input("Previous Admissions", 0, 10, 1)
bill = st.number_input("Treatment Cost", 0, 50000, 10000)

if os.path.exists("readmission_model.pkl"):
    model = joblib.load("readmission_model.pkl")
else:
    print("Model file not found.")
    # Optionally, raise an error or fallback logic


if st.button("Predict"):
    model = joblib.load("readmission_model.pkl")  # previously saved
    print("Expected number of features:", model.n_features_in_)
    # Example if model expects 5 features:
    pred = model.predict([[age, bill, admissions, gender, glucose_level]])
    input_df = pd.DataFrame([{
    "age": age,
    "bill": bill,
    "admissions": admissions,
    "gender": gender,
    "glucose_level": glucose_level
}])

pred = model.predict(input_df)
model.feature_names = ["age", "bill", "admissions", "gender", "glucose_level"]
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print(model.feature_names)


pred = model.predict([[age, bill, admissions]])
st.success(f"Prediction: {'Readmitted' if pred[0]==1 else 'Not Readmitted'}")
