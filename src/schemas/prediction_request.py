"""
Prediction request schema.
"""

from pydantic import BaseModel
from pydantic import Field


class PredictionRequest(BaseModel):
    """
    Inventory prediction request.
    """

    year: int = Field(..., ge=2020)

    month: int = Field(..., ge=1, le=12)

    product_id: int

    hub_id: int

    category: str

    brand: str

    city: str

    product_name: str

    opening_stock: int = Field(..., ge=0)

    sales_last_1: float

    sales_last_2: float

    sales_last_3: float

    avg_sales_3: float

    promotion: int = Field(..., ge=0, le=1)

    discount_percentage: float = Field(..., ge=0)

    festival_flag: int = Field(..., ge=0, le=1)

    returns: int = Field(..., ge=0)

    model_config = {
        "extra": "forbid",
        "str_strip_whitespace": True,
    }