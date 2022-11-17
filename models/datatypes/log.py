from dataclasses import dataclass
from datetime import datetime

import sqlalchemy as db
from dataclasses_json import dataclass_json

from db.lib import Base, engine


@dataclass_json
@dataclass
class Log(Base):
    id: int
    payload: str
    response: str
    created_at: datetime

    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    payload = db.Column(db.String)
    response = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now())

Base.metadata.create_all(engine)