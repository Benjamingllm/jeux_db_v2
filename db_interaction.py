from pymongo import MongoClient  # noqa: I001
from config import SCORE_COLLECTION,DB_NAME,SCORE_LIMIT
def open_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client[DB_NAME]
    return db


def close_database(db):
    db.client.close()

def get_database_items(db,collection):
    return list(db[collection].find({}, {"_id": 0}))
    





def save_score(score,pseudo,db):
    db[SCORE_COLLECTION].insert_one({
        "pseudo": pseudo,
        "score": score,
    })

def get_top_scores(db):
    filters = [
    {"$group": {"_id": "$pseudo", "score": {"$max": "$score"}}},
    {"$sort": {"score": -1}},
    {"$limit": SCORE_LIMIT},
    {"$project": {"_id": 0, "pseudo": "$_id", "score": 1}},
    ]
    return list(db["scores"].aggregate(filters))

