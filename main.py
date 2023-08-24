from typing import Union
from fastapi import FastAPI,Depends
from Function.CustomersFunction import get_customers, get_customers_by_id, update_customers_by_id
from Routers.db import get_db
from sqlalchemy.orm import Session
from Schemas.Customers import CustomersBasicSchemas, CustomersSchemas, UpdateCustomerSchemas
from Common.ResponseBase import IResponseBase

# Init the FastAPI
app = FastAPI()


# Define the router
# The main function of routing is to distinguish api methods
@app.get("/getCustomers", tags=["Customers"], # Distinguish between various users
         response_model=IResponseBase[list[CustomersBasicSchemas]], # Define the response format
         description="Get all customer from query") # Some Description
def getCustomers(customerName: Union[str, None] = None, # Optional parameters, Not mandatory
               contactLastName: Union[str, None] = None, 
               contactFirstName: Union[str, None] = None, 
               creditLimitDesc : bool = None,
               db: Session = Depends(get_db)): # Similar use of some special functions, In this case is use the yield for create a database session
    customers = get_customers(db,customerName,contactLastName,contactFirstName,creditLimitDesc)
    return IResponseBase(data=customers) # Use the custom response format

@app.get("/getCustomerByNumber/{customerNumber}", 
         tags=["Customers"], 
         response_model=IResponseBase[CustomersSchemas],
         description="Get customer by customerNumber")
def getCustomerById(customerNumber: int, 
                    db: Session = Depends(get_db)):
    customer = get_customers_by_id(db,customerNumber)
    return IResponseBase(data=customer)

@app.put("/updateCustomerByNumber/{customerNumber}", 
         tags=["Customers"], 
         response_model=IResponseBase[CustomersSchemas],
         description="Update customer data by customerNumber")
def updateCustomer(customerNumber: int, 
                   customerData: UpdateCustomerSchemas, 
                   db: Session = Depends(get_db)):
    customer = update_customers_by_id(db,customerNumber, customerData.model_dump())
    return IResponseBase(data=customer)