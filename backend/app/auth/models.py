from app.db.mongo import db

users_collection = db["users"]

def upsert_user(user: dict):
    users_collection.update_one(
        {"username": user["username"]},
        {"$set": user},
        upsert=True
    )

def get_user_by_username(username: str):
    return users_collection.find_one(
        {"username": username},
        {"_id": 0}
    )
