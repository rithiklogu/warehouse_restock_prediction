"""
Model Evaluation Component.

Responsible for evaluating a trained CatBoost regression model.
"""

import sys
import numpy as np
import polars as pl

from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
)

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class ModelEvaluator:
    """
    Evaluate a trained regression model.

    Metrics
    -------
    - MAE
    - RMSE
    - MAPE
    - R2 Score
    """

    def __init__(self) -> None:
        logger.info("ModelEvaluator initialized.")

    def run(
        self,
        model,
        X: pl.DataFrame,
        y: pl.Series,
    ) -> dict:
        """
        Evaluate a trained model.

        Parameters
        ----------
        model
            Trained CatBoost model.

        X : pl.DataFrame
            Feature dataframe.

        y : pl.Series
            Ground truth target values.

        Returns
        -------
        dict
            Dictionary containing predictions and evaluation metrics.
        """

        try:

            logger.info("Evaluating model...")

            # --------------------------------------------------------
            # Prediction
            # --------------------------------------------------------

            predictions = model.predict(
                X.to_pandas()
            )

            # --------------------------------------------------------
            # Metrics
            # --------------------------------------------------------

            mae = float(
                mean_absolute_error(
                    y.to_numpy(),
                    predictions,
                )
            )

            mse = float(
                mean_squared_error(
                    y.to_numpy(),
                    predictions,
                )
            )

            rmse = float(
                np.sqrt(mse)
            )

            mape = float(
                mean_absolute_percentage_error(
                    y.to_numpy(),
                    predictions,
                )
                * 100
            )

            r2 = float(
                r2_score(
                    y.to_numpy(),
                    predictions,
                )
            )

            metrics = {
                "MAE": mae,
                "RMSE": rmse,
                "MAPE": mape,
                "R2": r2,
            }

            logger.success("Model evaluation completed successfully.")

            logger.info(
                f"MAE  : {mae:.4f}"
            )

            logger.info(
                f"RMSE : {rmse:.4f}"
            )

            logger.info(
                f"MAPE : {mape:.4f}"
            )

            logger.info(
                f"R2   : {r2:.4f}"
            )

            return {
                "metrics": metrics,
                "predictions": predictions,
            }

        except Exception as e:

            logger.exception(
                "Model evaluation failed."
            )

            raise CustomException(
                e,
                sys,
            )