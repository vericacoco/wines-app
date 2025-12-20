from fastapi import FastAPI
from app.database import wines_collection
from app.models import Wine

app = FastAPI(title="Wine Recommendation API")

@app.get("/")
def root():
    return {"status": "Wine API is running"}

@app.post("/wines")
def create_wine(wine: Wine):
    wines_collection.insert_one(wine.dict())
    return {"message": "Wine added successfully"}

@app.get("/wines")
def get_wines():
    wines = list(wines_collection.find({}, {"_id": 0}))
    return wines
