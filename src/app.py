from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi.responses import FileResponse

from pydantic import BaseModel

import pandas as pd

from src.predict import predict_customer_segment
from src.batch_predict import predict_batch

# ---------------------------------
# Initialize FastAPI app
# ---------------------------------
app = FastAPI(
    title="Customer Segmentation Engine",
    description="Behavioral clustering and persona recommendation system",
    version="1.0"
)


# ---------------------------------
# Input schema
# ---------------------------------
class CustomerInput(BaseModel):

    Year_Birth: int
    Education: str
    Marital_Status: str
    Income: float

    Kidhome: int
    Teenhome: int

    Dt_Customer: str

    Recency: int

    MntWines: float
    MntFruits: float
    MntMeatProducts: float
    MntFishProducts: float
    MntSweetProducts: float
    MntGoldProds: float

    NumDealsPurchases: int
    NumWebPurchases: int
    NumCatalogPurchases: int
    NumStorePurchases: int

    NumWebVisitsMonth: int

    AcceptedCmp3: int
    AcceptedCmp4: int
    AcceptedCmp5: int
    AcceptedCmp1: int
    AcceptedCmp2: int

    Complain: int
    Response: int


# ---------------------------------
# Health check endpoint
# ---------------------------------
@app.get("/")
def home():

    return {
        "message": "Customer Segmentation Engine API is running"
    }


# ---------------------------------
# Prediction endpoint
# ---------------------------------
@app.post("/predict")
def predict(customer: CustomerInput):

    # Convert request into DataFrame
    input_df = pd.DataFrame([customer.dict()])

    # Run prediction pipeline
    result = predict_customer_segment(input_df)

    return result

# ---------------------------------
# Batch prediction endpoint
# ---------------------------------
@app.post("/predict_batch")
async def predict_batch_endpoint(
    file: UploadFile = File(...)
):

    # Read uploaded CSV
    df = pd.read_csv(file.file)

    # Run batch prediction
    results_df = predict_batch(df)

    # Temporary output path
    output_path = "batch_prediction_results.csv"

    # Save predictions
    results_df.to_csv(output_path, index=False)

    # Return downloadable file
    return FileResponse(
        path=output_path,
        filename="batch_prediction_results.csv",
        media_type="text/csv"
    )