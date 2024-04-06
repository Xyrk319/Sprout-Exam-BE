from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database_conn import engine, SessionLocal
from app.models import UserModel, RoleModel 
from app.routes import authentication

UserModel.Base.metadata.create_all(bind=engine)
RoleModel.Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(authentication.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
