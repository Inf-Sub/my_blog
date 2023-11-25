from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Table,
    Column
)

from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    relationship,
)
from config import engine

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False)


post_tag_table = Table(
    'post_tag_table',
    Base.metadata,
    Column('post_id', ForeignKey('post.id')),
    Column('tag_id', ForeignKey('tag.id'))
)


class Post(Base):
    __tablename__ = 'post'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String, nullable=False)
    content = mapped_column(String, nullable=False)
    user = mapped_column(Integer, ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    tags = relationship("Tag",secondary=post_tag_table, backref='posts')


class Tag(Base):
    __tablename__ = 'tag'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String, nullable=False)
    name = mapped_column(String, nullable=False)


def main():
    # Base.metadata.create_all(bind=engine)
    Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    main()
