from sqlalchemy.orm import Session
from app.models.EmployeeModel import Employee
from app.schemas.EmployeeSchema import EmployeeCreate, EmployeeUpdate 
from app.enums.EmployeeTypes import EmployeeTypes

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def get_all_employees(db: Session):
    return db.query(Employee).all()

def create_employee(db: Session, employee_data: EmployeeCreate):
    employee = Employee(**employee_data.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def update_employee(db: Session, employee_id: int, update_data: EmployeeUpdate):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        update_data_dict = update_data.dict(exclude_unset=True)
        for key, value in update_data_dict.items():
            setattr(employee, key, value)
        db.commit()
        db.refresh(employee)
        return employee
    return None

def delete_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False

def get_employee_types():
    return EmployeeTypes.employeeTypeList()