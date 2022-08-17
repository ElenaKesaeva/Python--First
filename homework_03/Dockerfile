# 1. Собрать докер в текущей директории - docker build . -t app
# 2. Запуск контейнера - docker run -it app
# 3.Провести порт для запуска снаружи - docker run -p 8000:8000 -it app
# 4.Для открытия приложения в браузере набираем  - localhost:8000

FROM python:3.10-bullseye
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install poetry==1.1.14
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY app-home .

EXPOSE 8000
CMD uvicorn app_w:app --host=0.0.0.0 --port=8000