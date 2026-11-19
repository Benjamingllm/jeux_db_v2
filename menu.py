from inputs import get_valid_choice
from display import build_menu_panel
from questo import select as qselect
from inputs import run_menu
from yakh.key import Keys
from utils import format_names
from models import InventoryView


def open_menu(team,player):
    character = team[get_valid_choice(format_names(team))]
    views = [      
        InventoryView("Sac du joueur", player,character),
        InventoryView(character.name,character,player)
    ]
    InventoryMenu(views).run()






class InventoryMenu:
    def __init__(self, views):
        self.views = views
        self.current = 0
        self.items = views[0].get_items()

    def switch_view(self, state):
        self.current = (self.current + 1) % len(self.views)
        self.items = self.views[self.current].get_items()
        return qselect.SelectState(options=format_names(self.items))

    def use_item(self,state):
        if not self.items:
            return state
        item = self.items[state.index]
        self.views[self.current].on_enter(item)
        self.items = self.views[self.current].get_items()
        index = max(min(state.index, len(self.items) - 1), 0)
        return qselect.SelectState(options=format_names(self.items), index=index)

    def quit_menu(self,state):
        return qselect.SelectState(options=state.options, index=None, exit=True)

    def run(self):
        extra_keys = {
        Keys.LEFT_ARROW: self.switch_view,      
        Keys.RIGHT_ARROW: self.switch_view,
        Keys.ENTER: self.use_item,              
        Keys.ESC: self.quit_menu,               
        }
        return run_menu(qselect.SelectState(options=format_names(self.items)),
                        lambda state: build_menu_panel(state,self.views[self.current].title),
                        extra_keys)

    
