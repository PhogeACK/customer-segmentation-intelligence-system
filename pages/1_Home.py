import streamlit as st

st.title("🏠 Customer Segmentation Intelligence System")

st.write(
    """
Welcome to the Customer Segmentation Intelligence System.

This application transforms raw customer data into actionable business intelligence using
machine learning-based customer segmentation.

Use the navigation menu on the left to explore the available features.
"""
)

st.divider()

st.subheader("Available Modules")

st.markdown("""
- 👤 **Single Prediction** — Predict a customer segment for an individual customer.

- 📁 **Batch Prediction** — Upload a CSV file and enrich an entire customer dataset.

- 📈 **Analytics Dashboard** — Explore segmentation results through interactive visualizations.

- ℹ️ **About** — Learn more about the project architecture and technology stack.
""")