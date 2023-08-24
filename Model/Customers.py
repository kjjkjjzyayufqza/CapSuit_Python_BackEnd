from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, Integer, String,DECIMAL
from Routers.db import Base

# Define Customers Model, Same with database
class Customers(Base):
    __tablename__ = "customers"
    customerNumber = Column(Integer, primary_key=True, index=True)
    customerName = Column(String(50),nullable=False)
    contactLastName = Column(String(50),nullable=False)
    contactFirstName = Column(String(50),nullable=False)
    phone = Column(String(50),nullable=False)
    addressLine1 = Column(String(50),nullable=False)
    addressLine2 = Column(String(50),default=None)
    city = Column(String(50),nullable=False)
    state = Column(String(50),default=None)
    postalCode = Column(String(15),default=None)
    country = Column(String(50),nullable=False)
    salesRepEmployeeNumber = Column(Integer, ForeignKey('employees.employeeNumber'), default=None)
    creditLimit = Column(DECIMAL(10,2),default=None)
    __table_args__ = (
        ForeignKeyConstraint(['salesRepEmployeeNumber'], ['employees.employeeNumber'], name="customers_ibfk_1"),
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'latin1'}
    )
