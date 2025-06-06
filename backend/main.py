from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import os

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

@app.post("/pattern/", response_model=schemas.Pattern)
def create_pattern(pattern: schemas.PatternCreate, db: Session = Depends(get_db)):
    return crud.create_pattern(db, pattern)

@app.get("/patterns/", response_model=list[schemas.Pattern])
def read_patterns(db: Session = Depends(get_db)):
    return crud.get_patterns(db)
