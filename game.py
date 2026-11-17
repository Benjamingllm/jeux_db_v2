

from db_interaction import get_database_items,save_score
from display import display_score,format_character_info, PSEUDO, QUIT
from battle import game_loop
from models import Character
from config import CHARACTER_COLLECTION,MONSTER_COLLECTION
from inputs import get_valid_choice
from config import TEAM_LENGTH







def play(db):
    pseudo = input(PSEUDO)
    characters = get_database_items(db,CHARACTER_COLLECTION)
    team = create_team(characters)
    monsters = get_database_items(db,MONSTER_COLLECTION)
    score = game_loop(team,monsters)
    save_score(score,pseudo,db)
    display_score(score)
    input(QUIT)







def create_team(characters):
    team = []
    remaining_options = list(characters)
    while team_not_full(team):
        choice = get_valid_choice(format_character_info(remaining_options)) 
        character_infos = remaining_options[choice -1]
        remaining_options.pop(choice -1)
        character = Character.create_from_dict(character_infos)
        team.append(character)
    return team

    
def team_not_full(team):
    return len(team) < TEAM_LENGTH



def leaderboard():
    pass

 


"""



#################### CHOIX AFFICHER LES RESULTATS#########################
recupperer les 3meilleurs score 
afficher les 3 meilleurs score

proposer de cliquer sur une touche 
revenir au menu 

"""