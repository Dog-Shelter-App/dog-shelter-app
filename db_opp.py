# DATABASE SCHEMA

# dogs
#   #   _id
#   #   name
#   #   image
#   #   gender
#   #   fix
#   #   breed
#   #   location_found
#   #   date_found
#   #   prim_color
#   #   sec_color
#   #   height
#   #   weight
#   #   eye_color
#   #   ear_type
#   #   age
#   #   notes

# users
#   #   _id
#   #   given_name
#   #   family_name
#   #   email
#   #   phone
#   #   type
#   #   shelter
#   #   avatar
#   #   date_created

# shelters
#   #   _id
#   #   name
#   #   phone
#   #   email
#   #   address
#   #   city
#   #   state
#   #   user_list
#   #   #   #   user_id...

# breeds
#   #   _id
#   #   name






# pull creds
from settings import mongo_url
# import driver
import pymongo
from pymongo import UpdateMany
# import client function
from pymongo import MongoClient
# create client
client = pymongo.MongoClient(mongo_url, ssl=True)
# imort UUID functionality
import uuid

if client:
    print("client working.")
# define database
db = client.test_database

# define collections
users = db.users_collection
dogs = db.dogs_collection
shelters = db.shelters_collection
breeds = db.breeds_collection

##########################
#### cluster
######## database
############ collection
################ document

# USER FUNCTIONS

def find_user_by_email(email):
    return users.find_one({"email": email})

def find_user_by_id(id):
    return users.find_one({"_id": _id})

def find_all_users():
    return users.find({})

def add_new_user(data):
    # type & shelter auto set to not_set
    return users.insert_one(data)
def update_user_by_id(_id, data):
    return users.update_one({"_id": _id}, {'$set': data})


# DOG FUNCTIONS

def find_dog_by_id(_id):
    return dogs.find_one({"_id": _id})
def find_dog_by_name(name):
    return dogs.find_one({"name": name})
def find_all_dogs():
    return dogs.find({})

def add_new_dog():


def update_dog_by_id(_id, data):
    return dogs.update_one({"_id":_id}, {'$set': data })
