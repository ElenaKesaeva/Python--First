from sqlalchemy import Column, Integer, String

from homework_06.models import db


class Poem(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(1000), unique=True, nullable=False)
