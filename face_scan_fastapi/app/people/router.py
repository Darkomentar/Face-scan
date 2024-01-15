from app.people.schemas import SBeople
from fastapi import APIRouter
from sqlalchemy import select
from app.database import gen_session
from app.people.models import People
from app.people.dao import PeopleDAO

router = APIRouter(
    prefix="/people", 
    tags=["Люди"]
    )

@router.get("")
async def get_peoples()-> list[SBeople]:
    return await PeopleDAO.find_all()
        



@router.get("/{people_id}")
async def get_people(people_id: int)-> SBeople:
    return await PeopleDAO.find_by_id(people_id)