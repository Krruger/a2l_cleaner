from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.on_event("startup")
# def startup_populate():
#     db = SessionLocal()
#     if not db.query(models.SearchString).first():
#         db.add_all([
#             models.SearchString(value="FOO"),
#             models.SearchString(value="BAR"),
#             models.SearchString(value="TEST123")
#         ])
#         db.commit()
#     db.close()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    patterns = crud.get_patterns(db)
    filtered_lines = []

    for line in contents.decode().splitlines():
        if not any(p.value in line for p in patterns):
            filtered_lines.append(line)

    output_path = f"uploads/filtered_{file.filename}"
    with open(output_path, "w") as f:
        f.write("\n".join(filtered_lines))

    return {"filename": output_path}


@app.post("/groups/", response_model=schemas.PatternGroup)
def create_group(group: schemas.PatternGroupCreate, db: Session = Depends(get_db)):
    print("123")
    return crud.create_group(db, group)


@app.get("/groups/", response_model=list[schemas.PatternGroup])
def list_groups(db: Session = Depends(get_db)):
    return crud.get_groups(db)


@app.get("/patterns/{group_id}", response_model=list[schemas.Pattern])
def list_patterns(group_id: int, db: Session = Depends(get_db)):
    return crud.get_patterns_by_group(db, group_id)


@app.post("/patterns/", response_model=schemas.Pattern)
def add_pattern(pattern: schemas.PatternCreate, db: Session = Depends(get_db)):
    return crud.add_pattern_to_group(db, pattern)
