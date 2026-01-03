import os
from pymongo import MongoClient

MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB = os.getenv("MONGO_DB", "wines")

MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

print(f"Mongo URI: {MONGO_URI}")
print(f"Mongo DB: {MONGO_DB}")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
wines_collection = db["wines"]
