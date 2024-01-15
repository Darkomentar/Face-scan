from datetime import datetime
from pydantic import BaseModel

class SDetect_history(BaseModel):
    id:int
    id_people:int
    date_time:datetime
    photo:str


    class Config:
        orm_mode = True

class SDetect_history_for_site(BaseModel):
    id:int
    name_people:str
    date_time:datetime
    photo:str


    class Config:
        orm_mode = True