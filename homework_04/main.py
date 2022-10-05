"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import async_engine, Base, User, Post, Session


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: AsyncSession, user: dict):
    user = User(username=user["username"], email=user["email"],
                name=user["name"], id=user["id"])

    session.add(user)


async def create_posts(session: AsyncSession, post: dict):

    post = Post(user_id=post["userId"], title=post["title"],
                body=post["body"])

    session.add(post)


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    async with Session() as session:
        async with session.begin():
            for user in users_data:
                await create_users(session, user)
            for post in posts_data:
                await create_posts(session, post)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

