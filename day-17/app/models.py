"""
models.py
---------
SQLAlchemy database models.
Defines the Employee table structure in the database.
"""

from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    email = Column(String, unique=True, nullable=False)