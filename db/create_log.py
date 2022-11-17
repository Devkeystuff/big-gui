from lib import Log

from ..models.payload import Log
from ..utils.db_connection import DbConnection


def create_log(payload: str, response: str) -> bool:
    try:
        with DbConnection() as conn:
            query = Log.insert().values(payload, response)
            
    except ValueError as e:
        print(e)