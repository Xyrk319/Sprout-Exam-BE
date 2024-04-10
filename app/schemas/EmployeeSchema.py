from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr, validator
from app.schemas.BenefitSchema import BenefitRead
from app.schemas.ProjectSchema import ProjectRead
from app.enums.EmployeeTypes import EmployeeTypes


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    number_of_leaves: int
    contract_end_date: datetime
    employee_type: int

class EmployeeUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    email: EmailStr = None
    number_of_leaves: int = None
    contract_end_date: datetime = None
    employee_type: int = None

class EmployeeRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    number_of_leaves: int
    contract_end_date: Optional[datetime] = None
    employee_type: int
    benefits: List[BenefitRead] = []
    projects: List[ProjectRead] = []

    class Config:
        orm_mode = True