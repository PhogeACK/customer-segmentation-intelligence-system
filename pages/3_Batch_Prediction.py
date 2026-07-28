import streamlit as st
import pandas as pd

from src.batch_predict import predict_batch


st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Batch Customer Prediction")

st.write(
    "Upload a customer dataset to generate customer segmentation "
    "and business recommendations for all customers."
)

st.divider()


# ============================================
# Upload
# ============================================

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)


if uploaded_file is None:

    st.info("Upload a CSV file to begin.")

    st.stop()


# ============================================
# Read dataset
# ============================================

df = pd.read_csv(uploaded_file)


required_columns = [

    "Year_Birth",
    "Education",
    "Marital_Status",
    "Income",

    "Kidhome",
    "Teenhome",

    "Dt_Customer",

    "Recency",

    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds",

    "NumDealsPurchases",
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases",

    "NumWebVisitsMonth",

    "AcceptedCmp1",
    "AcceptedCmp2",
    "AcceptedCmp3",
    "AcceptedCmp4",
    "AcceptedCmp5",

    "Complain",
    "Response"

]


missing_columns = [

    column
    for column in required_columns
    if column not in df.columns

]


# ============================================
# Validation
# ============================================

if missing_columns:

    st.error(
        "The uploaded dataset is missing required columns."
    )

    st.code("\n".join(missing_columns))

    st.stop()


# ============================================
# Dataset Preview
# ============================================

st.subheader("Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Rows",
        f"{len(df):,}"
    )

with col2:

    st.metric(
        "Columns",
        len(df.columns)
    )

st.divider()


# ============================================
# Prediction
# ============================================

if st.button(
    "Predict All Customers",
    use_container_width=True
):

    with st.spinner(
        "Running customer segmentation..."
    ):

        result_df = predict_batch(df)

    st.session_state["batch_results"] = result_df

    st.success(
        "Batch prediction completed successfully!"
    )


# ============================================
# Stop here if nothing predicted yet
# ============================================

if "batch_results" not in st.session_state:

    st.stop()


result_df = st.session_state["batch_results"]

# ============================================
# Prediction Summary
# ============================================

st.divider()

st.header("📊 Prediction Summary")

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.metric(
        "Customers Processed",
        f"{len(result_df):,}"
    )

with metric2:

    st.metric(
        "Segments Found",
        result_df["cluster_id"].nunique()
    )

with metric3:

    st.metric(
        "High Priority Customers",
        int((result_df["priority"] == "High").sum())
    )

with metric4:

    st.metric(
        "Campaigns Generated",
        len(result_df)
    )


# ============================================
# Segment Distribution
# ============================================

st.divider()

st.header("📈 Segment Distribution")

segment_summary = (
    result_df["segment_name"]
    .value_counts()
    .reset_index()
)

segment_summary.columns = [
    "Segment",
    "Customers"
]

st.dataframe(
    segment_summary,
    use_container_width=True,
    hide_index=True
)


# ============================================
# Business Recommendations Preview
# ============================================

st.divider()

st.header("🎯 Business Recommendations Preview")

preview_columns = [

    "segment_name",
    "priority",
    "recommended_campaign",
    "workflow_name"

]

st.dataframe(
    result_df[preview_columns],
    use_container_width=True,
    hide_index=True
)

# ============================================
# Export Results
# ============================================

st.divider()

csv = result_df.to_csv(
    index=False
).encode("utf-8")

col1, col2 = st.columns(2)

with col1:

    st.download_button(
        label="📥 Download Full Prediction Results",
        data=csv,
        file_name="batch_prediction_results.csv",
        mime="text/csv",
        use_container_width=True,
        key="download_batch_results"
    )

with col2:

    if st.button(
        "📊 Open Analytics Dashboard",
        use_container_width=True,
        key="open_dashboard"
    ):

        st.switch_page(
            "pages/4_Analytics_Dashboard.py"
        )


# ============================================
# Dataset Overview
# ============================================

st.divider()

with st.expander("📄 View Full Prediction Results"):

    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True
    )