import pymongo
from pymongo import MongoClient
import pprint

from settings import mongo_url
mongo_url = mongo_url

def Connect():
    client = pymongo.MongoClient(mongo_url)
    db = client.test


serverStatusResult=db.command("serverStatus")
print(serverStatusResult)
