# 🔮 Telecom Customer Churn Prediction

# 🔮 Customer Churn Prediction App

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-ff4b4b?logo=streamlit&logoColor=white)](https://rishabhyadav1202-customer-churn-prediction-app-oa1ke2.streamlit.app)

A machine learning web app to predict telecom customer churn and explain predictions using SHAP.


A machine learning project to predict customer churn using Logistic Regression, XGBoost, Random Forest, SMOTE, and SHAP for interpretability. Deployed using Streamlit.

## 🔑 Key Highlights

- Achieved **73.5% to 77.9% accuracy** across all models.
- **Logistic Regression** delivered the best **recall (78.8%)** and **F1-score (0.646)**.
- Applied **SMOTE** to address class imbalance, improving minority class detection.
- Used **SHAP** to explain churn predictions — key drivers: `Contract`, `Tenure`, `MonthlyCharges`.
- Performed **5-Fold Cross-Validation** with a **mean score of 80.1%**, showing strong generalization.

## 📦 Tech Stack
- Python, Pandas, Scikit-learn, XGBoost
- SMOTE (imbalanced-learn), SHAP
- Streamlit for app deployment
