

from utils import open_database , close_database
from display import display_numbered_options


def main():
    while True :
        open_database()
        choice = get_valid_choice(OPTION_MENU)
        OPTION_MENU[choice][1]()
        close_database()

def play():
    pass

def leaderboard():
    pass

def quitt():
    pass

OPTION_MENU = [
    ("Jouer", play),
    ("Voir le classement" , leaderboard),
    ("Quitter", quitt),
]

def get_valid_choice(options):
    while True:
        display_numbered_options(texte for texte, fonction in OPTION_MENU)
        choice = input("veuillez choisir une des options   ")
        if is_valid_choice(choice, 1, len(options)):
            return int(choice)
        print("Choix invalide")


def is_valid_choice(choice,minimum,maximum):
    validator = [
        lambda x: x.isdecimal(), 
        lambda x: minimum <= int(x) <= maximum,
    ]
    result = all(condition(choice) for condition in validator)
    return result


main()


"""




#################### CHOIX LANCER JEUX #########################

#demander pseudo
personnages recuperer les personnages
#recuperer les choix de personnages du joueurs parmis plusieures options
    team = []
    options restantes = list(personanges)
    tant que l'équipe n'est pas pleine
        recuperer le choix du joueur parmis la liste d'options restante
        enlever le personnage des options restantes
        créer une instance du personnage
        ajouter dans la team

monstres = recuperer les monstres
#score =  boucle de jeux
sauvegarde score
#afficher le score 
#proposer de cliquer sur une touche
# retourner rien( pour stop la fonction et continuer dans la boucle menu )

####


recuperer les monstres
    recuperer les monstres dans la db 
    les stocker dans une liste 
    les retourner

recup les personnages
    recuperer les personnages dans la db 
    les stocker dans une liste 
    les retourner




choisir un monstre au hasard
    on prend un monstre au hasard
    on crée une nouvelle instance de monstre et on la retourne

    



#### boucle de jeux ####
    boucle de jeux
    score = 0
    tant que la team n'est pas morte :
        choisir un nouveau monstre
        tant que le monstre n'es pas mort :
            event = attaque equipe
            ajouter attaque monstre a event
            score += 1
            afficher les event

    retourner score


#team morte 
    pour personnages dans la team:
        si personanges est vivant
        retourner false
    retourner vrai 



    
    


attaque equipe
    event = []
    pour personnage dans la team:
        personnage attaque le monstre 
        ajouter l'event a la liste
        si monstre est mort :
            ajouter l'event a la liste
            break
    retourner event 

attaque monstre :
    event = []
    choisi un personnage vivant 
    le monstre attaque le personnage
    ajouter l'event a la liste
    si le personnage est mort :
        ajouter l'event a la liste
    retourne event


#choisir un personnages vivant
    personnages vivant = []
    pour personnages dans la team:
        si personnage est vivant on l'ajoute a personnages vivant
    choix = choice (personnages vivant)
    retourner choix 

    




#################### CHOIX  quitter#########################
quitter

#################### CHOIX AFFICHER LES RESULTATS#########################
recupperer les 3meilleurs score 
afficher les 3 meilleurs score

proposer de cliquer sur une touche 
revenir au menu 

"""