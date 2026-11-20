
from config import RARITY_WEIGHTS_BY_LEVEL

class Mob:
    def __init__(self,name,hp,base_atk,defense):
        self.name = name
        self.hp = hp
        self.base_defense = defense
        self.defense = self.base_defense
        self.base_atk = base_atk
        self.atk = self.base_atk

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
    def __init__(self, name, hp, base_atk, defense,drop_level):
        super().__init__(name, hp, base_atk, defense)
        self.rarity_dict = RARITY_WEIGHTS_BY_LEVEL[drop_level]

    def __str__(self):
        return super().__str__()

    @classmethod
    def create_from_dict(cls, data):
        return super().create_from_dict(data,drop_level =data["niveau"])
        





class Character(Mob):
    def __init__(self, name, hp, base_atk, base_defense):
        super().__init__(name, hp, base_atk, base_defense)
        self.inventory = []

    def __str__(self):
        return super().__str__() 

    def add_item(self,item):
        self.atk += item.atk
        self.defense += item.defense
        self.inventory.append(item)



    def remove_item(self,item):
        self.defense -= item.defense
        self.atk -= item.atk
        self.inventory.remove(item)

    def can_recieve(self,item_type):
        for item in self.inventory:
            if item_type == item.type:
                return False
        return True


class Player:
    def __init__(self,score,name,inventory):
        self.score = score
        self.name = name
        self.inventory = inventory

    def add_item(self,item):
        self.inventory.append(item)

    def remove_item(self,item):
        self.inventory.remove(item)

    def can_recieve(self,item):
        return True

    

        
    

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
        return f"{self.item.name} a été dropé par {self.source.name} il a été ajouté a l'inventaire"
class Item:
    def __init__(self,name,type,rarity,atk,defense):
        self.name = name
        self.rarity = rarity
        self.atk = atk
        self.defense = defense
        self.type = type

    def __eq__(self, value):
        return isinstance(value, Item) and  self.name == value.name


class  InventoryView:
    def __init__(self, title,owner,target):

        self.title = title
        self.owner = owner
        self.target = target
        self.actions = {
            "switch" : (self.switch_item,"Entrer pour échanger avec l'item du meme type"),
            "equip" : (self.add_item,"Entrer pour équiper"),
            "unequip" : (self.add_item,"Entrer pour déséquiper")
        }

    def get_items(self):
        return self.owner.inventory

    def on_enter(self,item,action):
        self.actions[action][0](item)

    def add_item(self,item):
        self.target.add_item(item)
        self.owner.remove_item(item)

    def switch_item(self,item):
        item_to_switch = self.get_item_in_inventory(item,self.target)
        self.target.remove_item(item_to_switch)
        self.target.add_item(item)
        self.owner.remove_item(item)
        self.owner.add_item(item_to_switch)

    def is_item_switchable(self,item):
        return not self.target.can_recieve(item.type)

    def get_item_in_inventory(self,wanted_item,target):
        for item in target.inventory:
            if wanted_item.type == item.type:
                return item

"""i1 = Item("1","armure","legendaire",10,10)
i2 = Item("2","armure","legendaire",10,10)
o1 = Player(10,"player",[])
o2 = Character("char",10,10,10)

o1.add_item(i1)
o2.add_item(i2)
inv_view = InventoryView("test",o1,o2)
inv_view.switch_item(i1)
print(o1.inventory[0].name)
print(o2.inventory[0].name)
"""






        

    


