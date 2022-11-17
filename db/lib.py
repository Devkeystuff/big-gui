import sqlalchemy as db

engine = db.create_engine("sqlite:///gui.db", echo=True)
meta = db.MetaData()

class Log(db.Table):
    id = db.Column(db.Integer, primary_key=True),
    payload = db.Column(db.String),
    response = db.Column(db.String),
    created_at = db.Column(db.DateTime)
