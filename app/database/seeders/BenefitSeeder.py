from app.database.seeders.BaseSeeder import BaseSeeder
from app.models.BenefitModel import Benefit

class BenefitSeeder(BaseSeeder):
    @staticmethod
    def seed():
        db = BaseSeeder.get_db_session()
        
        benefits = [
            {
                "name": "HMO on DAY 1"
            },
            {
                "name": "Free Lunch"
            },
            {
                "name": "Birthday Cake"
            },
            {
                "name": "13th Month Payment"
            },
            {
                "name": "14th Month Payment"
            },
            {
                "name": "15th Month Payment"
            }
        ]

        for benefitData in benefits:
            benefit = Benefit(**benefitData)
            db.add(benefit)
        
        try:
            db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            db.rollback()
        finally:
            db.close()