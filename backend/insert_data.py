import pymongo

client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client["mydb"]
collection = db["mycollection"]
collection.insert_many([
    {"name": "Sumit", "age": 25},
    {"name": "Sushmita", "age": 25}
])