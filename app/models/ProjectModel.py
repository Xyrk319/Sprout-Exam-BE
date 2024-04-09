from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.Base import Base
from app.models.EmployeeModel import employee_project_association

class Project(Base):
    __tablename__ = "projects"

    name = Column(String(255), unique=True, index=True)
    employees = relationship("Employee", secondary=employee_project_association, back_populates="projects")
    