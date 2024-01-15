from datetime import datetime
from app.dao.base import BaseDAO
from sqlalchemy import desc, select
from app.database import gen_session
from app.detect_history.models import Detect_history
from app.people.models import People
from app.detect_history.schemas import SDetect_history_for_site

class Detect_historyDAO(BaseDAO):
    model = Detect_history

    @classmethod
    async def find_last_n_with_names(cls, limit: int, **filter_by)->list[SDetect_history_for_site] :
            async with gen_session() as session:
                query = (select(Detect_history.id, People.fio, Detect_history.date_time, Detect_history.photo)
                .join(People, Detect_history.id_people == People.id).order_by(desc(Detect_history.id)).limit(limit))
        
               
                result = await session.execute(query)
                data = [{
                    'id': row[0],
                    'name_people': row[1],
                    'date_time': row[2],
                    'photo': row[3]
                } for row in result.all()]

                return data
    
    @classmethod
    async def add_new_detect_history(cls, id_people: int, date_time: datetime, photo: str):
        async with gen_session() as session:
            new_detect_history = Detect_history(
                id_people=id_people,
                date_time=date_time,
                photo=photo
            )
            session.add(new_detect_history)
            await session.commit()
            return new_detect_history

            

