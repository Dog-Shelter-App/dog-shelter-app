from datetime import datetime

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
#   #   date_deleted
#FK #   user_id
#FK #   shelter_id

# users
#   #   _id
#   #   given_name
#   #   family_name
#   #   email
#   #   phones
#   #   type
#   #   avatar
#   #   date_created
#FK #   shelter_id


# shelters
#   #   _id
#   #   name
#   #   phone
#   #   email
#   #   address
#   #   city
#   #   state

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

def create_client():
    client = pymongo.MongoClient(mongo_url, ssl=True)
    if client:
        print("client working.")
    return client

client = create_client()

# imort UUID functionality

import uuid

def create_uuid():
    return str(uuid.uuid4())

db = client.test_database
# define collections
users = db.users
dogs = db.dogs
shelters = db.shelters
breeds = db.breeds





##########################
#### cluster
######## database
############ collection
################ document


######################################################
######################################################
# USER FUNCTIONS
######################################################
######################################################

def find_user_by_email(email):
    return users.find_one({"email": email})

def find_user_by_id(_id):
    return users.find_one({"_id": _id})

def find_all_users():
    return users.find({})

def add_new_user(data):
    # type & shelter auto set to not_set
    return users.insert_one(data)
def update_user_by_id(_id, data):
    return users.update_one({"_id": _id}, {'$set': data})

def update_user_by_email(email, data):
    return users.update_one({"email": email}, {'$set': data})

def delete_user_by_id(_id):
    return users.remove({"_id": _id})

def count_users():
    return users.find({}).count


def reset_kev():
    return users.update_one({"email": "houstonseosolutions@gmail.com"},{"$set": {
        "type": "not_set",
        "shelter_id": "not_set"
        }})

######################################################
######################################################
# DOG FUNCTIONS
######################################################
######################################################

def find_dog_by_id(_id):
    return dogs.find_one({"_id": _id})
def find_dog_by_name(name):
    return dogs.find_one({"name": name})
def find_all_dogs():
    return dogs.find({})
def find_deleted_dogs():
    return dogs.find({'delete': {'$ne': False} })
def find_all_public_dogs():
    return dogs.find({"delete":False})

def find_many_dogs(data):
    return dogs.find({"$and": data})

    # older version
    # return dogs.find({ "$or": data})

def add_new_dog(data):
    return dogs.insert_one(data)

def update_dog_by_id(_id, data):
    return dogs.update_one({"_id":_id}, {'$set': data })

def delete_dog_by_id(_id):
    return dogs.remove({"_id": _id})

def delete_many_dogs_by_date_range(start, stop):
    requests = [UpdateMany({'date_found':{'$gte': start, '$lt': stop}}, {'$set':{'delete':datetime.today()}})]

    dogs.bulk_write(requests)

    dogs_list = dogs.find({'date_found':{'$gte': start, '$lt': stop}})

    return dogs_list



def find_shelter_by_id(_id):
    return shelters.find_one({"_id": _id})
def find_shelter_by_name(name):
    return shelters.find_one({"name": name})
def find_all_shelters():
    return shelters.find({})

def add_new_shelter(data):
    return shelters.insert_one(data)

def update_shelter_by_id(_id, data):
    return shelters.update_one({"_id":_id}, {'$set': data })

def delete_shelter_by_id(_id):
    return shelters.remove({"_id": _id})


######################################################
######################################################
# IMAGE FUNCTIONS
######################################################
######################################################


# self.request.files['my_File'][0] is what you pass in as an argument

def upload_dog_image(my_File):
    file_all = my_File
    file_name = file_all['filename']
    file_body = file_all['body']

    import os

    file_path = os.path.join('static/img/dog_images/', file_name)
    if not os.path.exists('static/img/dog_images/'):
        os.makedirs('static/img/dog_images/')
    print(file_path)
    with open(file_path, 'wb') as f:
        f.write(file_body)
    f.closed

    return file_path
