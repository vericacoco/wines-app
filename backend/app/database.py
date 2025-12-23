from pymongo import MongoClient
import os
from urllib.parse import quote_plus

MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB = os.getenv("MONGO_DB", "wines")

MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

if MONGO_USER and MONGO_PASSWORD:
    username = quote_plus(str(MONGO_USER))
    password = quote_plus(str(MONGO_PASSWORD))
    mongo_url = f"mongodb://{username}:{password}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
else:
    mongo_url = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"

print("Mongo URL:", mongo_url)

client = MongoClient(mongo_url)
db = client[MONGO_DB]
wines_collection = db["wines"]
