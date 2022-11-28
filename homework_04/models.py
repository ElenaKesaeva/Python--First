"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI")or"postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
async_engine: AsyncEngine = create_async_engine(
    PG_CONN_URI,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(bind=async_engine, cls=Base)
Session = async_session


class User(Base):
    name = Column(String(15), unique=True, nullable=False)
    username = Column(String(20), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    posts = relationship('Post', back_populates='user')


class Post(Base):

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, unique=False, nullable=False)
    body = Column(String, nullable=False, default="N/A")
    user = relationship('User', back_populates='posts')
