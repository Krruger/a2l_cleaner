from pydantic import BaseModel

class PatternGroupBase(BaseModel):
    name: str

class PatternGroupCreate(PatternGroupBase):
    pass

class PatternGroup(PatternGroupBase):
    id: int
    class Config:
        orm_mode = True


class PatternBase(BaseModel):
    value: str

class PatternCreate(PatternBase):
    group_id: int

class Pattern(PatternBase):
    id: int
    group_id: int
    class Config:
        orm_mode = True