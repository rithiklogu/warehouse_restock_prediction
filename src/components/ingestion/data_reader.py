"""
Data Reader Component.

Loads all configured raw datasets using the CSVLoader.
"""

from pathlib import Path

import polars as pl

from src.components.ingestion.csv_loader import CSVLoader
from src.config.paths import RAW_DATA_DIR
from src.config.settings import settings
from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class DataReader:
    """
    Read all raw datasets required by the project.
    """

    def __init__(self) -> None:
        self.loader = CSVLoader()
        logger.info("DataReader initialized.")

    def read_all(self) -> dict[str, pl.DataFrame]:
        """
        Load all configured datasets.

        Returns:
            dict[str, pl.DataFrame]:
                Dictionary containing all loaded datasets.
        """

        try:

            logger.info("Reading all raw datasets...")

            datasets: dict[str, pl.DataFrame] = {}

            for dataset_name, file_name in settings.datasets.items():

                file_path = RAW_DATA_DIR / file_name

                datasets[dataset_name] = self.loader.load(file_path)

            logger.success(
                f"Successfully loaded {len(datasets)} datasets."
            )

            return datasets

        except Exception as e:
            logger.exception("Failed to read datasets.")
            raise CustomException(e, __import__("sys"))