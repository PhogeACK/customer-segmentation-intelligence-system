import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Segmentation Intelligence Dashboard")

st.write(
    "Executive business insights generated from the latest batch prediction."
)

st.divider()

# ============================================
# Load latest prediction
# ============================================

if "batch_results" not in st.session_state:

    st.warning(
        "No batch prediction available."
    )

    st.info(
        "Please generate a Batch Prediction first."
    )

    st.stop()

result_df = st.session_state["batch_results"]

# ============================================
# Executive KPIs
# ============================================

st.header("📈 Executive Overview")

total_customers = len(result_df)

total_segments = result_df["cluster_id"].nunique()

average_income = result_df["Income"].mean()

average_spending = (

    result_df[
        [
            "MntWines",
            "MntFruits",
            "MntMeatProducts",
            "MntFishProducts",
            "MntSweetProducts",
            "MntGoldProds"
        ]
    ]
    .sum(axis=1)
    .mean()

)

high_priority = (
    result_df["priority"] == "High"
).sum()

metric1, metric2, metric3, metric4, metric5 = st.columns(5)

with metric1:

    st.metric(
        "Customers",
        f"{total_customers:,}"
    )

with metric2:

    st.metric(
        "Segments",
        total_segments
    )

with metric3:

    st.metric(
        "Avg Income",
        f"${average_income:,.0f}"
    )

with metric4:

    st.metric(
        "Avg Spending",
        f"${average_spending:,.0f}"
    )

with metric5:

    st.metric(
        "High Priority",
        high_priority
    )

# ============================================
# Customer Distribution
# ============================================

st.divider()

st.header("📈 Customer Distribution")

col1, col2 = st.columns(2)

# --------------------------------------------
# Segment Distribution
# --------------------------------------------

with col1:

    segment_summary = (
        result_df["segment_name"]
        .value_counts()
        .reset_index()
    )

    segment_summary.columns = [
        "Segment",
        "Customers"
    ]

    fig_segment = px.bar(
        segment_summary,
        x="Customers",
        y="Segment",
        orientation="h",
        text="Customers",
        title="Customers by Segment"
    )

    fig_segment.update_layout(
        height=450,
        showlegend=False,
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )

# --------------------------------------------
# Priority Distribution
# --------------------------------------------

with col2:

    priority_summary = (
        result_df["priority"]
        .value_counts()
        .reset_index()
    )

    priority_summary.columns = [
        "Priority",
        "Customers"
    ]

    fig_priority = px.pie(
        priority_summary,
        names="Priority",
        values="Customers",
        title="Priority Distribution"
    )

    fig_priority.update_layout(
        height=450
    )

    st.plotly_chart(
        fig_priority,
        use_container_width=True
    )

# ============================================
# Segment Value Analysis
# ============================================

st.divider()

st.header("💼 Segment Value Analysis")

col1, col2 = st.columns(2)

# --------------------------------------------
# Average Income by Segment
# --------------------------------------------

with col1:

    income_summary = (
        result_df
        .groupby("segment_name")["Income"]
        .mean()
        .reset_index()
    )

    income_summary.columns = [
        "Segment",
        "Average Income"
    ]

    fig_income = px.bar(
        income_summary,
        x="Average Income",
        y="Segment",
        orientation="h",
        text="Average Income",
        title="Average Income by Segment"
    )

    fig_income.update_traces(
        texttemplate="$%{text:,.0f}",
        textposition="outside"
    )

    fig_income.update_layout(
        height=450,
        showlegend=False,
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig_income,
        use_container_width=True
    )

# --------------------------------------------
# Average Spending by Segment
# --------------------------------------------

with col2:

    spending_df = result_df.copy()

    spending_df["Total Spending"] = (

        spending_df["MntWines"]
        + spending_df["MntFruits"]
        + spending_df["MntMeatProducts"]
        + spending_df["MntFishProducts"]
        + spending_df["MntSweetProducts"]
        + spending_df["MntGoldProds"]

    )

    spending_summary = (

        spending_df
        .groupby("segment_name")["Total Spending"]
        .mean()
        .reset_index()

    )

    spending_summary.columns = [
        "Segment",
        "Average Spending"
    ]

    fig_spending = px.bar(
        spending_summary,
        x="Average Spending",
        y="Segment",
        orientation="h",
        text="Average Spending",
        title="Average Spending by Segment"
    )

    fig_spending.update_traces(
        texttemplate="$%{text:,.0f}",
        textposition="outside"
    )

    fig_spending.update_layout(
        height=450,
        showlegend=False,
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig_spending,
        use_container_width=True
    )

# ============================================
# Customer Personas
# ============================================

st.divider()

st.header("👤 Customer Personas")

persona_df = (

    result_df
    .groupby("segment_name")
    .agg(
        Customers=("cluster_id", "count"),
        Priority=("priority", "first"),
        Business_Value=("business_value", "first"),
        Primary_Goal=("primary_goal", "first"),
        Campaign=("recommended_campaign", "first"),
        Workflow=("workflow_name", "first"),
        Opportunity=("opportunity", "first"),
        Risk=("risk", "first")
    )
    .reset_index()

)

for i in range(0, len(persona_df), 2):

    col1, col2 = st.columns(2)

    # -----------------------------
    # Left Card
    # -----------------------------

    with col1:

        row = persona_df.iloc[i]

        with st.container(border=True):

            st.subheader(f"👤 {row['segment_name']}")

            st.metric(
                "Customers",
                row["Customers"]
            )

            st.metric(
                "Priority",
                row["Priority"]
            )

            st.markdown("**💰 Business Value**")
            st.write(row["Business_Value"])

            st.markdown("**🎯 Primary Goal**")
            st.write(row["Primary_Goal"])

            st.markdown("**📣 Recommended Campaign**")
            st.success(row["Campaign"])

            st.markdown("**⚙ Recommended Workflow**")
            st.info(row["Workflow"])

            st.markdown("**🚀 Opportunity**")
            st.write(row["Opportunity"])

            st.markdown("**⚠ Risk**")
            st.warning(row["Risk"])

    # -----------------------------
    # Right Card
    # -----------------------------

    if i + 1 < len(persona_df):

        with col2:

            row = persona_df.iloc[i + 1]

            with st.container(border=True):

                st.subheader(f"👤 {row['segment_name']}")

                st.metric(
                    "Customers",
                    row["Customers"]
                )

                st.metric(
                    "Priority",
                    row["Priority"]
                )

                st.markdown("**💰 Business Value**")
                st.write(row["Business_Value"])

                st.markdown("**🎯 Primary Goal**")
                st.write(row["Primary_Goal"])

                st.markdown("**📣 Recommended Campaign**")
                st.success(row["Campaign"])

                st.markdown("**⚙ Recommended Workflow**")
                st.info(row["Workflow"])

                st.markdown("**🚀 Opportunity**")
                st.write(row["Opportunity"])

                st.markdown("**⚠ Risk**")
                st.warning(row["Risk"])
                
# ============================================
# Executive Key Insights
# ============================================

st.divider()

st.header("💡 Executive Key Insights")

largest_segment = (
    result_df["segment_name"]
    .value_counts()
    .idxmax()
)

largest_count = (
    result_df["segment_name"]
    .value_counts()
    .max()
)

spending_df = result_df.copy()

spending_df["Total Spending"] = (

    spending_df["MntWines"]
    + spending_df["MntFruits"]
    + spending_df["MntMeatProducts"]
    + spending_df["MntFishProducts"]
    + spending_df["MntSweetProducts"]
    + spending_df["MntGoldProds"]

)

highest_value_segment = (

    spending_df
    .groupby("segment_name")["Total Spending"]
    .mean()
    .idxmax()

)

top_campaign = (
    result_df["recommended_campaign"]
    .value_counts()
    .idxmax()
)

high_priority = (
    result_df["priority"] == "High"
).sum()

high_priority_pct = (
    high_priority
    / len(result_df)
) * 100

st.success(

    f"""
### Largest Customer Segment

**{largest_segment}**

This segment contains **{largest_count:,} customers**, making it the largest customer group in the uploaded dataset.

---

### Highest Customer Value

**{highest_value_segment}**

This segment generates the highest average customer spending and should remain a strategic retention priority.

---

### Recommended Marketing Focus

The most frequently recommended campaign is:

**{top_campaign}**

This indicates the primary business opportunity identified by the segmentation model.

---

### High Priority Customers

**{high_priority:,} customers ({high_priority_pct:.1f}% of the dataset)**

These customers should receive immediate business attention before lower-priority segments.

"""
)