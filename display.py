from db_interaction import get_top_scores  # noqa: I001
from time import sleep
from config import EVENT_TIME_GAP,ROUND_TIME_GAP

def display_numbered_options(options):
    for index,option in enumerate(options,start=1):
        print(f"{index} : {option}")


def format_character_info(characters):
    formated_characters = []
    for character in characters:
        string = f"nom : {character["nom"] }, pv : {character["pv"]}, attaque {character["attaque"]}, defense : {character["defense"]}"
        formated_characters.append(string)
    return formated_characters

def display_score(score):
    print(score)
    
def display_events(events):
    for event in events:
        print(event)
        sleep(EVENT_TIME_GAP)

def display_next_round(round):
    print(f'passage au round {round}')
    sleep(ROUND_TIME_GAP)


def display_error_message(message):
    print(f"⚠️ {message}" )

def display_monster_spawn(monster):
    print(f"{monster.name} apparait")

def display_leaderboard(db):
    scores = get_top_scores(db)
    for score in scores:
        print(f"{score["pseudo"]} : {score["score"] } points")

### Messages et message d'input ####
MENU_CHOICE = "veuillez choisir une des options   "
PSEUDO = "Entrez votre pseudo"
MENU = "appuyez sur entrer pour revenir au menu"
CHOICE_ERROR = "Choix invalide"
