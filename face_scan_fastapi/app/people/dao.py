from app.dao.base import BaseDAO
from sqlalchemy import select
from app.database import gen_session
from app.people.models import People

class PeopleDAO(BaseDAO):
    model = People