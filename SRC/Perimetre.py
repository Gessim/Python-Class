class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def afficher(self):
        print(f"Rectangle de largeur {self.largeur} et de hauteur {self.hauteur}")

    def obtenir_largeur(self):
        return self.largeur

    def obtenir_hauteur(self):
        return self.hauteur

    def modifier_largeur(self, nouvelle_largeur):
        self.largeur = nouvelle_largeur

    def modifier_hauteur(self, nouvelle_hauteur):
        self.hauteur = nouvelle_hauteur


# Programme principal
mon_rectangle = Rectangle(4, 6)

mon_rectangle.afficher()
print("Périmètre :", mon_rectangle.calculer_perimetre())
print("Surface :", mon_rectangle.calculer_surface())

nouvelle_largeur = 8
mon_rectangle.modifier_largeur(nouvelle_largeur)
nouvelle_hauteur = 10
mon_rectangle.modifier_hauteur(nouvelle_hauteur)

mon_rectangle.afficher()
print("Périmètre :", mon_rectangle.calculer_perimetre())
print("Surface :", mon_rectangle.calculer_surface())
