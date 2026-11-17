from display import display_numbered_options, display_error_message,CHOICE_ERROR,MENU_CHOICE
from verif import is_valid_choice

def get_valid_choice(options):
    while True:
        display_numbered_options(options)
        choice = input(MENU_CHOICE)
        if is_valid_choice(choice, 1, len(options)):
            return int(choice)
        display_error_message(CHOICE_ERROR)



