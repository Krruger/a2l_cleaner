from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Pattern(Base):
    __tablename__ = "patterns"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String, unique=True, index=True)

class PatternGroup(Base):
    __tablename__ = "pattern_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    patterns = relationship("SearchString", back_populates="group")


class SearchString(Base):
    __tablename__ = "search_strings"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
    group_id = Column(Integer, ForeignKey("pattern_groups.id"))

    group = relationship("PatternGroup", back_populates="patterns")
