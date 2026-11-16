"""
format choix : {
            numero : fonction 
}
option [str]



choix dispo : jouer, voir les scores , quitter

################## Menu ################################


Menu
    recuperer le choix du joueur parmis plusieurs options 
    lancer le choix en question (on appelle choix[1]())


    
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
    tant que l'équipe n'est pas pleine
        recuperer le choix du joueur parmis la liste d'options
        créer une instance du personnage
        ajouter dans la team

#lancer la boucle de jeux
#afficher le score 


#### boucle de jeux ####
    score = 0
    
    tant que la team n'es pas morte:
        choisir un monstre au hasart
        phase de combat


    sauvegarder les resultat dans la db 
    retourner score



afficher les resultat (event)
    pour event in events:
        afficher event    
        

tour
    events = []
    ajouter l'attaque du monstre a event
    ajouter l'attaque de la team a event
    on retourne les events

    
attaque du monstre
    events = []
    le monstre attaque un perso aléatoire
            on choisis un personnage aléatoire
            le monstre l'attaque
            on ajoute l'évenement a la liste
            si il est mort :
                on l'enlève de la team
                on ajoute l'event a la liste
    retourner events



attaque de la team
    events = []
    pour personnages dans la team
        personnage attaque le monstre
        on ajoute a events
        si le monstre est mort :
             retourner events, True
    retourner events, None
            

    

#################### CHOIX LANCER JEUX #########################








###################################### CLASSES ##################################

classe mob
    initialisation (pv, atk,defense,est_mort)
        on initialise les variables 


    attaque(cible)
        cible prend des dégats equivalent au montant d'ataque

    prendre des dégats(montant)
        on enleve le maximum de : 1 et nombre de pv du montant d'ataque - la défense 
        si pv <=0:
            pv = 0
            est_mort = true

        

##classes identiques pour l'instant mais scalable si des actions spécifiques au joueur ou ennemi sont ajoutés

classe Personnage(Mob)
    initialisation
        hérite des paramètres de mob


classe Enemi(Mob)
    initialisation
        hérite des paramètres de mob
    

"""
