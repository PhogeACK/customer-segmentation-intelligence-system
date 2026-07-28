import streamlit as st

st.title("🏠 Customer Segmentation Intelligence System")

st.markdown("""
Welcome to the **Customer Segmentation Intelligence System**.

This end-to-end Machine Learning application transforms raw customer marketing data into actionable business intelligence through behavioral customer segmentation.

Rather than simply assigning customers to clusters, the system automatically generates business personas, marketing campaign recommendations, workflow suggestions, and executive insights that support data-driven decision making.
""")

st.divider()

st.header("🎯 What This Application Does")

st.markdown("""
The application combines Machine Learning and Business Intelligence into one complete analytical workflow.

Using customer demographic information, purchasing behavior, and campaign history, the system automatically:

- Predicts customer segments using a trained K-Means clustering model
- Generates business personas for every customer
- Recommends marketing campaigns
- Recommends CRM workflows
- Supports individual customer analysis
- Processes entire customer datasets through batch prediction
- Visualizes customer insights through an interactive analytics dashboard
""")

st.divider()

st.header("⚙️ Machine Learning Pipeline")

st.markdown("""
The prediction pipeline follows a complete end-to-end Machine Learning workflow:

- Data Preprocessing
- Feature Engineering
- Categorical Encoding
- Feature Scaling
- K-Means Customer Segmentation
- Business Intelligence Generation
- Interactive Analytics Dashboard
""")

st.divider()

st.header("🚀 Application Features")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Prediction")

    st.success("✅ Individual Customer Prediction")
    st.success("✅ Batch Customer Prediction")
    st.success("✅ Customer Persona Generation")
    st.success("✅ Business Recommendations")

with col2:

    st.subheader("Analytics")

    st.success("✅ Executive Dashboard")
    st.success("✅ Customer Distribution Analysis")
    st.success("✅ Segment Value Analysis")
    st.success("✅ Executive Key Insights")

st.divider()

st.header("📌 Navigation")

st.markdown("""
Use the sidebar to navigate through the application:

- **🧍 Single Prediction** — Analyze one customer and receive immediate business recommendations.
- **📂 Batch Prediction** — Upload a customer dataset and generate predictions for every customer.
- **📊 Analytics Dashboard** — Explore customer segments, business insights, and executive summaries generated from your latest batch prediction.
- **ℹ️ About** — Learn more about the project architecture, machine learning pipeline, and technology stack.
""")

st.divider()

st.info(
    "💡 Tip: Start with **Batch Prediction**, then open the **Analytics Dashboard** to explore insights generated from your uploaded dataset."
)