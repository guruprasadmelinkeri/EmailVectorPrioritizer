from sqlalchemy import Column, Integer, String, Boolean, Text
from .database import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    body = Column(Text)
    sender = Column(String)
    is_high_priority = Column(Boolean, default=False)
