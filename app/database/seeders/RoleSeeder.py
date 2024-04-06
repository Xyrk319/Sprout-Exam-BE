from app.database.seeders.BaseSeeder import BaseSeeder
from app.models.RoleModel import Role

class RoleSeeder(BaseSeeder):
    @staticmethod
    def seed():
        db = BaseSeeder.get_db_session()
        
        roles = [
            {
                "name": "admin"
            },
            {
                "name": "user"
            }
        ]

        for roleData in roles:
            role = Role(**roleData)
            db.add(role)
        
        try:
            db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            db.rollback()
        finally:
            db.close()