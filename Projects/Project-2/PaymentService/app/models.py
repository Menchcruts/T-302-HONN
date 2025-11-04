from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, index=True)
    result = Column(String, nullable=False)