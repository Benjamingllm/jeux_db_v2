from inputs import get_valid_choice

def open_menu(team):
    options = format_team(team)
    choice = get_valid_choice(options)
    open_character_menu(team[choice])

def format_team(team):
    formated_team = []
    for character in team:
        formated_team.append(character.name)
    return formated_team


def open_character_menu(character):
    pass