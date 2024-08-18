import streamlit as st
import hopsworks
import joblib
import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
hopsworks_key = os.getenv("HOPSWORKS_KEY")
# hopsworks_key = hopsworks_key.strip()

def load_model():
    project = hopsworks.login(api_key_value=hopsworks_key)
    mr = project.get_model_registry()
    model = mr.get_model(name="diabetes_prediction_model")
    model_dir = model.download()
    model_path = os.path.join(model_dir, 'diab_pred_model.pkl')
    model = joblib.load(model_path)
    return model

# Load the model
model = load_model()

# Singular prediction function
def predict_diabetes_single(age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level):
    input_data = [[age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level]]
    prediction = model.predict(input_data)[0]
    return "Diabetic" if prediction == 1 else "Not Diabetic"

# Batch prediction function
def predict_diabetes_batch(features_df):
    features_df= features_df[["patient_id","age", "hypertension", "heart_disease", "bmi", "HbA1c_level", "blood_glucose_level"]]
    primary_key_df = features_df[["patient_id"]]
    data = features_df.drop(["patient_id"], axis=1)
    predictions = model.predict(data.sample(100))
    predictions = ["Diabetic" if pred == 1 else "Not Diabetic" for pred in predictions]
    prediction_df = primary_key_df.copy()
    prediction_df["prediction"] = predictions
    return prediction_df

# Streamlit Interface
st.title("DiabPred")

tab1, tab2 = st.tabs(["Single Prediction", "Batch Prediction"])

with tab1:
    st.header("Enter individual patient data:")
    
    age = st.number_input("Age", value=30)
    hypertension = st.radio("Hypertension (0: No, 1: Yes)", [0, 1], index=0)
    heart_disease = st.radio("Heart Disease (0: No, 1: Yes)", [0, 1], index=0)
    bmi = st.number_input("BMI", value=25.0)
    hba1c_level = st.number_input("HbA1c Level", value=5.5)
    blood_glucose_level = st.number_input("Blood Glucose Level", value=100)
    
    if st.button("Predict"):
        prediction = predict_diabetes_single(age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level)
        st.write("Prediction:", prediction)

with tab2:
    st.header("Upload patient data for batch prediction:")
    
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        features_df = pd.read_csv(uploaded_file)
        predictions_df = predict_diabetes_batch(features_df)
        st.write("Predictions:")
        st.dataframe(predictions_df)
