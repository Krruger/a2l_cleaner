from sqlalchemy.orm import Session
from passlib.context import CryptContext

import models
import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_group(db: Session, group: schemas.PatternGroupCreate):
    db_group = models.PatternGroup(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_groups(db: Session):
    return db.query(models.PatternGroup).all()

def get_patterns_by_group(db: Session, group_id: int):
    return db.query(models.SearchString).filter(models.SearchString.group_id == group_id).all()

def add_pattern_to_group(db: Session, pattern: schemas.PatternCreate):
    db_pattern = models.SearchString(value=pattern.value, group_id=pattern.group_id)
    db.add(db_pattern)
    db.commit()
    db.refresh(db_pattern)
    return db_pattern