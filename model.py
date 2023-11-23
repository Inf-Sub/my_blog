from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import (
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship 
from config import engine

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db.init_app(app)


class User(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String, unique=True, nullable=False)
    email = mapped_column(String, nullable=False)


class Post(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String, nullable=False)
    content = mapped_column(String, nullable=False)
    user = mapped_column(Integer, ForeignKey(User.id), nullable=False)
    tags = relationship('Tag', back_populates='post')


class Tag(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String, nullable=False)
    post_id = mapped_column(ForeignKey(Post.id))
    post = relationship('Post', back_populates='tags')


with app.app_context():
    db.create_all()
    # db.drop_all()
