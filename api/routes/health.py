from datetime import datetime

from fastapi import APIRouter

from src.schemas.health_response import HealthResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "/",
    response_model=HealthResponse,
)
async def health():

    return HealthResponse(

        service="Warehouse Restock Prediction API",

        version="1.0.0",

        status="healthy",

        timestamp=datetime.utcnow(),
    )