from pymongo import MongoClient

def open_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Game"]
    return db


def close_database(db):
    db.client.close()

def get_database_items(db,name):
    collection  = get_collection(db,name).find()
    items = []
    for item in collection:
        items.append(item) 
    return items




def get_collection(db,collection):
    return db[collection]

def save_score(score,pseudo,db):
    get_collection(db,"score").insert_one({
        "pseudo": pseudo,
        "score": score,
    })