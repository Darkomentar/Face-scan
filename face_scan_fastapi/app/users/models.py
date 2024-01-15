from sqlalchemy import JSON, Column, Integer, String
from app.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fio = Column(String, nullable=False)
    login = Column(String,  nullable=False)
    password = Column(String,  nullable=False)