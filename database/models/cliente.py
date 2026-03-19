from peewee import DateTimeField, Model, CharField
from database.database import db
import datetime

class Cliente(Model):
    name = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

