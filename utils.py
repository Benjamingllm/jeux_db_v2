from pymongo import MongoClient

def open_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Game"]
    return db


def close_database():
    client = MongoClient("mongodb://localhost:27017")
    client.close()

def get_database_items(db,name):
    collection  = get_collection(db,name).find()
    items = []
    for item in collection:
        items.append(item) 
    return items




def get_collection(db,collection):
    return db[collection]

def save_score(score,pseudo,db):
    pass