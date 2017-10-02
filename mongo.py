import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://kevin:Bettyb00p!@cluster0-shard-00-00-fqbin.mongodb.net:27017,cluster0-shard-00-01-fqbin.mongodb.net:27017,cluster0-shard-00-02-fqbin.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.test


# Create One Record
db.inventory.insert_one({"name":"Wade"})
# # Create Multiple Records
# db.inventory.insert_many([
#     {"name": "Kevin"},
#     {"name": "Mr.Mind"}
# ])

# Find https://docs.mongodb.com/manual/tutorial/query-documents/#read-operations-query-argument
# wade = db.inventory.find_and_modify(
#     {"name": "Wade"},
#     {$set: {"name":"Wadeskis"}}
# )

for doc in wade:
    print(doc)




# Update One Record
db.inventory.update_one(
    {"_id": "59d163498c3dc919ffd56bb7"},
    {$set:
        {
        "name": "Mr.Wade"
        }
    }
)
