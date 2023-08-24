from typing import Union
from fastapi import FastAPI
from fastapi import Depends
from Function.CustomersFunction import get_customers, get_customers_by_id, update_customers_by_id
from Model.Customers import Customers
from Routers.db import get_db
from sqlalchemy.orm import Session
from Schemas.Customers import CustomersBasicSchemas, CustomersSchemas, UpdateCustomerSchemas

app = FastAPI()

@app.get("/getCustomers", tags=["Customers"], response_model=list[CustomersBasicSchemas])
def getCustomers(customerName: Union[str, None] = None,
               contactLastName: Union[str, None] = None, 
               contactFirstName: Union[str, None] = None, 
               isDesc : bool = None,
               db: Session = Depends(get_db)):
    customers = get_customers(db,customerName,contactLastName,contactFirstName,isDesc)
    return customers

@app.get("/getCustomerByNumber/{customerNumber}", tags=["Customers"], response_model=CustomersSchemas | None)
def getCustomerById(customerNumber: int, db: Session = Depends(get_db)):
    customers = get_customers_by_id(db,customerNumber)
    return customers

@app.put("/getCustomerByNumber/{customerNumber}", tags=["Customers"], response_model=CustomersSchemas | None)
def updateCustomer(customerNumber: int, customerData: UpdateCustomerSchemas, db: Session = Depends(get_db)):
    customers = update_customers_by_id(db,customerNumber, customerData.model_dump())
    return customers