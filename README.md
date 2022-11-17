# Big GUI

Technical dept? We don't do that here.

School project GUI made with PySimpleGUI and SQLAlchemy.

## Installing

### Clone

    git clone git@github.com:Devkeystuff/python-gui.git

### Installing dependencies

> OPTIONAL: create virtual environment

```
python -m venv venv
source venv/bin/activate
```

    pip install -r requirements.txt

### Running locally

    python main.py

## Project structure

1. `api` contains all API call functions, in this case, only one.
2. `db` is responsible for connecting to db in `__init__.py` and the rest are queries to the db.
3. `models/eio` contains all types needed in communication with the GUI. Something similar to ECS.
4. `models/datatypes` are all types used by SQLAlchemy ORM to generate tables and write queries.
5. `utils` has some utility functions that could be seen reused many times in code. For example, `db_connection`, which is a neat way of connecting to DB using `with` statement.

### Tools used

1. [PySimpleGUI](https://www.pysimplegui.org/en/latest/) for creating the graphical interface in Python
2. [SQLAlchemy](https://www.sqlalchemy.org/) as ORM, mapping dataclasses to DB, and
3. [SQLite](https://www.sqlite.org/index.html) as the DB
