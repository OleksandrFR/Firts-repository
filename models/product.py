from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class Product:
    __tablename__='product'
    id=Column(Integer,primary_key=True)
    title=Column(String(100), nullable=False)
    price=Column(Integer, nullable=False)
    barcode=Column(String(100), nullable=False)
    count=Column(String, nullable=False)
    guarantee=Column(String, nullable=False)