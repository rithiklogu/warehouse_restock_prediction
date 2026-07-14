"""
FastAPI application entry point.
"""

from fastapi import FastAPI

from api.routes.health import router as health_router
from api.routes.prediction import router as prediction_router

from api.middleware import register_middleware

app = FastAPI(
    title="Warehouse Restock Prediction API",
    description="Production ML API for Warehouse Inventory Prediction",
    version="1.0.0",
)

# Register Middleware
register_middleware(app)

# Register Routers
app.include_router(health_router)
app.include_router(prediction_router)