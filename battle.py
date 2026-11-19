

from display import  display_fight_info# noqa: I001

from models import  Monster, Attack, Dead,Drop,Item
import random

def game_loop(team,monsters,items):
    
    score = 0
    while is_team_alive(team):
        monster = pick_new_monster(monsters)
        while not monster.is_dead() and is_team_alive(team) :
            events = monster_attack(team,monster)
            events += team_attack(team,monster,items)
            score += 1
            display_fight_info(alive_team(team),monster,events,is_team_alive(team),score)
    return score


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

    

def team_attack(team,monster,items):

    events = []
    
    for character in alive_team(team) :
        damages = monster.take_damage(character.atk)
        if monster.is_dead():
            events.append(Dead(monster,character))
            events.append(Drop(character,monster,drop_item(monster,team,items)))
            return events
        event = Attack(monster,character,damages)
        events.append(event)    
    return events

def drop_item(monster,team,items):
    rarity_dict = monster.rarity_dict
    item = pick_random_item(rarity_dict,items)
    item_instance = Item(**item)
    character = pick_alive_character(team)
    add_item(item_instance,character)
    return item_instance

def add_item(item,character):
    if character.is_item_pickable(item):
        character.add_item(item)
        item.is_picked = True


def pick_random_item(rarity_dict,items):
    rarity = pick_rarity(rarity_dict)
    item = pick_item(rarity,items)
    return item

def pick_item(rarity,items):
    print(items)
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
    

