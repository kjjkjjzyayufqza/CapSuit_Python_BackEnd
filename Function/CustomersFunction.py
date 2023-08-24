from typing import Optional
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from Model.Customers import Customers
from Schemas.Customers import UpdateCustomerSchemas

def get_customers(db: Session, 
                  customerName: str,
                  contactLastName : str,
                  contactFirstName: str, 
                  isDesc: Optional[bool]):
    
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
    
    if isDesc is not None:
        query = query.order_by(Customers.creditLimit.desc() if isDesc else Customers.creditLimit.asc())

    return query.all()

def get_customers_by_id(db: Session, customerNumber: int):
    return db.query(Customers).filter(Customers.customerNumber == customerNumber).first()

def update_customers_by_id(db: Session,customerNumber: int, customerData: UpdateCustomerSchemas):
    db.query(Customers).filter(Customers.customerNumber == customerNumber).update(customerData)
    db.commit()
    return db.query(Customers).filter(Customers.customerNumber == customerNumber).first()