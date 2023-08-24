from typing import Union
from fastapi import FastAPI,Depends
from Function.CustomersFunction import get_customers, get_customers_by_id, update_customers_by_id
from Routers.db import get_db
from sqlalchemy.orm import Session
from Schemas.Customers import CustomersBasicSchemas, CustomersSchemas, UpdateCustomerSchemas
from Common.ResponseBase import IResponseBase

app = FastAPI()

@app.get("/getCustomers", tags=["Customers"], response_model=IResponseBase[list[CustomersBasicSchemas]])
def getCustomers(customerName: Union[str, None] = None,
               contactLastName: Union[str, None] = None, 
               contactFirstName: Union[str, None] = None, 
               creditLimitDesc : bool = None,
               db: Session = Depends(get_db)):
    customers = get_customers(db,customerName,contactLastName,contactFirstName,creditLimitDesc)
    return IResponseBase(data=customers)

@app.get("/getCustomerByNumber/{customerNumber}", tags=["Customers"], response_model=IResponseBase[CustomersSchemas])
def getCustomerById(customerNumber: int, db: Session = Depends(get_db)):
    customer = get_customers_by_id(db,customerNumber)
    return IResponseBase(data=customer)

@app.put("/getCustomerByNumber/{customerNumber}", tags=["Customers"], response_model=IResponseBase[CustomersSchemas])
def updateCustomer(customerNumber: int, customerData: UpdateCustomerSchemas, db: Session = Depends(get_db)):
    customer = update_customers_by_id(db,customerNumber, customerData.model_dump())
    return IResponseBase(data=customer)