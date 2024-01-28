from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, ForeignKey

from datetime import datetime



Base = declarative_base()


class Check:
    __tablename__='product'
    id=Column(Integer, primaty_key=True)
    time=Column(DateTime(), default=datetime.now)
    items=Column(Integer, ForeignKey('product.id'))
    amount=Column(Integer, nullable=False)