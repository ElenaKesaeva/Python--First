"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users_data():
    async with ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:
            users_data = await response.json()
            return users_data


async def fetch_posts_data():
    async with ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as response:
            posts_data = await response.json()
            return posts_data




