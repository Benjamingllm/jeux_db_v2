

from display import  display_fight_info# noqa: I001
from utils import wait
from models import  Monster, Attack, Dead,Drop,Item
import random
from config import ROUND_TIME_GAP
from menu import open_menu


def game_loop(team,monsters,items,player):
    

    hotkeys = {"m": lambda: open_menu(team,player)}
    while is_team_alive(team):
        monster = pick_new_monster(monsters)
        while not monster.is_dead() and is_team_alive(team) :
            events = monster_attack(team,monster)
            events += team_attack(team,monster,items,player)
            player.score+=1
            display_fight_info(alive_team(team),monster,events,is_team_alive(team),player.score)
            wait(ROUND_TIME_GAP,hotkeys)



def monster_attack(team,monster):
    events = []
    if monster.is_dead():
        return []
    
    character = pick_alive_character(team)
    damages = character.take_damage(monster.atk)
    
    if character.is_dead():
        event = Dead(character,monster)
        events.append(event)
        return events

    event = Attack(character,monster,damages)
    events.append(event)
    return events




def pick_alive_character(team):
    return random.choice(alive_team(team))

    

def team_attack(team,monster,items,player):

    events = []
    
    for character in alive_team(team) :
        damages = monster.take_damage(character.atk)
        if monster.is_dead():
            events.append(Dead(monster,character))
            events.append(Drop(character,monster,drop_item(monster,player,items)))
            return events
        event = Attack(monster,character,damages)
        events.append(event)    
    return events

def drop_item(monster,player,items):
    rarity_dict = monster.rarity_dict
    item = pick_random_item(rarity_dict,items)
    item_instance = Item(**item)
    player.add_item(item_instance)
    return item_instance




def pick_random_item(rarity_dict,items):
    rarity = pick_rarity(rarity_dict)
    item = pick_item(rarity,items)
    return item

def pick_item(rarity,items):
    item_list = items[rarity]
    return random.choice(item_list)

def pick_rarity(rarity_dict):
    rarity_list = list(rarity_dict.keys())
    wheight = rarity_dict.values()
    return random.choices(rarity_list,weights= wheight)[0]



def alive_team(team):
    return [character for character in team if not character.is_dead()]

def is_team_alive(team):
    return len(alive_team(team)) > 0

def pick_new_monster(monsters):
    random_monster = random.choice(monsters)
    monster_instance = Monster.create_from_dict(random_monster)
    return monster_instance
    

