from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    item = Column(String)
    vendor = Column(String)
    qty = Column(Integer)
    price = Column(Float)