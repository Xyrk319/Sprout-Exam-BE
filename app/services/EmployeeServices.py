from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.EmployeeModel import Employee
from app.models.ProjectModel import Project
from app.models.BenefitModel import Benefit
from app.schemas.EmployeeSchema import EmployeeCreate, EmployeeUpdate 
from app.enums.EmployeeTypes import EmployeeTypes
from typing import List

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def get_all_employees(db: Session):
    return db.query(Employee).all()

def create_employee(db: Session, employee_data: EmployeeCreate):
    if db.query(Employee).filter(Employee.email == employee_data.email).first():
        raise HTTPException(status_code=400, detail="Email already exists!")

    # Extract IDs
    benefit_ids = [benefit.id for benefit in employee_data.benefits]
    project_ids = [project.id for project in employee_data.projects]
    
    benefits = db.query(Benefit).filter(Benefit.id.in_(benefit_ids)).all() if benefit_ids else []
    projects = db.query(Project).filter(Project.id.in_(project_ids)).all() if project_ids else []

    # Prepare the employee data excluding the benefits and projects to avoid errors
    employee_info = employee_data.dict(exclude={"benefits", "projects"})
    
    # Create the Employee object
    employee = Employee(**employee_info, benefits=benefits, projects=projects)

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee

def update_employee(db: Session, employee_id: int, update_data: EmployeeUpdate):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return None

    update_data_dict = update_data.dict(exclude_unset=True)
    benefits_ids = update_data_dict.pop("benefits", None)
    projects_ids = update_data_dict.pop("projects", None)

    for key, value in update_data_dict.items():
        setattr(employee, key, value)

    if benefits_ids is not None:
        benefits_ids_list = [benefit['id'] for benefit in benefits_ids]
        employee.benefits = get_benefits_by_ids(db, benefits_ids_list)

    if projects_ids is not None:
        projects_ids_list = [project['id'] for project in projects_ids]
        employee.projects = get_projects_by_ids(db, projects_ids_list)

    db.commit()
    db.refresh(employee)

    return employee

def get_benefits_by_ids(db: Session, ids: List[int]):
    return db.query(Benefit).filter(Benefit.id.in_(ids)).all()

def get_projects_by_ids(db: Session, ids: List[int]):
    return db.query(Project).filter(Project.id.in_(ids)).all()
def delete_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False

def get_employee_types():
    return EmployeeTypes.employeeTypeList()