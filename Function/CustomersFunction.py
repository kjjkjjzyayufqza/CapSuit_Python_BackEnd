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
    
    query = db.query(Customers)

    conditions = []

    if customerName is not None:
        conditions.append(Customers.customerName.like(f"%{customerName}%"))
    if contactLastName is not None:
        conditions.append(Customers.contactLastName.like(f"%{contactLastName}%"))
    if contactFirstName is not None:
        conditions.append(Customers.contactFirstName.like(f"%{contactFirstName}%"))

    if conditions:
        query = query.filter(or_(*conditions))
    
    if creditLimitDesc is not None:
        query = query.order_by(Customers.creditLimit.desc() if creditLimitDesc else Customers.creditLimit.asc())

    return query.all()

def get_customers_by_id(db: Session, customerNumber: int):
    exists = db.query(Customers).filter(Customers.customerNumber == customerNumber).first()
    
    if exists is not None:
        return exists
    else:
        raise HTTPException(status_code=404, detail="customerNumber not found")

def update_customers_by_id(db: Session,customerNumber: int, customerData: UpdateCustomerSchemas):
    exists = db.query(Customers).filter(Customers.customerNumber == customerNumber).first()
    
    if exists is not None:
        db.query(Customers).filter(Customers.customerNumber == customerNumber).update(customerData)
        db.commit()
        return db.query(Customers).filter(Customers.customerNumber == customerNumber).first()
    else:
        raise HTTPException(status_code=404, detail="customerNumber not found")