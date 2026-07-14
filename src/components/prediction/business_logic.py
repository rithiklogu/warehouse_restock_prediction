"""
Business logic for warehouse inventory prediction.
"""

import math
import sys

from src.exception.custom_exception import CustomException
from src.schemas.prediction_response import PredictionResponse
from src.logger.logger import logger


class BusinessLogic:
    """
    Applies inventory business rules.
    """

    def __init__(self):

        logger.info("BusinessLogic initialized.")

    def run(
        self,
        predicted_demand: float,
        current_stock: int,
    ) -> dict:

        try:

            logger.info(
                "Applying business rules..."
            )

            predicted_demand = math.ceil(
                predicted_demand
            )

            safety_stock = max(
                int(predicted_demand * 0.20),
                10,
            )

            remaining_stock = (
                current_stock - predicted_demand
            )

            restock_required = (
                remaining_stock < safety_stock
            )

            if restock_required:

                recommended_order_quantity = (
                    safety_stock - remaining_stock
                )

            else:

                recommended_order_quantity = 0

            logger.success(
                "Business logic applied successfully."
            )

           
        
            return PredictionResponse(

                predicted_demand=predicted_demand,

                current_stock=current_stock,

                remaining_stock=remaining_stock,

                safety_stock=safety_stock,

                restock_required=restock_required,

                recommended_order_quantity=recommended_order_quantity,

                recommendation=(
                    "Restock immediately"
                    if restock_required
                    else "Inventory level is sufficient"
                ),

                confidence=95.0,
            )

        except Exception as e:

            logger.exception(
                "Business logic failed."
            )

            raise CustomException(
                e,
                sys,
            )