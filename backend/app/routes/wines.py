from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.database import wines_collection
from app.models import Wine

router = APIRouter(prefix="/wines")


@router.get("")
def get_wines(page: int = 1, limit: int = 5):
    skip = (page - 1) * limit

    wines = []
    for wine in wines_collection.find().skip(skip).limit(limit):
        wine["id"] = str(wine["_id"])
        del wine["_id"]
        wines.append(wine)

    total = wines_collection.count_documents({})

    return {
        "data": wines,
        "total": total,
        "page": page,
        "limit": limit
    }


@router.post("")
def add_wine(wine: Wine):
    result = wines_collection.insert_one(wine.dict())
    return {
        "id": str(result.inserted_id),
        **wine.dict()
    }


@router.put("/{wine_id}")
def update_wine(wine_id: str, wine: Wine):
    result = wines_collection.update_one(
        {"_id": ObjectId(wine_id)},
        {"$set": wine.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Wine not found")

    return {"message": "Wine updated"}


@router.delete("/{wine_id}")
def delete_wine(wine_id: str):
    result = wines_collection.delete_one({"_id": ObjectId(wine_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Wine not found")

    return {"message": "Wine deleted"}
