"""
format choices : {
            numero : fonction 
}
option [str]



choix dispo : jouer, voir les scores , quitter

################## Menu ################################


Menu
    ouvrir la db (elle vas passer en argument dans les 2 choix qui la nécessite puis dans les fonction qui
    la demande (sauvegarder le score, recuperer les personnages, monstres etc ))
    recuperer le choix du joueur parmis plusieurs options 
    lancer le choix en question (on appelle choices[choice]())


    
recuperer le choix du joueur parmis plusieurs options
    afficher les options numerotées
    Tant que Vrai
        demander le choix au joueur
        si le choix est valide
            retourner int(choix)
        afficher message d'erreur

    

afficher les options numereotées
    pour numero, option dans enumerate(options)
        afficher f"{numero} : {option}"
    
verifier si le choix est valide
    si le choix est pas is_digit
        retourner False
    choix = int(choix)
    retourner choix inferieur maximum et superieur a minimum


    
#################### CHOIX LANCER JEUX #########################

#demander pseudo
#recuperer les choix de personnages du joueurs parmis plusieures options
    team = []
    personnages recuoerer les personnages
    monstres = recuperer les monstres
    tant que l'équipe n'est pas pleine
        recuperer le choix du joueur parmis la liste d'options
        créer une instance du personnage
        ajouter dans la team

#score =  boucle de jeux
sauvegarde score
ferme la connexion 
#afficher le score 
#proposer de cliquer sur une touche
#revenir au menu 


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
    monstre = nouveau monstre
    tant que la team n'est pas vide :
        events = attaque equipe
        si monstre mort :
            monstre = nouveau monstre
        sinon :
            ajouter attaque monstre a event
        score += 1
        afficher les events

    retourner score




afficher les resultat (event)
    pour event in events:
        afficher event    
        
    
    

    
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
    choisi un personnage au hasard 
    le monstre attaque le personnage
    ajouter l'event a la liste
    si le personnage est mort :
        ajouter l'event a la liste
        on le retire de la team
    retourne event


        


            

    

#################### CHOIX  quitter#########################
quitter

#################### CHOIX AFFICHER LES RESULTATS#########################
recupperer les 3meilleurs score 
afficher les 3 meilleurs score
proposer de cliquer sur une touche 
revenir au menu 




###################################### CLASSES ##################################

classe mob
    initialisation (pv, atk,defense,nom)
        on initialise les variables 




    prendre des dégats(montant)
        on enleve le maximum de : 1 et nombre de pv du montant d'ataque - la défense 
        si pv <=0:
            pv = 0

        
    est_mort
        retourner pv inferieur ou = a 0

        

##classes identiques pour l'instant mais scalable si des actions spécifiques au joueur ou ennemi sont ajoutés

classe Personnage(Mob)
    initialisation
        hérite des paramètres de mob


classe Enemi(Mob)
    initialisation
        hérite des paramètres de mob


Classe Event
    INITIALISATION 
        cible
        source


class Attaque(Event):
    INTIalisation 
        heritage de Event
        dégats
        vie

    methode string d'affichage des données


class Mort(Event)
     INTIalisation 
            heritage de Event


    methode string d'affichage des données
"""
