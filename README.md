# Customer Segmentation Intelligence System

An end-to-end machine learning application that transforms raw customer data into actionable business intelligence through behavioral segmentation, marketing recommendations, and workflow automation.

---

## Additional Documentation

This repository contains two complementary parts:

- **Product Documentation** — this README describes the production application and software architecture.
- **Machine Learning Research** — the complete experimentation process, EDA, feature engineering, clustering analysis, and model selection can be found in:

📄 **[Machine Learning Research](notebooks/README_ML.pdf)**

---
# 1. Introduction

...

---

# 2. Key Features

- Behavioral customer segmentation using K-Means clustering
- Business persona generation
- Marketing recommendation engine
- Workflow recommendation engine
- REST API for single and batch predictions
- Modular architecture designed for future expansion

---

# 3. System Overview

...

(Architecture image)

Customer Data

↓

Prediction

↓

Customer Segment

↓

Business Intelligence

↓

API Response

↓

Marketing Action

---

# 4. Product Architecture

(Miro diagram)

Workflow summary...

---

# 5. Project Structure

```text
Customer-Segmentation-Intelligence-System/
│
├── src/
├── models/
├── notebooks/
├── docs/
├── data/
├── README.md
└── requirements.txt
```

---

# 6. Prediction Pipeline

Receive customer

↓

Validate input

↓

Preprocess

↓

Load trained model

↓

Predict customer segment

↓

Generate customer persona

↓

Generate business recommendations

↓

Assign operational workflow

↓

Return enriched business intelligence response

---

# 7. Business Intelligence Layer

## Persona Engine

...

## Recommendation Engine

...

## Workflow Engine

...

---

# 8. API

## POST /predict

...

## POST /predict_batch

...

---

# 9. Example Output

(JSON example)

---

# 10. Running the Project

1. Clone repository
2. Install dependencies
3. Run FastAPI
4. Open Swagger UI
5. Test endpoints

---

# 11. Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Machine Learning | scikit-learn |
| Data Processing | pandas, NumPy |
| API | FastAPI |
| Model | K-Means |
| Serialization | joblib |
| Documentation | Markdown |
| Visualization | Matplotlib, Plotly |

---

# 12. Roadmap

## Version 1 ✅

Customer Segmentation Intelligence System

## Version 2

Interactive Business Dashboard

## Version 3

Business Automation (n8n)

## Version 4

Dynamic Decision Engine

## Version 5

Cloud Deployment

