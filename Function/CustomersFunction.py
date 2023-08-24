from typing import Optional
from fastapi import HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session
from Model.Customers import Customers
from Schemas.Customers import UpdateCustomerSchemas

def get_customers(db: Session, 
                  customerName: str,
                  contactLastName : str,
                  contactFirstName: str, 
                  creditLimitDesc: bool):
    # Create the query object
    query = db.query(Customers)

    # Create the conditions list
    # Because the function have a lot of conditions.
    conditions = []

    if customerName is not None:
        conditions.append(Customers.customerName.like(f"%{customerName}%"))
    if contactLastName is not None:
        conditions.append(Customers.contactLastName.like(f"%{contactLastName}%"))
    if contactFirstName is not None:
        conditions.append(Customers.contactFirstName.like(f"%{contactFirstName}%"))

    # Split the condition into a function
    # eg. query.filter(or_(Customers.customerName.like(f"%{customerName}%"))))
    if conditions:
        query = query.filter(or_(*conditions))
    
    if creditLimitDesc is not None:
        query = query.order_by(Customers.creditLimit.desc() if creditLimitDesc else Customers.creditLimit.asc())

    # Last return all the result
    return query.all()

def get_customers_by_id(db: Session, customerNumber: int):
    # First will Check the id is exists
    exists = db.query(Customers).filter(Customers.customerNumber == customerNumber).first()
    
    if exists is not None:
        return exists # If exists just return the result
    else:
        # If not item is equal, an error will be prompted
        raise HTTPException(status_code=404, detail="customerNumber not found")

def update_customers_by_id(db: Session,customerNumber: int, customerData: UpdateCustomerSchemas):
    # First will Check the id is exists
    exists = db.query(Customers).filter(Customers.customerNumber == customerNumber).first()
    
    if exists is not None:
        # If exists use the update command
        db.query(Customers).filter(Customers.customerNumber == customerNumber).update(customerData)
        # Submit changes
        db.commit()
        # Last return the result
        return db.query(Customers).filter(Customers.customerNumber == customerNumber).first()
    else:
        # If not item is equal, an error will be prompted
        raise HTTPException(status_code=404, detail="customerNumber not found")