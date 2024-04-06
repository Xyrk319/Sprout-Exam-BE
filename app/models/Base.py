# app/models/base.py
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr

class CustomBase:
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Timestamps
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Soft deletion
    deleted_at = Column(DateTime, nullable=True)

    # Generate table names automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

Base = declarative_base(cls=CustomBase)
