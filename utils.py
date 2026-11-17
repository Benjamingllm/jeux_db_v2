from pymongo import MongoClient

def open_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Game"]
    return db


def close_database():
    client = MongoClient("mongodb://localhost:27017")
    client.close()