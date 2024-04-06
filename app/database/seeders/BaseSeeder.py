from app.database_conn import SessionLocal

class BaseSeeder:
    @staticmethod
    def seed():
        raise NotImplementedError("Seed method should be implemented")

    @staticmethod
    def get_db_session():
        return SessionLocal()
