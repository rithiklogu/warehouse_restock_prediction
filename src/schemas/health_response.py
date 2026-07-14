"""
Health response schema.
"""

from datetime import datetime

from pydantic import BaseModel


class HealthResponse(BaseModel):

    success: bool = True

    service: str

    version: str

    status: str

    timestamp: datetime