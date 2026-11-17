

from utils import open_database , close_database,get_database_items,save_score
from display import display_numbered_options, format_character_info,display_score, display_events
from sys import exit
from models import Character, Monster, Attack, Dead
import random
def main():
    while True :
        db = open_database()
        options = [texte for texte, fonction in OPTION_MENU]
        choice = get_valid_choice(options)
        OPTION_MENU[choice - 1 ][1](db)
        close_database(db)




def get_valid_choice(options):
    while True:
        display_numbered_options(options)
        choice = input("veuillez choisir une des options   ")
        if is_valid_choice(choice, 1, len(options)):
            return int(choice)
        print("Choix invalide")


def is_valid_choice(choice,minimum,maximum):
    validator = [
        lambda x: x.isdecimal(), 
        lambda x: minimum <= int(x) <= maximum,
    ]
    result = all(condition(choice) for condition in validator)
    return result





def play(db):
    pseudo = input("Entrez votre pseudo")
    characters = get_database_items(db,"characters")
    team = create_team(characters)
    monsters = get_database_items(db,"monsters")
    score = game_loop(team,monsters)
    save_score(score,pseudo,db)
    display_score(score)
    input("appuyez sur entrer pour quitter")
    return


def game_loop(team,monsters):

    score = 0
    while len(alive_team(team))  > 0:
        monster = pick_new_monster(extract_mob_info(monsters))
        while not monster.is_dead() and len(alive_team(team))  > 0 :
            events = team_attack(team,monster)
            events.extend(monster_attack(team,monster))
            score += 1
            display_events(events)
    return score


def monster_attack(team,monster):
    events = []
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
    return list(filter(lambda p: not p.is_dead(), team) )

def pick_new_monster(monsters):
    random_monster = random.choice(monsters)
    name, hp, atk, defense = random_monster.values()
    monster_instance = Monster(name,hp,atk,defense)
    return monster_instance
    






def create_team(characters):
    team = []
    remaining_options = extract_mob_info(characters)
    while team_not_full(team):
        choice = get_valid_choice(format_character_info(remaining_options)) 
        character_infos = remaining_options[choice -1]
        remaining_options.pop(choice -1)
        character = Character(character_infos["nom"],character_infos["pv"],character_infos["attaque"],character_infos["defense"])
        team.append(character)
    return team





        
def extract_mob_info(brut_information):
    infos = [
        {cle: valeur for cle, valeur in character.items() if cle != "_id"}
        for character in brut_information
    ]
    return infos





def team_not_full(team):
    return len(team) < TEAM_LENGHT



def leaderboard():
    pass

def quitt():
    exit()
    








OPTION_MENU = [
    ("Jouer", play),
    ("Voir le classement" , leaderboard),
    ("Quitter", lambda db : quitt()),
]
TEAM_LENGHT = 3


main()
    


"""



#################### CHOIX AFFICHER LES RESULTATS#########################
recupperer les 3meilleurs score 
afficher les 3 meilleurs score

proposer de cliquer sur une touche 
revenir au menu 

"""