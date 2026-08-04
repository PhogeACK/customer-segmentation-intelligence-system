# Customer Segmentation Intelligence System

> **An end-to-end Machine Learning & Business Intelligence application that transforms raw customer marketing data into actionable business recommendations through behavioral customer segmentation.**

---

# Overview

The **Customer Segmentation Intelligence System** demonstrates how an unsupervised Machine Learning model can be integrated into a complete business application.

Instead of only assigning customers to clusters, the system converts analytical results into practical business intelligence by automatically generating:

- Customer Personas
- Marketing Campaign Recommendations
- CRM Workflow Suggestions
- Executive Business Insights
- Interactive Analytics Dashboard

The project combines the full machine learning lifecycle—from raw customer data to executive decision support—inside a production-style Streamlit application.

---

# Business Problem

Marketing teams often manage thousands of customers without a clear understanding of behavioral differences.

Traditional clustering projects stop after assigning customers to clusters.

This project extends clustering into a complete decision-support system by translating model predictions into business actions that marketing and CRM teams can immediately use.

---

# Application Features

## Single Customer Prediction

Predict an individual customer's segment and instantly receive:

- Customer Segment
- Business Persona
- Marketing Campaign Recommendation
- CRM Workflow Recommendation
- Business Objective
- Opportunity & Risk Assessment

---

## Batch Customer Prediction

Upload an entire customer dataset to:

- Predict customer segments
- Generate business intelligence for every customer
- Export enriched prediction results
- Prepare datasets for business analysis

---

## Analytics Dashboard

Explore prediction results through interactive visualizations including:

- Executive Overview
- Customer Distribution
- Segment Value Analysis
- Customer Personas
- Executive Key Insights

---

# Machine Learning Pipeline

```text
Raw Customer Data
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Categorical Encoding
        │
        ▼
Feature Scaling
        │
        ▼
K-Means Clustering
        │
        ▼
Business Intelligence Engine
        │
        ▼
Interactive Analytics Dashboard
```

---

# Application Architecture

```text
                    Customer Dataset
                           │
                           ▼
                    load_data.py
                           │
                           ▼
                   preprocess.py
                           │
                           ▼
              feature_engineering.py
                           │
                           ▼
                    encoding.py
                           │
                           ▼
                   transform.py
                           │
                           ▼
                     train.py
                           │
                           ▼
                   clustering.py
                           │
                           ▼
                     predict.py
                           │
                           ▼
             business_intelligence.py
                   ├──────────────┐
                   ▼              ▼
         persona_engine.py   recommendation_engine.py
                   │              │
                   └──────┬───────┘
                          ▼
                workflow_engine.py
                          │
                          ▼
                Streamlit Application
```

---

# Project Structure

```text
Customer-Segmentation-Intelligence-System/
│
├── pages/
│   ├── Home.py
│   ├── Single_Prediction.py
│   ├── Batch_Prediction.py
│   ├── Analytics_Dashboard.py
│   └── About.py
│
├── src/
    │
    ├── app.py                      # FastAPI application entry point
    ├── batch_predict.py            # Batch prediction pipeline for customer datasets
    ├── business_intelligence.py    # Combines personas, campaigns, and workflows into business insights
    ├── clustering.py               # K-Means model training and cluster prediction
    ├── config.py                   # Global configuration and project file paths
    ├── encoding.py                 # Categorical feature encoding
    ├── feature_engineering.py      # Feature engineering and business feature creation
    ├── load_data.py                # Dataset loading utilities
    ├── persona_engine.py           # Customer persona generation
    ├── predict.py                  # Single customer prediction pipeline
    ├── preprocess.py               # Data cleaning and preprocessing
    ├── recommendation_engine.py    # Marketing campaign recommendation engine
    ├── save_artifacts.py           # Save trained models and preprocessing artifacts
    ├── test_prediction.py          # Local prediction testing script
    ├── train.py                    # End-to-end model training pipeline
    ├── transform.py                # Feature scaling and data transformations
    ├── workflow_engine.py          # CRM workflow recommendation engine
    │
├── models/
├── notebooks/
├── data/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Clustering Model | K-Means |
| Model Serialization | Joblib |
| Frontend | Streamlit |
| Backend API | FastAPI |
| Visualization | Streamlit Native Charts |
| Development Environment | Jupyter Notebook |

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

(Optional) Run the FastAPI service

```bash
uvicorn api.main:app --reload
```

---
### Demo Dataset

A sample dataset is provided in:

```text
data/sample_batch.csv
```

Upload this file through the **Batch Prediction** page to explore the complete prediction workflow and analytics dashboard.
---

# Future Improvements

Potential enhancements include:

- Real CRM integration
- Alternative clustering algorithms
- Automatic cluster monitoring
- Campaign performance tracking
- Explainable AI visualizations
- Authentication and role-based access
- Cloud deployment

---

# Author

**Almog Cohen**

Data Scientist

Machine Learning • Customer Analytics • Business Intelligence

This project was developed as a portfolio application demonstrating the complete lifecycle of an end-to-end machine learning solution—from raw customer data to executive business insights.