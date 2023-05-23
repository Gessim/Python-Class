class Voiture:
    def __init__(self, annee, modele, puissance_fiscale, carburant):
        self.annee = annee
        self.modele = modele
        self.puissance_fiscale = puissance_fiscale
        self.carburant = carburant

    def afficher_details(self):
        print(f"Année: {self.annee}")
        print(f"Modèle: {self.modele}")
        print(f"Puissance fiscale: {self.puissance_fiscale}")
        print(f"Carburant: {self.carburant}")
		
class Marque:
    def __init__(self, nom_marque, voitures):
        self.nom_marque = nom_marque
        self.voitures = voitures

    def afficher_voitures(self):
        print(f"Voitures de luxe de la marque {self.nom_marque}:")
        for voiture in self.voitures:
            voiture.afficher_details()
            print()
			
class Catalogue:
    def __init__(self, nom_catalogue, marques):
        self.nom_catalogue = nom_catalogue
        self.marques = marques

    def afficher_marques(self):
        print(f"Marques présentes dans le catalogue {self.nom_catalogue}:")
        for marque in self.marques:
            marque.afficher_voitures()
            print()

from voiture import Voiture
from marque import Marque
from catalogue import Catalogue

# Création des voitures de luxe
voiture1 = Voiture(2022, "Ferrari 488 GTB", 45, "Essence")
voiture2 = Voiture(2023, "Lamborghini Aventador", 50, "Essence")
voiture3 = Voiture(2023, "Porsche 911 Turbo S", 40, "Essence")

# Création des marques
marque1 = Marque("Ferrari", [voiture1])
marque2 = Marque("Lamborghini", [voiture2])
marque3 = Marque("Porsche", [voiture3])

# Création du catalogue
catalogue = Catalogue("Catalogue de voitures de luxe", [marque1, marque2, marque3])

# Affichage des marques et voitures
catalogue.afficher_marques()

