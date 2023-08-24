from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv() # Load the .env file

# Load various parameters from env file
username = os.getenv('DB_username') 
password = os.getenv('DB_password') 
host = os.getenv('DB_host')
port = os.getenv('DB_port')     
database = os.getenv('DB_database')

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}/{database}?charset=latin1")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
