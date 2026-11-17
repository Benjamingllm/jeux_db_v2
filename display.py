from db_interaction import get_top_scores


def display_numbered_options(options):
    for index,option in enumerate(options,start=1):
        print(f"{index} : {option}")


def format_character_info(characters):
    formated_characters = []
    for character in characters:
        string = f"nom : {character["nom"] }, pv : {character["pv"]}, attaque {character["attaque"]}, defense : {character["defense"]}"
        formated_characters.append(string)
    return formated_characters

def display_score(score):
    print(score)

def display_events(events):
    for event in events:
        print(event)

def display_error_message(message):
    print("⚠️" + message)

def display_leaderboard(db):
    scores = get_top_scores(db)
    for score in scores:
        print(f"{score["pseudo"]} : {score["score"] } score")

### Messages et input ####
MENU_CHOICE = "veuillez choisir une des options   "
PSEUDO = "Entrez votre pseudo"
QUIT = "appuyez sur entrer pour quitter"
CHOICE_ERROR = "Choix invalide"
