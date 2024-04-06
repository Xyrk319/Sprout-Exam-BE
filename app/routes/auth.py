from ..schemas.LoginSchema import LoginSchema
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database_conn import get_db
from ..schemas.UserSchema import UserCreate, UserToken
from ..services.AuthServices import register, login

router = APIRouter(tags=["Authentication"])

@router.post("/register", response_model=UserToken)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    
    return register(user, db)

@router.post("/login")
async def login_for_access_token(form_data: LoginSchema, db: Session = Depends(get_db)):
    return await login(form_data, db)
