from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017")

client = MongoClient(MONGO_URL)
db = client["wines_db"]

wines_collection = db["wines"]
users_collection = db["users"]
ratings_collection = db["ratings"]
