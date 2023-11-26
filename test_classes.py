from sqlalchemy import select

from model import User, Post, Tag

def test_post_amount(db_session):
    result = db_session.scalars(select(Post).where(Post.user==1)).all()
    assert len(result) == 2

def test_user_amount(db_session):
    result = result = db_session.scalars(select(User)).all()
    assert len(result) == 5

def test_user_names(db_session):
    result = db_session.scalars(select(User)).all()
    assert result[0].username == 'AmazingSam'
    assert result[1].username == 'ValueableJohn'
    assert result[2].username == 'CuriousDave'
    assert result[3].username == 'JellySally'
    assert result[4].username == 'IncredibleLarry'

def test_posts_with_tag(db_session):
    statement = select(Post).where(Post.tags.any(title = 'genres history'))
    result = db_session.scalars(statement).all()
    assert len(result) == 4

def test_posts_with_tag2(db_session):
    statement = select(Post).where(Post.tags.any(title = 'genres history'))
    result = db_session.scalars(statement).all()
    # assert len(result) == 4