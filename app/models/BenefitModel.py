from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.Base import Base
from app.models.EmployeeModel import employee_benefit_association

class Benefit(Base):
    __tablename__ = "benefits"

    name = Column(String(255), unique=True, index=True)
    employees = relationship("Employee", secondary=employee_benefit_association, back_populates="benefits")