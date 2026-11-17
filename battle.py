

from display import  display_events

from models import  Monster, Attack, Dead
import random


def game_loop(team,monsters):

    score = 0
    while len(alive_team(team))  > 0:
        monster = pick_new_monster(monsters)
        while not monster.is_dead() and len(alive_team(team))  > 0 :
            events = team_attack(team,monster)
            events.extend(monster_attack(team,monster))
            score += 1
            display_events(events)
    return score


def monster_attack(team,monster):
    events = []
    if not monster.is_dead():
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

    

def team_attack(team,monster):

    events = []

    for character in alive_team(team) :
        damages = monster.take_damage(character.atk)
        if monster.is_dead():
            event = Dead(monster,character)
            events.append(event)
            return events
        event = Attack(monster,character,damages)
        events.append(event)    
    return events


def alive_team(team):
    return [character for character in team if not character.is_dead()]

def pick_new_monster(monsters):
    random_monster = random.choice(monsters)
    monster_instance = Monster.create_from_dict(random_monster)
    return monster_instance
    

