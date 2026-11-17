
"""


afficher event (event)
    pour event in events:
        afficher event    

        
#afficher les 3 meilleurs score



#    

afficher les options numereotées
    pour index, option dans enumerate(options =  start = 1)
        afficher f"{index} : {option}"
        """

def display_numbered_options(options):
    for index,option in enumerate(options,start=1):
        print(f"{index} : {option}")

def format_character_info(characters):
    print(characters)
    formated_characters = []
    for character in characters:
        str = f"nom : {character["nom"] }, pv : {character["pv"]}, attaque {character["attaque"]}, defense : {character["defense"]}"
        formated_characters.append(str)
    return formated_characters