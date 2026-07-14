"""
Data Ingestion Component.

Acts as the public interface for loading all raw datasets.
"""

from typing import Dict

import polars as pl

from src.components.ingestion.data_reader import DataReader
from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class DataIngestion:
    """
    Orchestrates the ingestion process.

    This class is the only entry point used by the
    training and prediction pipelines.
    """

    def __init__(self) -> None:
        self.reader = DataReader()
        logger.info("DataIngestion initialized.")

    def run(self) -> Dict[str, pl.DataFrame]:
        """
        Execute the ingestion process.

        Returns
        -------
        Dict[str, pl.DataFrame]
            Dictionary containing all raw datasets.
        """

        try:

            logger.info("Starting data ingestion...")

            datasets = self.reader.read_all()

            logger.success(
                "Data ingestion completed successfully."
            )

            return datasets

        except Exception as e:
            logger.exception("Data ingestion failed.")
            raise CustomException(e, __import__("sys"))