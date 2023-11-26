from sqlalchemy.orm import Session

from pytest import fixture

from model import User, Post, Tag

from config import engine

@fixture()
def db_session():
    with Session(engine) as session:
        yield session

    # session = Session(engine)
    # yield session
    # session.close()
    