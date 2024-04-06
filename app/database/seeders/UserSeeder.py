from app.database.seeders.BaseSeeder import BaseSeeder
from app.models.UserModel import User
from app.models.RoleModel import Role

class UserSeeder(BaseSeeder):
    @staticmethod
    def seed():
        db = BaseSeeder.get_db_session()

        adminRole = db.query(Role).filter_by(name="admin").first()
        
        users = [
            {
                "username": "admin",
                "email": "admin@admin.com",
                "hashed_password": "admin",
                "roles": [adminRole]
            },
        ]

        for userData in users:
            user = User(
                username=userData["username"],
                email=userData["email"],
                hashed_password=userData["hashed_password"]
            )
            
            for role in userData["roles"]:
                user.roles.append(role)
            db.add(user)
        
        try:
            db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            db.rollback()
        finally:
            db.close()
