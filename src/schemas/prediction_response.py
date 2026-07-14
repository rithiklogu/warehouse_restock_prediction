"""
Prediction response schema.
"""

from pydantic import BaseModel
from pydantic import Field


class PredictionResponse(BaseModel):
    """
    Prediction response.
    """

    predicted_demand: int = Field(..., ge=0)

    current_stock: int = Field(..., ge=0)

    remaining_stock: int

    safety_stock: int = Field(..., ge=0)

    restock_required: bool

    recommended_order_quantity: int = Field(..., ge=0)

    recommendation: str

    confidence: float = Field(..., ge=0.0, le=100.0)

    model_config = {
        "extra": "forbid"
    }   