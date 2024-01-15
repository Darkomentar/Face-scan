from fastapi import APIRouter
from sqlalchemy import select
from app.database import gen_session
from app.detect_history.dao import Detect_historyDAO
from app.detect_history.schemas import SDetect_history, SDetect_history_for_site

router = APIRouter(
    prefix="/detect_history", 
    tags=["История"]
    )

@router.get("")
async def get_history()-> list[SDetect_history]:
    return await Detect_historyDAO.find_all()
        
@router.get("/get_history_find_top_n/{count}")
async def get_history_find_top_n(count:int)-> list[SDetect_history]:
    return await Detect_historyDAO.find_top_n(count)
        
@router.get("/get_history_find_last_n/{count}")
async def get_history_find_last_n(count:int)-> list[SDetect_history]:
    return await Detect_historyDAO.find_last_n(count)
        
@router.get("/find_last_n_with_names/{count}")
async def find_last_n_with_names(count:int)-> list[SDetect_history_for_site]:
    res = await Detect_historyDAO.find_last_n_with_names(limit=count)
    # print(res)
    return res



# @router.get("/{people_id}")
# async def get_people(people_id: int)-> SBeople:
#     return await Detect_historyDAO.find_by_id(people_id)