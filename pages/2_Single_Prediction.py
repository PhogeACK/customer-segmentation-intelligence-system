import streamlit as st

st.title("👤 Single Customer Prediction")

st.write(
    "Enter customer information to generate behavioral segmentation "
    "and business recommendations."
)

st.divider()

# =====================================
# Customer Profile
# =====================================

st.header("Customer Profile")

col1, col2 = st.columns(2)

with col1:
    year_birth = st.number_input(
        "Year of Birth",
        min_value=1893,
        max_value=1996,
        value=1970
    )

    education = st.selectbox(
        "Education",
        [
            "Basic",
            "2n Cycle",
            "Graduation",
            "Master",
            "PhD"
        ]
    )

with col2:
    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Together",
            "Divorced",
            "Widow",
            "Alone",
            "YOLO",
            "Absurd"
        ]
    )

    income = st.number_input(
        "Income",
        min_value=1730,
        value=50000,
        step=1000
    )

st.divider()

# =====================================
# Household
# =====================================

st.header("Household")

col1, col2 = st.columns(2)

with col1:
    kidhome = st.slider(
        "Kids at Home",
        0,
        2,
        0
    )

with col2:
    teenhome = st.slider(
        "Teenagers at Home",
        0,
        2,
        0
    )

st.divider()

# =====================================
# Customer Activity
# =====================================

st.header("Customer Activity")

col1, col2 = st.columns(2)

with col1:
    dt_customer = st.date_input(
        "Customer Since"
    )

with col2:
    recency = st.slider(
        "Days Since Last Purchase",
        0,
        99,
        49
    )

st.divider()

# =====================================
# Spending
# =====================================

st.header("Product Spending")

col1, col2 = st.columns(2)

with col1:

    mnt_wines = st.number_input(
        "Wine",
        min_value=0,
        value=175
    )

    mnt_meat = st.number_input(
        "Meat",
        min_value=0,
        value=67
    )

    mnt_sweets = st.number_input(
        "Sweets",
        min_value=0,
        value=8
    )

with col2:

    mnt_fruits = st.number_input(
        "Fruits",
        min_value=0,
        value=8
    )

    mnt_fish = st.number_input(
        "Fish",
        min_value=0,
        value=12
    )

    mnt_gold = st.number_input(
        "Gold",
        min_value=0,
        value=24
    )

st.divider()

# =====================================
# Purchasing Behavior
# =====================================

st.header("Purchasing Behavior")

col1, col2 = st.columns(2)

with col1:

    deals = st.slider(
        "Deals Purchases",
        0,
        15,
        2
    )

    web = st.slider(
        "Web Purchases",
        0,
        27,
        4
    )

with col2:

    catalog = st.slider(
        "Catalog Purchases",
        0,
        28,
        2
    )

    store = st.slider(
        "Store Purchases",
        0,
        13,
        5
    )

website_visits = st.slider(
    "Website Visits Per Month",
    0,
    20,
    6
)

st.divider()

# =====================================
# Campaign History
# =====================================

st.header("Campaign History")

accepted_cmp1 = st.checkbox("Accepted Campaign 1")
accepted_cmp2 = st.checkbox("Accepted Campaign 2")
accepted_cmp3 = st.checkbox("Accepted Campaign 3")
accepted_cmp4 = st.checkbox("Accepted Campaign 4")
accepted_cmp5 = st.checkbox("Accepted Campaign 5")

complain = st.checkbox("Customer Complaint")

response = st.checkbox("Accepted Latest Campaign")

st.divider()

predict_button = st.button(
    "Predict Customer Segment",
    use_container_width=True
)