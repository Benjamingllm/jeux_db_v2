"""
format choices : {
            numero : fonction 
}
option [str]



choix dispo : jouer, voir les scores , quitter

################## Menu ################################


Menu
    tant que vrai:
        ouvrir la db (elle vas passer en argument dans les 2 choix qui la nécessite puis dans les fonction qui
        la demande (sauvegarder le score, recuperer les personnages, monstres etc ))
        recuperer le choix du joueur parmis plusieurs options 
        lancer le choix en question (on appelle choices[choice]())
        fermer la connexion 



    
recuperer le choix du joueur parmis plusieurs options
    Tant que Vrai
        afficher les options numerotées
        demander le choix au joueur
        si le choix est valide
            retourner int(choix)
        afficher message d'erreur







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

    


    
verifier si le choix est valide
    si le choix est pas is_digit
        retourner False
    choix = int(choix)
    if choix inferieur maximum et superieur a minimum:
        return true
    return false

TODO passer avec un validator

#################### CHOIX  quitter#########################
quitter

#################### CHOIX AFFICHER LES RESULTATS#########################
recupperer les 3meilleurs score 
afficher les 3 meilleurs score

proposer de cliquer sur une touche 
revenir au menu 

"""