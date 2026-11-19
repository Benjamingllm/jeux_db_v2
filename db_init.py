from pymongo import MongoClient  # noqa: I001
from config import CHARACTER_COLLECTION, MONSTER_COLLECTION,DB_NAME,ITEM_COLLECTION
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
    {"nom": "La Courbature",                  "pv": 10, "attaque": 5, "defense": 4,  "niveau": 5},
    {"nom": "Les Pompes Enragées",            "pv": 50,  "attaque": 17,  "defense": 7,  "niveau": 1},
    {"nom": "L'Haltère Rouillée",             "pv": 50,  "attaque": 15,  "defense": 10, "niveau": 1},
    {"nom": "Le Burpee Maudit",               "pv": 55,  "attaque": 19,  "defense": 5,  "niveau": 1},
    {"nom": "Le Tapis de Course Emballé",     "pv": 60,  "attaque": 18,  "defense": 6,  "niveau": 2},
    {"nom": "Le Miroir Narcissique",          "pv": 65,  "attaque": 17,  "defense": 12, "niveau": 2},
    {"nom": "Le Vestiaire Puant",             "pv": 70,  "attaque": 16,  "defense": 9,  "niveau": 2},
    {"nom": "Le Squat Infernal",              "pv": 70,  "attaque": 21,  "defense": 10, "niveau": 3},
    {"nom": "La Traction Impossible",         "pv": 75,  "attaque": 18,  "defense": 14, "niveau": 3},
    {"nom": "Le Banc Possédé",                "pv": 85,  "attaque": 20,  "defense": 13, "niveau": 3},
    {"nom": "La Planche Éternelle",           "pv": 90,  "attaque": 15,  "defense": 16, "niveau": 4},
    {"nom": "Le Soulevé de Terre Titanesque", "pv": 95,  "attaque": 24,  "defense": 11, "niveau": 4},
    {"nom": "Le Coach Sadique",               "pv": 110, "attaque": 25,  "defense": 12, "niveau": 4},
])
def insert_items():
    items = db[ITEM_COLLECTION]
    items.insert_many([
    # ── Armes : surtout de l'attaque ──
    {"name": "Serviette Humide",           "type": "arme",   "rarity": "commun",     "atk": 3,  "defense": 0},
    {"name": "Shaker de Protéine",         "type": "arme",   "rarity": "commun",     "atk": 3,  "defense": 1},
    {"name": "Élastique de Résistance",    "type": "arme",   "rarity": "commun",     "atk": 4,  "defense": 1},
    {"name": "Corde à Sauter Fouettante",  "type": "arme",   "rarity": "rare",       "atk": 6,  "defense": 1},
    {"name": "Kettlebell de Poche",        "type": "arme",   "rarity": "rare",       "atk": 7,  "defense": 2},
    {"name": "Medecine Ball Explosif",     "type": "arme",   "rarity": "épique",     "atk": 9,  "defense": 2},
    {"name": "Barre Olympique Chromée",    "type": "arme",   "rarity": "épique",     "atk": 10, "defense": 3},
    {"name": "L'Haltère de Zeus",          "type": "arme",   "rarity": "légendaire", "atk": 14, "defense": 3},

    # ── Armures : surtout de la défense ──
    {"name": "Débardeur Troué",            "type": "armure", "rarity": "commun",     "atk": 0,  "defense": 3},
    {"name": "Legging Fluo",               "type": "armure", "rarity": "commun",     "atk": 1,  "defense": 3},
    {"name": "T-shirt Promo de la Salle",  "type": "armure", "rarity": "commun",     "atk": 0,  "defense": 4},
    {"name": "Sweat à Capuche Trempé",     "type": "armure", "rarity": "rare",       "atk": 1,  "defense": 6},
    {"name": "Ceinture de Force en Cuir",  "type": "armure", "rarity": "rare",       "atk": 2,  "defense": 7},
    {"name": "Combinaison de Compression", "type": "armure", "rarity": "épique",     "atk": 3,  "defense": 9},
    {"name": "Gilet Lesté Renforcé",       "type": "armure", "rarity": "épique",     "atk": 2,  "defense": 10},
    {"name": "L'Armure du Gainage Absolu", "type": "armure", "rarity": "légendaire", "atk": 3,  "defense": 14},
 
])
def insert_db():
    insert_characters()
    insert_monsters()
    insert_items()

def clear_db():
    db[CHARACTER_COLLECTION].delete_many({})
    db[MONSTER_COLLECTION].delete_many({})
    db[ITEM_COLLECTION].delete_many({})


clear_db()
insert_db()
