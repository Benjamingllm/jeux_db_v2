from db_interaction import get_top_scores  # noqa: I001
from time import sleep
from config import ROUND_TIME_GAP,LEADERBOARD_STYLE,TEAM_PANEL_STYLE,MONSTER_PANEL_STYLE,EVENT_PANEL_STYLE,LOOSE_PANNEL_STYLE,ROUND_PANNEL_STYLE
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.console import Console

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
    
def clear_screen():
    print("\033[H\033[2J\033[3J")


def display_leaderboard(db):
    scores = get_top_scores(db)
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


def display_fight_info(team,monster,events,is_team_alive,score):
    clear_screen()

    if is_team_alive:

        display = [display_round(score ) , display_rounds_info(team,monster,events)]
    else:
        display = [display_loose(score)]
    
    console.print(*display)
    sleep(ROUND_TIME_GAP)



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

def create_grid():
    grid = Table.grid(expand=True)
    grid.add_column(ratio =1)
    grid.add_column(ratio =2)
    grid.add_column(ratio =1)
    return grid

def build_panel(style,text):
    panel = Panel(Align.center(text,vertical = "middle"),**style,)
    return panel

def format_height(grid, pannels):
    height = len(console.render_lines(grid, console.options))
    for pannel in pannels:
        pannel.height = height

### Messages et message d'input ####
MENU_CHOICE = "veuillez choisir une des options   "
PSEUDO = "Entrez votre pseudo"
MENU = "appuyez sur entrer pour revenir au menu"
LOOSE_MESSAGE = "Toute votre équipe est morte "
