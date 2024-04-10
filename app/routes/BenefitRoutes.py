from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database_conn import get_db
from app.models.BenefitModel import Benefit
from app.schemas.BenefitSchema import BenefitRead
from app.services.BenefitServices import (
    get_benefit_by_id,
    get_all_benefits as service_get_all_benefits,
)

router = APIRouter(tags=["Benefit"])

@router.get("/benefits/{benefit_id}", response_model=BenefitRead)
def get_benefit(benefit_id: int, db: Session = Depends(get_db)):
    return get_benefit_by_id(db, benefit_id)

@router.get("/benefits", response_model=List[BenefitRead])
def get_all_benefits(db: Session = Depends(get_db)):
    return service_get_all_benefits(db)


