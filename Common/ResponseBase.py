from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from typing import Generic, Optional, TypeVar
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({"detail": exc.errors(), "error": exc.body}),
    )


DataType = TypeVar("DataType")

class IResponseBase(BaseModel,Generic[DataType]):
    code: int = 200
    data: Optional[DataType] = None