from pydantic import BaseModel

class SBeople(BaseModel):
    id: int
    fio: str

    class Config:
        orm_mode = True