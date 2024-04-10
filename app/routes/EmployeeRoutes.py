from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database_conn import get_db
from app.models.EmployeeModel import Employee
from app.schemas.EmployeeSchema import EmployeeCreate, EmployeeUpdate, EmployeeRead
from app.services.EmployeeServices import (
    get_employee_by_id,
    get_all_employees as service_get_all_employees,
    create_employee,
    update_employee,
    delete_employee,
    get_employee_types as service_get_employee_types,
)

router = APIRouter(tags=["Employee"])

@router.get("/employees/types", response_model=List)
def get_employee_types():
    return service_get_employee_types()

@router.get("/employees/{employee_id}", response_model=EmployeeRead)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    return get_employee_by_id(db, employee_id)

@router.get("/employees", response_model=List[EmployeeRead])
def get_all_employees(db: Session = Depends(get_db)):
    return service_get_all_employees(db)

@router.post("/employees", response_model=EmployeeRead)
def create(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, employee)

@router.put("/employees/{employee_id}", response_model=EmployeeRead)
def update(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    return update_employee(db, employee_id, employee)

@router.delete("/employees/{employee_id}")
def delete(employee_id: int, db: Session = Depends(get_db)):
    return delete_employee(db, employee_id)


