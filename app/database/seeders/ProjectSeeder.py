from app.database.seeders.BaseSeeder import BaseSeeder
from app.models.ProjectModel import Project

class ProjectSeeder(BaseSeeder):
    @staticmethod
    def seed():
        db = BaseSeeder.get_db_session()
        
        projects = [
            {
                "name": "HRIS"
            },
            {
                "name": "Chatbot"
            },
            {
                "name": "Sprout AI Labs"
            },
            {
                "name": "Mobile App"
            },
        ]

        for projectData in projects:
            project = Project(**projectData)
            db.add(project)
        
        try:
            db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            db.rollback()
        finally:
            db.close()