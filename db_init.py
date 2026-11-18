from pymongo import MongoClient  # noqa: I001
from config import CHARACTER_COLLECTION, MONSTER_COLLECTION,DB_NAME
client = MongoClient("mongodb://localhost:27017/")
db = client[DB_NAME]

def insert_characters():
    characters = db[CHARACTER_COLLECTION]
    characters.insert_many([
    {"nom": "Bruno le Bodybuilder",     "pv": 40, "attaque": 80, "defense": 14},
    {"nom": "Clara la Crossfiteuse",    "pv": 100, "attaque": 20, "defense": 12},
    {"nom": "Max le Powerlifter",       "pv": 110, "attaque": 28, "defense": 8},
    {"nom": "Yanis le Yogi",            "pv": 90,  "attaque": 18, "defense": 18},
    {"nom": "Léa la Coach Cardio",      "pv": 85,  "attaque": 22, "defense": 10},
    {"nom": "Hugo l'Haltérophile",      "pv": 105, "attaque": 26, "defense": 10},
    {"nom": "Inès la Boxeuse",          "pv": 90,  "attaque": 25, "defense": 9},
    {"nom": "Rémi le Rameur",           "pv": 100, "attaque": 21, "defense": 13},
    {"nom": "Sofia la Reine du Pilates", "pv": 88,  "attaque": 17, "defense": 17},
    {"nom": "Kévin le Débutant",        "pv": 80,  "attaque": 17, "defense": 11},
])


def insert_monsters():
    monsters = db[MONSTER_COLLECTION]
    monsters.insert_many([
    {"nom": "La Courbature",                  "pv": 300,  "attaque": 400, "defense": 4},
    {"nom": "Les Pompes Enragées",            "pv": 50,  "attaque": 17, "defense": 7},
    {"nom": "L'Haltère Rouillée",             "pv": 50,  "attaque": 15, "defense": 10},
    {"nom": "Le Burpee Maudit",               "pv": 55,  "attaque": 19, "defense": 5},
    {"nom": "Le Tapis de Course Emballé",     "pv": 60,  "attaque": 18, "defense": 6},
    {"nom": "Le Miroir Narcissique",          "pv": 65,  "attaque": 17, "defense": 12},
    {"nom": "Le Vestiaire Puant",             "pv": 70,  "attaque": 16, "defense": 9},
    {"nom": "Le Squat Infernal",              "pv": 70,  "attaque": 21, "defense": 10},
    {"nom": "La Traction Impossible",         "pv": 75,  "attaque": 18, "defense": 14},
    {"nom": "Le Banc Possédé",                "pv": 85,  "attaque": 20, "defense": 13},
    {"nom": "La Planche Éternelle",           "pv": 90,  "attaque": 15, "defense": 16},
    {"nom": "Le Soulevé de Terre Titanesque", "pv": 95,  "attaque": 24, "defense": 11},
    {"nom": "Le Coach Sadique",               "pv": 110, "attaque": 25, "defense": 12},
])


def insert_db():
    insert_characters()
    insert_monsters()

def clear_db():
    db[CHARACTER_COLLECTION].delete_many({})
    db[MONSTER_COLLECTION].delete_many({})

clear_db()
insert_db()