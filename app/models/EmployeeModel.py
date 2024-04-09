from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.Base import Base

employee_project_association = Table('employee_projects', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)

employee_benefit_association = Table('employee_benefits', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('benefit_id', Integer, ForeignKey('benefits.id'))
)
class Employee(Base):
    __tablename__ = "employees"

    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    number_of_leaves = Column(Integer, nullable=True)
    contract_end_date = Column(DateTime,nullable=True)
    employee_type = Column(Integer)
    benefits = relationship ("Benefit", secondary=employee_benefit_association, back_populates="employees")
    projects = relationship("Project", secondary=employee_project_association, back_populates="employees")