import datetime
import os

<<<<<<< HEAD
import peewee as pw
=======
import peewee as peewee
>>>>>>> e3045b199f38cf66e3ecf00de291dc2fdd753a35
from playhouse.db_url import connect

# Connect To DB
<<<<<<< HEAD
# DB = connect(os.environ.get('DATABASE') or 'dog-shelter-app.c1ga7ut5sy84.us-east-1.rds.amazonaws.com')

DB = pw.MySqlDatabase("mydb", host = "dog-shelter-app.c1ga7ut5sy84.us-east-1.rds.amazonaws.com", port=5432, user="dogshelteruser", passwd="dogshelterpw")

DB.connect()
=======
# DB = connect(
#   os.environ.get(
#     'DATABASE_URL',
#     'postgres://localhost:5432/tornado_starter'
#   )
# )

myDB = peewee.MySQLDatabase("mydb", host="arn:aws:rds:us-east-1:956377352119:db:dog-shelter-app", port=54, user="dogshelteruser", passwd="dogshelterpw")

# db = PostgressqlDatabase(
#     'dog-shelter-app',
#     user='user',
#     password='12345',
#     host='db.mysite.com'
# )

# when you're ready to start querying, remember to connect
myDB.connect()
>>>>>>> e3045b199f38cf66e3ecf00de291dc2fdd753a35

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
