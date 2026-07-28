import streamlit as st
import pandas as pd
import requests

st.title("📂 Batch Customer Prediction")

st.write(
    "Upload a customer dataset to generate customer segmentation "
    "and business recommendations for all customers."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

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

        col
        for col in required_columns
        if col not in df.columns

    ]

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

    if missing_columns:

        st.error(
            "The uploaded dataset is missing required columns."
        )

        st.write("Missing columns:")

        st.code("\n".join(missing_columns))

    else:

        predict_button = st.button(
            "Predict All Customers",
            use_container_width=True
        )

        if predict_button:

            with st.spinner(
                "Running customer segmentation..."
            ):

                uploaded_file.seek(0)

                response = requests.post(
                    "http://127.0.0.1:8000/predict_batch",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file,
                            "text/csv"
                        )
                    }
                )

            if response.status_code == 200:

                st.success(
                    "Batch prediction completed successfully!"
                )

                result_df = pd.read_csv(
                    pd.io.common.BytesIO(response.content)
                )

                st.divider()

                # =====================================
                # Prediction Summary
                # =====================================

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
                        (result_df["priority"] == "High").sum()
                    )

                with metric4:

                    st.metric(
                        "Campaigns Generated",
                        len(result_df)
                    )

                st.divider()

                # =====================================
                # Segment Distribution
                # =====================================

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

                st.divider()

                # =====================================
                # Business Recommendations Preview
                # =====================================

                st.header("🎯 Business Recommendations Preview")

                preview_columns = [

                    "segment_name",
                    "priority",
                    "recommended_campaign",
                    "workflow_name"

                ]

                st.dataframe(
                    result_df[preview_columns].head(10),
                    use_container_width=True,
                    hide_index=True
                )

                st.divider()

                st.download_button(
                    label="📥 Download Full Prediction Results",
                    data=response.content,
                    file_name="batch_prediction_results.csv",
                    mime="text/csv",
                    use_container_width=True
                )

            else:

                st.error(
                    "Batch prediction failed."
                )