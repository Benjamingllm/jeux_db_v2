"""###################################### CLASSES ##################################

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


    methode string d'affichage des données"""