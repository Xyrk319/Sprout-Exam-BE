from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import UserModel
from app.database_conn import SessionLocal
from app.auth import auth_utils  # Assuming you have utility functions for auth

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register/")
def register_user(user_create: UserModel.UserCreate, db: Session = Depends(get_db)):  # Assuming UserCreate is a Pydantic model
    # Add registration logic here
    pass

@router.post("/login/")
def login(user_cred: UserModel.UserLogin, db: Session = Depends(get_db)):  # Assuming UserLogin is a Pydantic model
    # Add login logic here
    pass
