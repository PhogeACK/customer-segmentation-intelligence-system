import streamlit as st


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Segmentation Intelligence System",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("📊 Customer Segmentation Intelligence System")

st.markdown(
    """
An end-to-end Machine Learning application that transforms customer data into
actionable business intelligence using behavioral segmentation,
persona generation, marketing recommendations, and workflow automation.

This dashboard represents **Version 2** of the project, extending the original
FastAPI prediction service with an interactive business interface.
"""
)

st.divider()

# --------------------------------------------------
# System Overview
# --------------------------------------------------
st.header("System Overview")

st.markdown("""
The application processes customer records through a complete machine learning pipeline:

1. Data preprocessing
2. Feature engineering
3. Feature transformation & scaling
4. K-Means customer segmentation
5. Persona generation
6. Business recommendation generation
7. Workflow recommendation generation
""")

st.divider()

# --------------------------------------------------
# Current Capabilities
# --------------------------------------------------
st.header("Current Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Completed")
    st.success("Customer Segmentation")
    st.success("Business Personas")
    st.success("Marketing Recommendations")
    st.success("Workflow Recommendations")
    st.success("FastAPI Prediction Service")

with col2:
    st.subheader("Coming Next")
    st.info("Single Customer Prediction")
    st.info("Batch CSV Upload")
    st.info("Interactive Analytics Dashboard")
    st.info("Cluster Visualizations")
    st.info("Download Prediction Results")

st.divider()

# --------------------------------------------------
# Architecture
# --------------------------------------------------
st.header("Prediction Pipeline")

st.markdown("""
```text
Customer Data
      │
      ▼
Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Transformation & Scaling
      │
      ▼
K-Means Segmentation
      │
      ▼
Business Intelligence Layer
      ├── Persona Engine
      ├── Recommendation Engine
      └── Workflow Engine
      │
      ▼
Business Output