"""###################################### CLASSES ##################################

classe mob
    initialisation (pv, atk,defense,nom)
        on initialise les variables 

    prendre des dégats(montant)
        on enleve le maximum de : 1 et nombre de pv du montant d'ataque - la défense 
        si pv <=0:
            pv = 0

        
    est_mort
        retourner pv inferieur ou = a 0
"""

class Mob:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def take_damage(self,amount):
        damages = max(1, amount - self.defense)
        self.hp -= damages
        if self.hp < 0:
            self.hp = 0
        return damages


    def is_dead(self):
        return self.hp == 0

class Monster(Mob):
    def __init__(self, name, hp, atk, defense):
        super().__init__(name, hp, atk, defense)


class Character(Mob):
    def __init__(self, name, hp, atk, defense):
        super().__init__(name, hp, atk, defense)
        

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
