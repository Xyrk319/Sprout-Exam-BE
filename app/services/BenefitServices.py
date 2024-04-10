from sqlalchemy.orm import Session
from app.models.BenefitModel import Benefit

def get_benefit_by_id(db: Session, benefit_id: int):
    return db.query(Benefit).filter(Benefit.id == benefit_id).first()

def get_all_benefits(db: Session):
    return db.query(Benefit).all()