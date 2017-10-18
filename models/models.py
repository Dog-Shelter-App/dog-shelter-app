import datetime
import os

import peewee as pw
from playhouse.db_url import connect




# Connect To DB
# DB = connect(os.environ.get('DATABASE') or 'dog-shelter-app.c1ga7ut5sy84.us-east-1.rds.amazonaws.com')

DB = pw.MySqlDatabase("mydb", host = "dog-shelter-app.c1ga7ut5sy84.us-east-1.rds.amazonaws.com", port=5432, user="dogshelteruser", passwd="dogshelterpw")

DB.connect()

# Base Data Model
class BaseModel (pw.Model):
    class Meta:
        database = DB

class PersonModel(BaseModel):
    first_name = pw.CharField(max_length=255)
    last_name = pw.CharField(max_length=255)
    phone = pw.CharField(null = True)
    email = pw.CharField(unique = True)
    address = pw.CharField(null = True)
    city = pw.CharField(null = True)
    state = pw.CharField(null = True)
    zip_code = pw.CharField(null = True)
    created = pw.DateTimeField(
        default = datetime.datetime.utcnow()
    )
    def __str__ (self):
        return self.email

# User Model
class User(PersonModel):
    username = pw.CharField(null = False)
