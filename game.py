

from db_interaction import get_database_items,save_score  # noqa: I001
from display import format_character_info,display_leaderboard,clear_screen
from battle import game_loop
from models import Character
from config import CHARACTER_COLLECTION,MONSTER_COLLECTION,ITEM_COLLECTION
from inputs import get_valid_choice, ask_pseudo,menu_input
from config import TEAM_LENGTH







def play(db):
    pseudo = ask_pseudo()
    characters = get_database_items(db,CHARACTER_COLLECTION)
    team = create_team(characters)
    monsters = get_database_items(db,MONSTER_COLLECTION)
    items = organized_items(db)
    score = game_loop(team,monsters,items)
    save_score(score,pseudo,db)
    menu_input()
    clear_screen()


def organized_items(db):
    raw_items = get_database_items(db,ITEM_COLLECTION)
    organized_items = {}
    for item in raw_items:
        rarity = item["rarity"]
        if rarity in organized_items:
            organized_items[rarity].append(item)
        else:
            organized_items[rarity] = [item]
    return organized_items






def create_team(characters):
    team = []
    remaining_options = list(characters)
    while team_not_full(team):
        choice = get_valid_choice(format_character_info(remaining_options)) 
        character_infos = remaining_options[choice]
        remaining_options.pop(choice)
        character = Character.create_from_dict(character_infos)
        team.append(character)
    return team

    
def team_not_full(team):
    return len(team) < TEAM_LENGTH



def leaderboard(db):
    display_leaderboard(db)
    menu_input()


 

