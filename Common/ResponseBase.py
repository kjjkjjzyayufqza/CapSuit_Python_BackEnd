from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

# Defining a generalized type
DataType = TypeVar("DataType")

# Customizing the response type
class IResponseBase(BaseModel,Generic[DataType]):
    code: int = 200
    data: Optional[DataType] = None