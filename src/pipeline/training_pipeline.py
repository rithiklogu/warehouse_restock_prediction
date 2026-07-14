"""
Training Pipeline.

Orchestrates the complete machine learning training workflow.
"""

import sys

from catboost import CatBoostRegressor

from src.config.settings import settings

from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.preprocess import Preprocess
from src.components.feature_engineering.feature_builder import FeatureBuilder
from src.components.splitting.time_series_split import TimeSeriesSplitter

from src.components.training.model_trainer import ModelTrainer
from src.components.training.model_evaluator import ModelEvaluator

from src.components.persistence.model_saver import ModelSaver

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class TrainingPipeline:
    """
    End-to-end training pipeline.
    """

    def __init__(self):

        logger.info("TrainingPipeline initialized.")

    def run(self):

        try:

            logger.info("=" * 80)
            logger.info("Starting Training Pipeline")
            logger.info("=" * 80)

                
            # Data Ingestion
                

            datasets = DataIngestion().run()

                
            # Data Preprocessing
                

            dataframe = Preprocess().run(
                datasets
            )

                
            # Feature Engineering
                

            dataframe = FeatureBuilder().run(
                dataframe
            )

                
            # Train / Validation / Test Split
                

            train_df, validation_df, test_df = (
                TimeSeriesSplitter().run(
                    dataframe
                )
            )

                
            # Feature Selection
                

            target = settings.target_column

            features = settings.feature_columns

            cat_features = settings.categorical_features

            X_train = train_df.select(features)
            y_train = train_df[target]

            X_validation = validation_df.select(features)
            y_validation = validation_df[target]

            X_test = test_df.select(features)
            y_test = test_df[target]

                
            # Model
                

            model = CatBoostRegressor(
                **settings.model_params
            )

                
            # Training
                

            trained_model = ModelTrainer(
                model
            ).run(
                X_train=X_train,
                y_train=y_train,
                cat_features=cat_features,
            )

                
            # Evaluation
                

            evaluator = ModelEvaluator()

            train_metrics = evaluator.run(
                trained_model,
                X_train,
                y_train,
            )

            validation_metrics = evaluator.run(
                trained_model,
                X_validation,
                y_validation,
            )

            test_metrics = evaluator.run(
                trained_model,
                X_test,
                y_test,
            )

                
            # Save Artifacts
                

            ModelSaver().run(
                model=trained_model,
                metrics={
                    "train": train_metrics["metrics"],
                    "validation": validation_metrics["metrics"],
                    "test": test_metrics["metrics"],
                },
                feature_columns=features,
            )

            logger.success("=" * 80)
            logger.success("Training Pipeline Completed Successfully.")
            logger.success("=" * 80)

            return trained_model

        except Exception as e:

            logger.exception(
                "Training pipeline failed."
            )

            raise CustomException(
                e,
                sys,
            )