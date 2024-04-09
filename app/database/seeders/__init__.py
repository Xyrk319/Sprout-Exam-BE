from app.database.seeders.UserSeeder import UserSeeder
from app.database.seeders.RoleSeeder import RoleSeeder
from app.database.seeders.BenefitSeeder import BenefitSeeder
from app.database.seeders.ProjectSeeder import ProjectSeeder
from app.database.seeders.EmployeeSeeder import EmployeeSeeder
def run_all():
    RoleSeeder.seed()
    UserSeeder.seed()
    BenefitSeeder.seed()
    ProjectSeeder.seed()
    EmployeeSeeder.seed()
