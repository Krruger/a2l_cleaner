from pydantic import BaseModel

class PatternBase(BaseModel):
    value: str

class PatternCreate(PatternBase):
    pass

class Pattern(PatternBase):
    id: int
    class Config:
        orm_mode = True
