"""
Application dependencies.
"""

from functools import lru_cache

from src.pipeline.prediction_pipeline import PredictionPipeline


@lru_cache
def get_prediction_pipeline() -> PredictionPipeline:
    """
    Returns a singleton PredictionPipeline.
    """
    return PredictionPipeline()