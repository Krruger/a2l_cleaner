from sqlalchemy.orm import Session
import models, schemas

def get_patterns(db: Session):
    return db.query(models.Pattern).all()

def create_pattern(db: Session, pattern: schemas.PatternCreate):
    db_pattern = models.Pattern(**pattern.dict())
    db.add(db_pattern)
    db.commit()
    db.refresh(db_pattern)
    return db_pattern
