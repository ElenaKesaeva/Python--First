# FROM tiangolo/uwsgi-nginx-flask:python3.9

# WORKDIR /homework_06

# COPY ./requirements.txt /app/requirements.txt
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY . /app

FROM tiangolo/uwsgi-nginx-flask:python3.9

WORKDIR /homework_06

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY . .