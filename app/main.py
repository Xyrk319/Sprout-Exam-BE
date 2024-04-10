from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database_conn import engine, SessionLocal
from app.models import UserModel, RoleModel 
from app.routes import auth, EmployeeRoutes

UserModel.Base.metadata.create_all(bind=engine)
RoleModel.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(EmployeeRoutes.router)
# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
