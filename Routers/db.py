from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = 'root'     # 資料庫帳號
password = 'for-root-test-only'     # 資料庫密碼
host = 'localhost'    # 資料庫位址
port = '3306'         # 資料庫埠號
database = 'classicmodels'   # 資料庫名稱

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}/{database}?charset=latin1")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
