from app.database.seeders.UserSeeder import UserSeeder
from app.database.seeders.RoleSeeder import RoleSeeder

def run_all():
    # RoleSeeder.seed()
    UserSeeder.seed()
