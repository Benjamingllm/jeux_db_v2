from display import MENU_CHOICE,PSEUDO,MENU,clear_screen # noqa: I001
from InquirerPy.base.control import Choice
from InquirerPy import inquirer


def get_valid_choice(options):
    clear_screen()
    choice = inquirer.select(
        message = MENU_CHOICE ,
        choices = [Choice(value = index, name = option) for index,option in enumerate(options)]
        ).execute()
    return int(choice)

def ask_pseudo():
    clear_screen()
    return input(PSEUDO)

def menu_input():
    input(MENU)