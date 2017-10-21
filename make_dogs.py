import random as random

# pull creds
from settings import mongo_url
# import driver
import pymongo
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
collection = db.test_collection
users = db.user_collection
dogs = db.dogs_collection

dog_names = [
    "Bella",
    "Lucy",
    "Daisy"
    "Lola",
    "Luna",
    "Molly",
    "Sadie",
    "Sophie",
    "Bailey",
    "Maggie",
    "Chloe",
    "Lily",
    "Stella",
    "Zoey",
    "Penny",
    "Roxy",
    "Coco",
    "Gracie",
    "Ruby",
    "Mia",
    "Zoe",
    "Ellie",
    "Nala",
    "Rosie",
    "Ginger",
    "Abby",
    "Lilly",
    "Piper",
    "Sasha",
    "Riley",
    "Pepper",
    "Lulu",
    "Emma",
    "Lady",
    "Layla",
    "Lexi",
    "Olive",
    "Annie",
    "Izzy",
    "Maya",
    "Maddie",
    "Dixie",
    "Princess",
    "Cali",
    "Millie",
    "Belle",
    "Ella",
    "Harley",
    "Honey",
    "Kona",
    "Charlie",
    "Willow",
    "Marley",
    "Roxie",
    "Cookie",
    "Scout",
    "Holly",
    "Minnie",
    "Winnie",
    "Angel",
    "Dakota",
    "Callie",
    "Missy",
    "Phoebe",
    "Hazel",
    "Athena",
    "Shelby",
    "Peanut",
    "Sugar",
    "Jasmine",
    "Ava",
    "Penelope",
    "Sandy",
    "Trixie",
    "Gigi",
    "Fiona",
    "Sydney",
    "Josie",
    "Cleo",
    "Mocha",
    "Leia",
    "Delilah",
    "Baby",
    "Harper",
    "Shadow",
    "Macy",
    "Pearl",
    "Allie",
    "Mila",
    "Heidi",
    "Bonnie",
    "Nina",
    "Grace",
    "Katie",
    "Lacey",
    "Gypsy",
    "Cocoa",
    "Nova",
    "Charlotte",
    "Xena"
]

dog_thumbnails = [
    "/static/img/sample_dogs/01f3e1c841cf3b864ea024d8eb0c7251--dog-pictures-animal-pictures.jpg",
    "/static/img/sample_dogs/630f0ef3f6f3126ca11f19f4a9b85243--dachshund-puppies-weenie-dogs.jpg",
    "/static/img/sample_dogs/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg",
    "/static/img/sample_dogs/bordercollie1.jpg",
    "/static/img/sample_dogs/Common-dog-behaviors-explained.jpg",
    "/static/img/sample_dogs/dog-1210559_960_720.jpg",
    "/static/img/sample_dogs/dog-bone.png",
    "/static/img/sample_dogs/dog-breed-selector-australian-shepherd.jpg",
    "/static/img/sample_dogs/file_23252_dogue-de-bordeaux-dog-breed.jpg",
    "/static/img/sample_dogs/German-Shepherd-Dog-1.jpg",
    "/static/img/sample_dogs/labrador-retriever1istock.jpg",
    "/static/img/sample_dogs/Natural-Dog-Law-2-To-dogs,-energy-is-everything.jpg",
    "/static/img/sample_dogs/pexels-photo-356378.jpeg",
    "/static/img/sample_dogs/scroll000.jpg",
    "/static/img/sample_dogs/scroll0011.jpg",
    "/static/img/sample_dogs/stock-photo-beagle-dog-in-front-of-a-white-background-76764031.jpg",
    "/static/img/sample_dogs/thul-571a0332-3d53-51bc-8189-e2a4771f3470.jpg",
    "/static/img/sample_dogs/wildlife-photography-pet-photography-dog-animal-159541.jpeg"
]

dog_breeds = [
    "poodle",
    "schnowzer",
    "Feeline"
]

dog_colors = [
    "brown",
    "blue",
    "asian",
    "whitest",
    "tan",
    "brown with spots",
    "kind of purpley",
    "steel blue"
]

dog_genders = ["male", "female"]

dog_bool = ["yes", "no"]

dog_ears = [
    "stand-up",
    "cropped",
    "folded"
]

def get_thumbnail():
    stop = len(dog_thumbnails)
    rand = random.randrange(0,stop)
    return dog_thumbnails[rand]

def get_breed():
    stop = len(dog_breeds)
    rand = random.randrange(0, stop)
    return dog_breeds[rand]

def get_id():
    return random.randrange(0,999999)

def get_color():
    stop = len(dog_colors)
    rand = random.randrange(0, stop)
    return dog_colors[rand]

def get_age():
    return random.randrange(0,15)

def get_date():
    day = random.randrange(1,31)
    month = random.randrange(1,12)
    year = random.randrange(1,2017)
    return "{}/{}/{}".format(month,day,year)

def get_height_weight():
    return random.randrange(5,69)

def get_bool(x):
    rand = random.randrange(0,1)
    if x == "bool":
        return dog_genders[rand]
    elif x == "gend":
        return dog_bool[rand]
def get_ears():
    stop = len(dog_ears)
    rand = random.randrange(0,stop)
    return dog_ears[rand]

def get_note():
    nouns = ("puppy", "pooch", "doggy dog", "monster", "service dog")
    verbs = ("ran", "vanished", "disappeared", "exploded", "stole away")
    adv = ("randomly", "vapidly", "foolishly", "merrily", "again")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    num = random.randrange(0,5)
    return "My {} {} {} {}.".format(adj[num],nouns[num],verbs[num],adv[num])




for name in dog_names:

    dogs.insert_one(
        {
        "_id": str(uuid.uuid4()),
        "dog_name": name,
        "thumbnail": get_thumbnail(),
        "breed": get_breed(),
        "id_chip": get_id(),
        "age": get_age(),
        "date_found": get_date(),
        "location_found": "Houston",
        "prim_color": get_color(),
        "sec_color": get_color(),
        "height": get_height_weight(),
        "weight": get_height_weight(),
        "gender": get_bool("gend"),
        "fix": get_bool("bool"),
        "collar": get_bool("bool"),
        "collar_color": get_color(),
        "ears": get_ears(),
        "eyes": get_color(),
        "notes": get_note()
        }
    )
