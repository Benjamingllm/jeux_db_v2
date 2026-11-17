

from db_interaction import open_database , close_database
from game import play,leaderboard, get_valid_choice
from sys import exit


        
OPTION_MENU = [
    ("Jouer", play),
    ("Voir le classement" , leaderboard),
    ("Quitter", lambda db : exit()),
]


def menu():
    while True :
        db = open_database()
        options = [texte for texte, fonction in OPTION_MENU]
        choice = get_valid_choice(options)
        OPTION_MENU[choice - 1 ][1](db)
        close_database(db)


if __name__ == "__main__" : menu()