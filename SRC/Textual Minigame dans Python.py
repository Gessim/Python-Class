import random

def jeu_pierre_papier_ciseaux():
    choix_possibles = ["pierre", "papier", "ciseaux"]
    
    print("Bienvenue dans le jeu Pierre, Papier, Ciseaux !")
    
    while True:
        choix_joueur = input("Choisissez votre coup (pierre, papier, ciseaux) ou 'q' pour quitter : ")
        
        if choix_joueur.lower() == "q":
            break
        
        if choix_joueur.lower() not in choix_possibles:
            print("Choix invalide. Veuillez choisir entre pierre, papier ou ciseaux.")
            continue
        
        choix_ordi = random.choice(choix_possibles)
        
        print(f"Joueur : {choix_joueur}")
        print(f"Ordinateur : {choix_ordi}")
        
        if choix_joueur.lower() == choix_ordi:
            print("Égalité !")
        elif (choix_joueur.lower() == "pierre" and choix_ordi == "ciseaux") or \
             (choix_joueur.lower() == "papier" and choix_ordi == "pierre") or \
             (choix_joueur.lower() == "ciseaux" and choix_ordi == "papier"):
            print("Vous avez gagné !")
        else:
            print("L'ordinateur a gagné !")

jeu_pierre_papier_ciseaux()
