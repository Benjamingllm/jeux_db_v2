from db_interaction import get_top_scores  # noqa: I001
from config import LEADERBOARD_STYLE,TEAM_PANEL_STYLE,MONSTER_PANEL_STYLE,EVENT_PANEL_STYLE,LOOSE_PANNEL_STYLE,ROUND_PANNEL_STYLE,MENU_PANEL_STYLE,LOOSE_MESSAGE,SELECTED_OPTION_STYLE,STAT_PANEL_STYLE,INVENTORY_ACTION_STYLE
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.console import Console
from rich.markup import escape

from utils import clear_screen
console = Console()

def format_character_info(characters):
    formated_characters = []
    for character in characters:
        string = f"nom : {character["nom"] }, pv : {character["pv"]}, attaque {character["attaque"]}, defense : {character["defense"]}"
        formated_characters.append(string)
    return formated_characters




def display_round(round):
    text = f"Round {round}"
    pannel = build_panel(ROUND_PANNEL_STYLE,text)
    return pannel
    


def display_leaderboard(scores):
    lines = []
    for score in scores:
        lines.append(f"{score["pseudo"]} : {score["score"] } points")
    text = "\n".join(lines)
    panel = build_panel(LEADERBOARD_STYLE,text)
    clear_screen()

    console.print(panel)

def build_fight_panel(*items,style):
    lines = []
    for item in items:
        lines.append(str(item))
    text = "\n".join(lines)
    
    return build_panel(style, text)

def build_stat_panel(character,title,deltas):
    lines = []
    for nom,valeur in vars(character).items():
        string = build_stat_string(nom,valeur,deltas)
        if string:
            lines.append(string)
    text =  "\n".join(lines)
    
    panel = build_panel({**STAT_PANEL_STYLE, "title": title},text)
    return panel

def build_stat_string(nom,valeur,deltas):
    string = None
    if nom == "inventory":
        return
    if deltas :
        string = build_deltas_string(nom,valeur,deltas)
    if not string:
        string = f"{nom} : {valeur},"
    return string

def build_deltas_string(nom,valeur,deltas):
    if nom == "atk":
        string = f"{nom}: {valeur} {deltas[0]}"
        return string
    if nom == "defense":
        string = f"{nom}: {valeur} {deltas[1]}"
        return string


def build_menu_panel(state,title):
    text = build_menu_text(state)
    return build_panel({**MENU_PANEL_STYLE, "title": title}, text)


def build_menu_text(state):
    lines = []
    for index, option in enumerate(state.options):
        text = option
        if index == state.index:
            lines.append(f"{SELECTED_OPTION_STYLE}{text}[/]")
        else:
            lines.append(text)
    text = "\n".join(lines)
    return text

def display_fight_info(team,monster,events,is_team_alive,score):
    clear_screen()

    if is_team_alive:

        display = [display_round(score ) , display_rounds_info(team,monster,events)]
    else:
        display = [display_loose(score)]
    
    console.print(*display)



def display_loose(score):
    score_text = f"Score : {score}"
    text = f"{LOOSE_MESSAGE}\n{score_text}"
    loose_pannel = build_panel(LOOSE_PANNEL_STYLE,text)
    return loose_pannel   


def display_rounds_info(team,monster,events):
    team_panel = build_fight_panel(*team, style = TEAM_PANEL_STYLE)
    monster_panel = build_fight_panel(monster, style = MONSTER_PANEL_STYLE)
    events_panel = build_fight_panel(*events, style = EVENT_PANEL_STYLE)
    grid = create_grid()
    pannels = [team_panel, events_panel, monster_panel]
    grid.add_row(*pannels)
    format_height(grid,pannels)
    return grid

def create_grid(*ratios):
    grid = Table.grid(expand=True)
    for ratio in ratios:
        grid.add_column(ratio=ratio)
    return grid

def build_panel(style,text):
    panel = Panel(Align.center(text,vertical = "middle"),**style,)
    return panel

def format_height(grid, pannels):
    height = len(console.render_lines(grid, console.options))
    for pannel in pannels:
        pannel.height = height

def build_inventory_screen(state,title,character,deltas,action_text):
    grid  = create_grid(1,1,1)
    view_panel = build_menu_panel(state,title)
    stats_panel = build_stat_panel(character,character.name,deltas)
    actions_panel = build_inventory_action(action_text)
    grid.add_row(view_panel, actions_panel,stats_panel)
    format_height(grid,[view_panel,stats_panel])
    return grid


def build_inventory_action(action):
    return build_panel(INVENTORY_ACTION_STYLE,action)




### Messages et message d'input ####

