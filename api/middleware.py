import time

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


def register_middleware(app: FastAPI):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    @app.middleware("http")
    async def request_logger(request, call_next):

        start = time.perf_counter()

        response = await call_next(request)

        elapsed = time.perf_counter() - start

        logger.info(
            f"{request.method} {request.url.path} "
            f"{response.status_code} "
            f"{elapsed:.3f}s"
        )

        response.headers["X-Process-Time"] = f"{elapsed:.3f}"

        return response

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):

        errors = []

        for error in exc.errors():

            errors.append(
                {
                    "field": ".".join(
                        str(item)
                        for item in error["loc"][1:]
                    ),
                    "message": error["msg"],
                }
            )

        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "error_code": "VALIDATION_ERROR",
                "message": "Request validation failed.",
                "details": errors,
            },
        )

    @app.exception_handler(CustomException)
    async def custom_exception_handler(request, exc):

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error_code": "APPLICATION_ERROR",
                "message": str(exc),
            },
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request, exc):

        logger.exception(exc)

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error_code": "INTERNAL_SERVER_ERROR",
                "message": "Unexpected server error.",
            },
        )