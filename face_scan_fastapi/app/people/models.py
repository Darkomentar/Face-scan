from sqlalchemy import JSON, Column, Integer, String
from app.database import Base

class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    fio = Column(String, nullable=False)
