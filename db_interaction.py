from pymongo import MongoClient
from config import SCORE_COLLECTION,DB_NAME
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