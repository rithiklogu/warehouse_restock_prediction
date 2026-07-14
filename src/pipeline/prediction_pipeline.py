"""
Prediction Pipeline.

Orchestrates the complete inference workflow.
"""

import sys

from src.components.persistence.model_loader import ModelLoader
from src.components.prediction.model_predictor import Predictor
from src.components.prediction.business_logic import BusinessLogic

from src.schemas.prediction_request import PredictionRequest
from src.schemas.prediction_response import PredictionResponse

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class PredictionPipeline:
    """
    End-to-end prediction pipeline.
    """

    def __init__(self):

        logger.info("PredictionPipeline initialized.")

        self.model = ModelLoader().run()

        self.predictor = Predictor()

        self.business_logic = BusinessLogic()

    def run(
        self,
        request: PredictionRequest,
    ) -> PredictionResponse:

        try:

            logger.info("=" * 80)
            logger.info("Starting Prediction Pipeline")
            logger.info("=" * 80)

              
            # Generate prediction
              

            prediction = self.predictor.run(
                model=self.model,
                request=request,
            )

              
            # Apply business rules
              

            response = self.business_logic.run(
                predicted_demand=prediction,
                current_stock=request.opening_stock,
            )

            logger.success(
                "Prediction Pipeline completed successfully."
            )

            return response

        except Exception as e:

            logger.exception(
                "Prediction Pipeline failed."
            )

            raise CustomException(
                e,
                sys,
            )