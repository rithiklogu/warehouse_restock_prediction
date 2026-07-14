"""
Schema Validation Component.

Validates dataframe structure before preprocessing.
"""

from typing import Iterable

import polars as pl

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class SchemaValidator:
    """
    Validate dataframe schema.
    """

    def __init__(self) -> None:
        logger.info("SchemaValidator initialized.")

    def validate(
        self,
        dataframe: pl.DataFrame,
        required_columns: Iterable[str],
        dataset_name: str,
    ) -> bool:
        """
        Validate dataframe schema.

        Parameters
        ----------
        dataframe
            Input dataframe.

        required_columns
            Expected columns.

        dataset_name
            Dataset name for logging.

        Returns
        -------
        bool
        """

        try:

            logger.info(
                f"Validating schema for '{dataset_name}'..."
            )

            if dataframe.is_empty():

                raise ValueError(
                    f"{dataset_name} is empty."
                )

            missing_columns = [
                column
                for column in required_columns
                if column not in dataframe.columns
            ]

            if missing_columns:

                raise ValueError(
                    f"Missing columns: {missing_columns}"
                )

            duplicate_columns = [
                col
                for col in dataframe.columns
                if dataframe.columns.count(col) > 1
            ]

            if duplicate_columns:

                raise ValueError(
                    f"Duplicate columns: {duplicate_columns}"
                )

            logger.success(
                f"Schema validation passed for '{dataset_name}'."
            )

            return True

        except Exception as e:

            logger.exception(
                "Schema validation failed."
            )

            raise CustomException(
                e,
                __import__("sys"),
            )