# warehouse_restock_prediction



inventory-stock-prediction/
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env
├── .gitignore
│
├── data/
│   ├── raw/
│   │   ├── Products.csv
│   │   ├── Warehouses.csv
│   │   ├── Sales_History.csv
│   │   └── Inventory.csv
│   │
│   ├── processed/
│   │   ├── merged_dataset.csv
│   │   ├── training_dataset.csv
│   │   ├── train.csv
│   │   ├── validation.csv
│   │   └── test.csv
│   │
│   └── predictions/
│       ├── forecast.csv
│       └── restock_recommendation.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Model_Evaluation.ipynb
│
├── src/
│   │
│   ├── data/
│   │   ├── load_data.py
│   │   ├── merge_data.py
│   │   ├── preprocess.py
│   │   ├── feature_engineering.py
│   │   └── split_dataset.py
│   │
│   ├── models/
│   │   ├── train_catboost.py
│   │   ├── train_lightgbm.py
│   │   ├── train_xgboost.py
│   │   ├── evaluate.py
│   │   └── select_best_model.py
│   │
│   ├── prediction/
│   │   ├── forecast.py
│   │   ├── restock_engine.py
│   │   └── inference.py
│   │
│   ├── api/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── services.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── helper.py
│   │
│   └── config/
│       └── settings.py
│
├── models/
│   ├── catboost_model.pkl
│   ├── lightgbm_model.pkl
│   ├── xgboost_model.pkl
│   └── best_model.pkl
│
├── reports/
│   ├── model_metrics.csv
│   ├── feature_importance.csv
│   └── evaluation_report.pdf
│
├── tests/
│   ├── test_feature_engineering.py
│   ├── test_training.py
│   └── test_prediction.py
│
├── scripts/
│   ├── create_training_dataset.py
│   ├── train_models.py
│   ├── batch_prediction.py
│   └── generate_reports.py
│
└── deployment/
    ├── Dockerfile
    ├── docker-compose.yml
    └── nginx.conf


# work flow 

Raw CSV Files
│
├── Products.csv
├── Warehouses.csv
├── Sales_History.csv
└── Inventory.csv
        │
        ▼
merge_data.py
        │
        ▼
preprocess.py
        │
        ▼
feature_engineering.py
        │
        ▼
training_dataset.csv
        │
        ▼
split_dataset.py
        │
        ├── train.csv
        ├── validation.csv
        └── test.csv
        │
        ▼
Train CatBoost
Train LightGBM
Train XGBoost
        │
        ▼
Evaluate
        │
        ▼
best_model.pkl
        │
        ▼
FastAPI
        │
        ▼
{
    "product_id": "P000001",
    "hub_id": "HUB001",
    "year": 2025,
    "month": 6
}
        │
        ▼
{
    "current_stock": 120,
    "predicted_demand": 185,
    "remaining_stock": -65,
    "restock_required": true,
    "recommended_restock_quantity": 105
}