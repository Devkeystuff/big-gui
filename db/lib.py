from datetime import date

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("sqlite:///gui.db", echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base(engine)
