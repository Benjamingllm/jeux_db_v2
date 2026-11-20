from inputs import get_valid_choice
from display import build_menu_panel, build_inventory_screen
from questo import select as qselect
from inputs import run_menu
from yakh.key import Keys
from utils import format_names
from models import InventoryView


def open_menu(team,player):
    character = team[get_valid_choice(format_names(team))]
    views = [      
        InventoryView("Inventaire du joueur", player,character),
        InventoryView(character.name,character,player)
    ]
    InventoryMenu(views, character).run()






class InventoryMenu:
    def __init__(self, views,character):
        self.views = views
        self.current = 0
        self.items = views[0].get_items()
        self.character = character

    def switch_view(self, state):
        self.current = self.calculate_next_view_index()
        self.items = self.calculated_view().get_items()
        return qselect.SelectState(options=format_names(self.items))

    def calculate_next_view_index(self):
        return (self.current + 1) % len(self.views)
        
    def use_item(self,state):
        if not self.items:
            return state
        item = self.selected_item(state)
        view = self.calculated_view()
        view.on_enter(item)
        self.items = view.get_items()
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
                        self.render,
                        extra_keys)
    
    def selected_item(self,state):
        if not self.items or state.index is None:
            return None
        return self.items[state.index]

    def stat_delta(self,item):
        atk_delta = self.calculate_delta("atk",item)
        character_delta = self.calculate_delta("defense",item)
        deltas = (atk_delta,character_delta)
        return deltas

    def calculate_delta(self,stat,item):
        item_stat = getattr(item,stat)
        if self.calculated_view().title == self.character.name :
                return -item_stat
        return item_stat
        
    def render(self,state):
        item = self.selected_item(state)
        view  =  self.calculated_view()
        action_text = self.action_text(view)
        deltas = None
        if item:
            deltas = self.stat_delta(item)
        
        return build_inventory_screen(state, view.title, self.character,deltas,action_text)

    def calculated_view(self):
        return self.views[self.current]

    def action_text(self,view):
        if view.owner == self.character:
            return "Enter pour Deséquiper"
        return "Entrer pour Equiper"