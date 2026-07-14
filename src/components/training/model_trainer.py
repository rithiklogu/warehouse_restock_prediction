"""
Model Trainer Component.

Responsible only for training the CatBoost model.
"""

import sys

import polars as pl
from catboost import CatBoostRegressor

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class ModelTrainer:
    """
    Train a CatBoost regression model.
    """

    def __init__(
        self,
        model: CatBoostRegressor,
    ) -> None:

        self.model = model

        logger.info("ModelTrainer initialized.")

    def run(
        self,
        X_train: pl.DataFrame,
        y_train: pl.Series,
        cat_features: list[str],
    ) -> CatBoostRegressor:
        """
        Train the CatBoost model.

        Parameters
        ----------
        X_train : pl.DataFrame
            Training feature dataframe.

        y_train : pl.Series
            Target values.

        cat_features : list[str]
            Categorical feature names.

        Returns
        -------
        CatBoostRegressor
        """

        try:

            logger.info("Starting CatBoost model training...")

            self.model.fit(
                X=X_train.to_pandas(),
                y=y_train.to_pandas(),
                cat_features=cat_features,
                verbose=False,
            )

            logger.success(
                "CatBoost model trained successfully."
            )

            return self.model

        except Exception as e:

            logger.exception(
                "Model training failed."
            )

            raise CustomException(e, sys)