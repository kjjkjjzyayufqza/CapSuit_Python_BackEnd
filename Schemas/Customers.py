from typing import Optional
from pydantic import BaseModel
from decimal import Decimal

#Define Schemas to be used for data checking when submitting data
class CustomersSchemas(BaseModel):
    customerNumber: int
    customerName: str
    contactLastName: str
    contactFirstName: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str] | None = None
    city: str
    state: Optional[str] | None = None
    postalCode: Optional[str] | None = None
    country: str
    salesRepEmployeeNumber: Optional[int] | None = None
    creditLimit: Optional[Decimal] | None = None

class UpdateCustomerSchemas(BaseModel):
    contactLastName: str
    contactFirstName: str
    creditLimit: Optional[Decimal] | None = None
    class Config:
        # Swagger example data
        json_schema_extra = {
            "example": {
                "contactLastName": "string",
                "contactFirstName": "string",
                "creditLimit": 0.0,
            }
        }