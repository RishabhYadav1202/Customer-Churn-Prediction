# 🔮 Telecom Customer Churn Prediction

# 🔮 Customer Churn Prediction App

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-ff4b4b?logo=streamlit&logoColor=white)](https://rishabhyadav1202-customer-churn-prediction-app-oa1ke2.streamlit.app)

A machine learning web app to predict telecom customer churn and explain predictions using SHAP.


## 📌 Problem Statement

The goal is to identify customers who are most likely to churn so that proactive retention strategies can be applied. Business losses due to churn are high — and early detection enables cost-effective intervention.

---

## 🧠 Solution Overview

- Performed detailed **EDA** to uncover patterns
- Preprocessed data (label encoding, null handling, feature fixing)
- Handled class imbalance using **SMOTE**
- Built and evaluated **4 ML models**:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - XGBoost
- Tuned models using **GridSearchCV**
- Compared models using Accuracy, Precision, Recall, F1-Score
- Used **SHAP** to explain churn predictions
- Deployed best model via **Streamlit**

---

## 🧪 Model Comparison

| Model                | Accuracy | Precision | Recall | F1 Score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | 0.771    | 0.55      | 0.79   | 0.65     |
| XGBoost             | 0.770    | 0.55      | 0.73   | 0.63     |
| Random Forest       | 0.779    | 0.58      | 0.58   | 0.58     |
| Decision Tree       | 0.735    | 0.50      | 0.66   | 0.57     |
| ✅ **Voting Ensemble** | ✅ **0.796** | ✅ **0.59** | ✅ **0.72** | ✅ **0.65** |

---

## 🧠 SHAP Explainability

SHAP was used to interpret model predictions.  
**Top Features Influencing Churn:**
- 📜 **Contract Type** (Month-to-month increases churn)
- 🕒 **Tenure** (Shorter tenure = higher churn)
- 💵 **Total Charges** (Lower charges = high churn)
- 🔐 **Tech Support & Online Security** (help reduce churn)

![SHAP Beeswarm](![image](https://github.com/user-attachments/assets/09ed7af8-dc5a-470a-8e2c-17a55272d606))

---

## 💼 Business Insights

- New users with month-to-month contracts are at **highest churn risk**
- Customers without tech support or security addons are more likely to leave
- These insights can be used for targeted retention strategies like offers, upgrades, and outreach

---

## 🚀 Tech Stack

- **Languages & Libraries**: Python, Pandas, NumPy, scikit-learn, XGBoost, imbalanced-learn, SHAP
- **Visualization**: Matplotlib, Seaborn
- **Deployment**: Streamlit
- **Model Storage**: Pickle

---

## 🔧 How to Run Locally

1. Clone this repo:
```bash
git clone https://github.com/RishabhYadav1202/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
