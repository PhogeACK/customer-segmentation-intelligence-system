import streamlit as st

st.title("ℹ️ About")

st.markdown(
    """
## Customer Segmentation Intelligence System

The Customer Segmentation Intelligence System is an end-to-end Machine Learning application that demonstrates how customer segmentation can be transformed into practical business intelligence.

The project combines data preprocessing, feature engineering, clustering, business logic, API development, and interactive dashboards into one complete analytical solution.

Its purpose is to demonstrate how Machine Learning models can move beyond prediction and become decision-support tools for marketing and customer relationship management.

---

# 🧠 Machine Learning Pipeline

The prediction pipeline follows the complete machine learning workflow:

Raw Customer Data
↓
Data Preprocessing
↓
Feature Engineering
↓
Categorical Encoding
↓
Feature Scaling
↓
K-Means Clustering Model
↓
Business Intelligence Engine
↓
Interactive Analytics Dashboard

Each stage was implemented as a modular component to improve readability, maintainability, and scalability.

---

# 🛠 Technology Stack

Programming Languages:
- Python

Data Science:
- Pandas
- NumPy
- Scikit-learn

Model Persistence:
- Joblib

Backend:
- FastAPI

Frontend:
- Streamlit

Visualization:
- Plotly

---

# 📦 Project Architecture

src/
│
├── preprocess.py
├── feature_engineering.py
├── encoding.py
├── transform.py
├── train.py
├── predict.py
├── business_intelligence.py
│
pages/
│
├── Home
├── Single Prediction
├── Batch Prediction
├── Analytics Dashboard
├── About

The project follows a modular architecture where each component is responsible for one stage of the machine learning pipeline.

---

# ✨ Core Features

- Individual Customer Prediction
- Batch Customer Prediction
- Customer Persona Generation
- Marketing Campaign Recommendation Engine
- Workflow Recommendation Engine
- Executive Analytics Dashboard
- Automated Business Intelligence Generation

---

# 🔮 Future Improvements

Potential future enhancements include:

- Real CRM integration
- Additional clustering algorithms
- Automatic cluster performance monitoring
- Campaign effectiveness tracking
- Explainable AI visualizations
- Cloud deployment with authentication and user management

---

# 👨‍💻 Author

Almog Cohen

Data Scientist

Specializing in Machine Learning, Customer Analytics, Predictive Modeling, and Business Intelligence.

This project was developed as a portfolio application demonstrating the complete lifecycle of an end-to-end data science solution—from raw customer data to executive business insights.
"""
)


