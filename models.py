
from config import RARITY_WEIGHTS_BY_LEVEL

class Mob:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.base_defense = defense
        self.defense = self.base_defense

    def take_damage(self,amount):
        damages = max(1, amount - self.defense)
        self.hp -= damages
        if self.hp < 0:  # noqa: PLR1730
            self.hp = 0
        return damages


    def is_dead(self):
        return self.hp == 0

    @classmethod
    def create_from_dict(cls,data,**extra):
        return cls(data["nom"],data["pv"],data["attaque"], data["defense"],**extra)

    def __str__(self):
        return f"{self.name} : {self.hp} pv"



class Monster(Mob):
    def __init__(self, name, hp, atk, defense,drop_level):
        super().__init__(name, hp, atk, defense)
        self.rarity_dict = RARITY_WEIGHTS_BY_LEVEL[drop_level]

    def __str__(self):
        return super().__str__()

    @classmethod
    def create_from_dict(cls, data):
        return super().create_from_dict(data,drop_level =data["niveau"])
        





class Character(Mob):
    def __init__(self, name, hp, atk, base_defense):
        super().__init__(name, hp, atk, base_defense)
        self.inventory = []

    def __str__(self):
        return super().__str__() 

    def add_item(self,item):
        self.atk += item.atk
        self.defense += item.defense
        self.inventory.append(item)

    def is_item_pickable(self,item):
        return item not in self.inventory


        
    

class Event:
    def __init__(self,target,source):
        self.target = target
        self.source = source

class Attack(Event):
    def __init__(self, target, source,damage):
        super().__init__(target, source)
        self.damage = damage
        self.hp = target.hp

    def __str__(self):
        return f"{self.source.name} inflige {self.damage} à {self.target.name}, il lui reste {self.hp} pv"

class Dead(Event):
    def __init__(self, target, source):
        super().__init__(target, source)

    def __str__(self):
        return f"{self.source.name} a tué {self.target.name}"

class Drop(Event):
    def __init__(self, target, source,item):
        super().__init__(target, source)
        self.item = item


    def __str__(self):
        if self.item.is_picked:
            string = f"{self.source.name} a dropé l'item {self.item.rarity} : {self.item.name}, {self.target.name} l'a ramassé"
        else:
            string = "tout vos personnages ont déja cet item il reste par terre"
        return string
class Item:
    def __init__(self,name,type,rarity,atk,defense):
        self.name = name
        self.rarity = rarity
        self.atk = atk
        self.defense = defense
        self.type = type
        self.is_picked = False

    def __eq__(self, value):
        return isinstance(value, Item) and self.name == value.name




