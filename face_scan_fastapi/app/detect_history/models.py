from sqlalchemy import JSON, Column, ForeignKey, Integer, String, DateTime
from app.database import Base

class Detect_history(Base):
    __tablename__ = "detect_history"

    id = Column(Integer, primary_key=True)
    id_people = Column(ForeignKey("people.id"))
    date_time = Column(DateTime, nullable=False)
    photo = Column(String, nullable=False)
