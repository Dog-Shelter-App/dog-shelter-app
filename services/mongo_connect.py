import pymongo
from pymongo import MongoClient


def connect():
    client = pymongo.MongoClient("mongodb://kevin:Bettyb00p!@cluster0-shard-00-00-fqbin.mongodb.net:27017,cluster0-shard-00-01-fqbin.mongodb.net:27017,cluster0-shard-00-02-fqbin.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
    db = client.test
