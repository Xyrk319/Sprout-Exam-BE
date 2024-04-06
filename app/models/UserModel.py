from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database_conn import Base
from app.models.RoleModel import user_role_association  # Adjust the import path as necessary

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    roles = relationship("Role", secondary=user_role_association, back_populates="users")
