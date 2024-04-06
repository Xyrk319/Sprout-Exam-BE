from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database_conn import engine, SessionLocal
from app.models import UserModel, RoleModel 
from app.routes import auth

UserModel.Base.metadata.create_all(bind=engine)
RoleModel.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
