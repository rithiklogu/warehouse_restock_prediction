from fastapi import APIRouter
from fastapi import Depends

from api.dependencies import get_prediction_pipeline

from src.pipeline.prediction_pipeline import PredictionPipeline

from src.schemas.api_response import ApiResponse
from src.schemas.prediction_request import PredictionRequest
from src.schemas.prediction_response import PredictionResponse

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"],
)


@router.post(
    "/predict",
    response_model=ApiResponse[PredictionResponse],
)
async def predict(

    request: PredictionRequest,

    pipeline: PredictionPipeline = Depends(
        get_prediction_pipeline,
    ),

):

    prediction = pipeline.run(request)

    return ApiResponse(

        message="Prediction completed successfully.",

        data=prediction,
    )