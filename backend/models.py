from sqlalchemy import Column, Integer, String
from database import Base

class Pattern(Base):
    __tablename__ = "patterns"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String, unique=True, index=True)
