from fastapi import FastAPI, HTTPException, Depends
import models
from database import SessionLocal, engine
from pydantic import BaseModel
from sqlalchemy.orm import Session



models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserBase(BaseModel):
    username:str

app = FastAPI()

@app.post("/add-user")
def add_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users")
def get_users(db:Session=Depends(get_db)):
    users = db.query(models.User).all()
    return {"users": users}
