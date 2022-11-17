from models.datatypes import Log
from utils.db_connection import DbConnection


def get_all_logs() -> list[Log] | None:
    try:
        with DbConnection() as conn:
            all_logs = conn.query(Log).all()
            return all_logs
    except ValueError as e:
        print(e)