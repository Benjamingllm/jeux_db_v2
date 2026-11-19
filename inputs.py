from config import MENU_CHOICE, PSEUDO, MENU
from utils import clear_screen
import readchar
from questo import select as qselect
from yakh import get_key
from yakh.key import Keys
from display import build_menu_panel
from readchar import key
MENU_KEYS = (Keys.UP_ARROW, Keys.DOWN_ARROW, Keys.ENTER, Keys.CTRL_C)


def get_valid_choice(options):
    clear_screen()
    menu = qselect.Select(
        qselect.SelectState(options=options),
        renderer=lambda state: build_menu_panel(state, MENU_CHOICE),
    )
    with menu.displayed():
        result = menu_input_handler(menu)
    return result

def menu_input_handler(menu):
    while True:
        key = get_key()
        if key not in MENU_KEYS:
            continue
        menu.state = qselect.key_handler(menu.state,key)
        if menu.state.abort:
            raise KeyboardInterrupt
        if menu.state.exit:
            return menu.result


def ask_pseudo():
    clear_screen()
    return input(PSEUDO)

def menu_input():
    input(MENU)

