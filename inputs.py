from config import MENU_CHOICE, PSEUDO, MENU
from utils import clear_screen
from questo import select as qselect
from yakh import get_key
from yakh.key import Keys
from display import build_menu_panel
MENU_KEYS = (Keys.UP_ARROW, Keys.DOWN_ARROW, Keys.ENTER, Keys.CTRL_C)


def get_valid_choice(options,extra_keys = None):
    return run_menu(
        qselect.SelectState(options=options),
        lambda state: build_menu_panel(state, MENU_CHOICE),
        extra_keys,
    )
    

def menu_input_handler(menu,extra_keys = None):
    extra_keys = extra_keys or {}
    while True:
        menu.state = calculate_state(menu.state, get_key(), extra_keys)
        if menu.state.abort:
            raise KeyboardInterrupt
        if menu.state.exit:
            return menu.result

def find_action(key,extra_keys):
    for extra_key, action in extra_keys.items():
        if key == extra_key:
            return action
    return None

def calculate_state(state,key,extra_keys):
    action = find_action(key,extra_keys)
    if action:    
        return action(state)
    if key in MENU_KEYS:
        return qselect.key_handler(state,key)
    return state


def run_menu(state, renderer, extra_keys=None):
    clear_screen()
    menu = qselect.Select(state, renderer=renderer)
    with menu.displayed():
        return menu_input_handler(menu, extra_keys)

def ask_pseudo():
    clear_screen()
    return input(PSEUDO)

def menu_input():
    input(MENU)

