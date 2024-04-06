from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.Base import Base

# Associations or Relationships
user_role_association = Table('user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

class Role(Base):
    __tablename__ = 'roles'

    name = Column(String(30), unique=True, index=True)
    users = relationship("User", secondary=user_role_association, back_populates="roles")
