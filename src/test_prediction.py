import pandas as pd

from predict import predict_customer_segment


# ---------------------------------
# Example customer
# ---------------------------------
sample_customer = {

    "Year_Birth": 1985,
    "Education": "Master",
    "Marital_Status": "Married",
    "Income": 85000,

    "Kidhome": 1,
    "Teenhome": 1,

    "Dt_Customer": "2021-06-15",

    "Recency": 12,

    "MntWines": 600,
    "MntFruits": 80,
    "MntMeatProducts": 500,
    "MntFishProducts": 120,
    "MntSweetProducts": 60,
    "MntGoldProds": 90,

    "NumDealsPurchases": 2,
    "NumWebPurchases": 8,
    "NumCatalogPurchases": 6,
    "NumStorePurchases": 5,

    "NumWebVisitsMonth": 3,

    "AcceptedCmp3": 0,
    "AcceptedCmp4": 1,
    "AcceptedCmp5": 1,
    "AcceptedCmp1": 1,
    "AcceptedCmp2": 0,

    "Complain": 0,
    "Response": 1
}

# ---------------------------------
# Convert to DataFrame
# ---------------------------------
input_df = pd.DataFrame([sample_customer])

# ---------------------------------
# Predict segment
# ---------------------------------
result = predict_customer_segment(input_df)

print(result)