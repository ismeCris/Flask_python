from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Cliente(Model):
    # Changed to 'nome' to match your route, or update the route to 'name'
    nome = CharField() 
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db