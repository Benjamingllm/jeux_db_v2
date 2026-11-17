from pymongo import MongoClient

def open_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Game"]
    return db


def close_database():
    client = MongoClient("mongodb://localhost:27017")
    client.close()

def get_character(db):
    character_collection = "characters"
    characters_db = get_collection(db,character_collection).find()
    characters = []
    for character in characters_db:
        characters.append(character) 
    return characters


def get_collection(db,collection):
    return db[collection]