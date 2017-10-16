import datetime
import os

import peewee
from playhouse.db_url import connect

# Connect To DB
DB = connect(
  os.environ.get(
    'DATABASE_URL',
    'postgres://localhost:5432/tornado_starter'
  )
)

# Base Data Model
class BaseModel (peewee.Model):
    class Meta:
        database = DB

class PersonModel(BaseModel):
    first_name = peewee.CharField(max_length=255)
    last_name = peewee.CharField(max_length=255)
    phone = peewee.CharField(null = True)
    email = peewee.CharField(unique = True)
    address = peewee.CharField(null = True)
    city = peewee.CharField(null = True)
    state = peewee.CharField(null = True)
    zip_code = peewee.CharField(null = True)
    created = peewee.DateTimeField(
        default = datetime.datetime.utcnow()
    )
    def __str__ (self):
        return self.email

# User Model
class User(PersonModel):
    username = peewee.CharField(null = False)
