from app.database.seeders.BaseSeeder import BaseSeeder
from app.models.EmployeeModel import Employee
from app.models.BenefitModel import Benefit
from app.models.ProjectModel import Project
from app.enums.EmployeeTypes import EmployeeTypes as EmpType

class EmployeeSeeder(BaseSeeder):
    @staticmethod
    def seed():
        db = BaseSeeder.get_db_session()

        benefits = db.query(Benefit).all()
        projects = db.query(Project).all()
        
        employees = [
            {
                "first_name": "Test",
                "last_name": "Regular",
                "email": "test@regular.com",
                "number_of_leaves": 15,
                "contract_end_date": None,
                "employee_type": EmpType.REGULAR.value,
                "benefits": benefits[:3],
                "projects": []
            },
            {
                "first_name": "Test",
                "last_name": "Manager",
                "email": "test@manager.com",
                "number_of_leaves": 15,
                "contract_end_date": None,
                "employee_type": EmpType.REGULAR.value,
                "benefits": benefits,
                "projects": projects
            },
            {
                "first_name": "Test",
                "last_name": "Contract",
                "email": "test@contract.com",
                "number_of_leaves": 0,
                "contract_end_date": "2024-12-31",
                "employee_type": EmpType.CONTRACTUAL.value,
                "benefits": [],
                "projects": projects[-2:]
            }
        ]

        for employeeData in employees:
            employee = Employee(
                first_name=employeeData["first_name"],
                last_name=employeeData["last_name"],
                email=employeeData["email"],
                number_of_leaves=employeeData["number_of_leaves"],
                contract_end_date=employeeData["contract_end_date"],
                employee_type=employeeData["employee_type"]
            )

            for benefit in employeeData["benefits"]:
                employee.benefits.append(benefit)
            for project in employeeData["projects"]:
                employee.projects.append(project)

            db.add(employee)
        
        
        try:
            db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            db.rollback()
        finally:
            db.close()