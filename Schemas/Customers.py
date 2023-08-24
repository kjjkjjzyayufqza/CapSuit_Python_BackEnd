from typing import Optional
from pydantic import BaseModel
from decimal import Decimal

class CustomersBasicSchemas(BaseModel):
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
        json_schema_extra = {
            "example": {
                "contactLastName": "string",
                "contactFirstName": "string",
                "creditLimit": 0.0,
            }
        }