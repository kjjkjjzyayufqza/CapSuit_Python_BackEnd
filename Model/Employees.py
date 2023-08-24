from sqlalchemy import Column, ForeignKeyConstraint, Integer, String,DECIMAL

class Employees:
    __tablename__ = "employees"
    employeeNumber = Column(Integer, primary_key=True, index=True)
    lastName = Column(String(50),nullable=False)
    firstName = Column(String(50),nullable=False)
    extension = Column(String(50),nullable=False)
    email = Column(String(50),nullable=False)
    officeCode = Column(String(50),nullable=False)
    reportsTo = Column(String(50),default=None)
    jobTitle = Column(String(50),nullable=False)
    state = Column(String(50),default=None)
    postalCode = Column(String(15),default=None)
    country = Column(String(50),nullable=False)
    salesRepEmployeeNumber = Column(Integer,default=None)
    creditLimit = Column(DECIMAL(10,2),default=None)
    ForeignKeyConstraint(
        ["salesRepEmployeeNumber"], ["employees.employeeNumber"], name="customers_ibfk_1"
    )
    mariadb_engine="InnoDB"

