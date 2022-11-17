from models.datatypes.log import Log
from utils.db_connection import DbConnection


def create_log(payload: str, response: str) -> bool:
    try:
        with DbConnection() as conn:
            query = Log(payload=payload, response=response)
            conn.add(query)
            res = conn.commit()
            print(res)
            return bool(res)
    except ValueError as e:
        print(e)