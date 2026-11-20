TEAM_LENGTH = 3
CHARACTER_COLLECTION = "characters"
MONSTER_COLLECTION = "monsters"
DB_NAME = "Game"
SCORE_COLLECTION = "scores"
SCORE_LIMIT = 3
EVENT_TIME_GAP = 1
ROUND_TIME_GAP = 3
LEADERBOARD_STYLE = {"title" : "Leaderboard","style": "cyan","border_style" : "white"}
TEAM_PANEL_STYLE = {"title" : "team", "style" : "green1"}
MONSTER_PANEL_STYLE = {"title" : "monster", "style" : "red"}
EVENT_PANEL_STYLE = {"title" : "Déroulé du combat", "style" : "white"}
LOOSE_PANNEL_STYLE = {"style" : "bold red"}
ROUND_PANNEL_STYLE = {"style": "bold cyan"}
ITEM_COLLECTION = "items"
RARITY_WEIGHTS_BY_LEVEL = {
    1: {"commun": 0.80, "rare": 0.17, "épique": 0.03,  "légendaire": 0.00},
    2: {"commun": 0.65, "rare": 0.27, "épique": 0.07,  "légendaire": 0.01},
    3: {"commun": 0.50, "rare": 0.32, "épique": 0.14, "légendaire": 0.04},
    4: {"commun": 0.35, "rare": 0.35, "épique": 0.22, "légendaire": 0.08},
    5: {"commun": 0.00,  "rare": 0.45, "épique": 0.40, "légendaire": 0.15},
}

MENU_CHOICE = "veuillez choisir une des options"
PSEUDO = "Entrez votre pseudo"
MENU = "appuyez sur entrer pour revenir au menu"
LOOSE_MESSAGE = "Toute votre équipe est morte "
SELECTED_OPTION_STYLE = "[bold black on green1]"

MENU_PANEL_STYLE = {
    "border_style": "green1",
    "title_align": "left",                    
    "subtitle": "[dim]↑↓ · Entrée[/]",        
    "subtitle_align": "right",
    "padding": (1, 2),                        
    "expand": False,                          
}
STAT_PANEL_STYLE = { "style" : "green1"}
INVENTORY_ACTION_STYLE  = { "style" : "white"}

