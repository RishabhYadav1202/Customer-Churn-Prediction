import streamlit as st
import pickle
import numpy as np

# ------------------------
# Load model and encoders
import joblib

model = joblib.load("customer_churn_model.pkl")
encoders = joblib.load("encoders.pkl")

feature_names = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
]
# ------------------------
# Safe encoder
def safe_encode(column_name, value):
    try:
        encoder = encoders[column_name]
        clean_value = str(value).strip()
        encoded_value = encoder.transform([clean_value])[0]
        return encoded_value
    except Exception as e:
        st.error(f"Encoding error for '{column_name}' with value '{value}': {e}")
        st.stop()

# ------------------------
# Streamlit Setup
st.set_page_config(page_title="Customer Churn Predictor", page_icon="🔮", layout="centered")

st.title("🔮 Customer Churn Prediction")
st.markdown("Predict whether a telecom customer is likely to churn based on their service profile and usage patterns.")
st.markdown("---")

# ------------------------
# Sidebar Inputs
st.sidebar.header("🧾 Customer Details")

categorical_features = {
    'gender': ['Female', 'Male'],
    'Partner': ['No', 'Yes'],
    'Dependents': ['No', 'Yes'],
    'PhoneService': ['No', 'Yes'],
    'MultipleLines': ['No', 'Yes', 'No phone service'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['No', 'Yes', 'No internet service'],
    'OnlineBackup': ['No', 'Yes', 'No internet service'],
    'DeviceProtection': ['No', 'Yes', 'No internet service'],
    'TechSupport': ['No', 'Yes', 'No internet service'],
    'StreamingTV': ['No', 'Yes', 'No internet service'],
    'StreamingMovies': ['No', 'Yes', 'No internet service'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaperlessBilling': ['No', 'Yes'],
    'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
}

numeric_features = {
    'SeniorCitizen': (0, 1),
    'tenure': (0, 72),
    'MonthlyCharges': (0.0, 120.0),
    'TotalCharges': (0.0, 9000.0),
    'TotalServices': (0, 6)
}

with st.sidebar.form("input_form"):
    user_inputs = []

    with st.expander("📋 Basic Details", expanded=True):
        for feature in ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure']:
            if feature in categorical_features:
                value = st.selectbox(feature, categorical_features[feature])
            else:
                min_val, max_val = numeric_features[feature]
                value = st.slider(feature, min_val, max_val)
            user_inputs.append(value)

    with st.expander("🌐 Internet & Add-ons"):
        for feature in ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
                        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']:
            value = st.selectbox(feature, categorical_features[feature])
            user_inputs.append(value)

    with st.expander("💳 Billing & Payments"):
        for feature in ['Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'TotalServices']:
            if feature in categorical_features:
                value = st.selectbox(feature, categorical_features[feature])
            else:
                min_val, max_val = numeric_features[feature]
                step = 0.1 if isinstance(min_val, float) else 1
                value = st.slider(feature, min_val, max_val, step=step)
            user_inputs.append(value)

    submitted = st.form_submit_button("🔍 Predict Churn")

# ------------------------
# Prediction and Output
if submitted:
    final_input = []
    for feature, value in zip(feature_names, user_inputs):
        if feature in encoders:
            final_input.append(safe_encode(feature, value))
        else:
            final_input.append(value)

    final_input = np.array([final_input])
    prediction = model.predict(final_input)[0]
    probability = model.predict_proba(final_input)[0]

    st.markdown("---")
    st.subheader("🎯 Prediction Result")

    col1, col2 = st.columns(2)
    col1.metric(label="🔵 Stay Probability", value=f"{probability[0]*100:.2f}%")
    col2.metric(label="🔴 Churn Probability", value=f"{probability[1]*100:.2f}%")

    if prediction == 1:
        st.error("⚠️ The customer is **likely to churn**.")
        st.markdown("""
        **Suggested Actions:**
        - Offer loyalty discounts or upgrade plans
        - Improve technical support experience
        - Engage through personalized communication
        """)
    else:
        st.success("✅ The customer is **likely to stay**.")
        st.markdown("""
        **Suggested Actions:**
        - Continue engagement through value-based messaging
        - Recommend cross-sell or upsell options
        """)
