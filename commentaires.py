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
    
    tant que l'équipe n'est pas pleine
        recuperer le choix du joueur parmis la liste d'options
        créer une instance du personnage
        ajouter dans la team

#score =  boucle de jeux
#afficher le score 
#proposer de cliquer sur une touche
#revenir au menu 

choisir un monstre au hasard
    recuperer les monstres 
    en retourner un au hasard

recup les monstres
recup les joueurs

#### boucle de jeux ####
    score = 0
    choisir un monstre au hasard
    
    tant que la team n'es pas morte:
        score += phase de combat
        si monstre est mort  :
            choisir un nouveau monstre


    afficher la mort du personnage
    sauvegarder les resultat dans la db
    retourner score 




afficher les resultat (event)
    pour event in events:
        afficher event    
        

phase de combat
    tant que la team est pas morte et que le monstre est pas mort :
        event = attaque equipe
        si monstre mort : 
            afficher event
            retourner score
        ajouter a event attaque du monstre
        ajouter 1 au score
        afficher event
    retourner score
    
    

    
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
    retourne events


        


            

    

#################### CHOIX  quitter#########################
quitter

#################### CHOIX AFFICHER LES RESULTATS#########################
recupperer les 3meilleurs score 
afficher les 3 meilleurs score
proposer de cliquer sur une touche 
revenir au menu 




###################################### CLASSES ##################################

classe mob
    initialisation (pv, atk,defense,est_mort,nom)
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
