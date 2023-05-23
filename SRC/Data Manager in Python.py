 class DataManager:
    def __init__(self):
        self.data = []
    
    def ajouter_element(self, element):
        self.data.append(element)
        print("Élément ajouté avec succès.")
    
    def afficher_elements(self):
        if len(self.data) == 0:
            print("Aucun élément à afficher.")
        else:
            print("Liste des éléments :")
            for element in self.data:
                print(element)
    
    def supprimer_element(self, element):
        if element in self.data:
            self.data.remove(element)
            print("Élément supprimé avec succès.")
        else:
            print("Élément non trouvé.")

# Exemple d'utilisation du DataManager

# Création d'une instance du DataManager
data_manager = DataManager()

# Ajout d'éléments à la liste
data_manager.ajouter_element("Élément 1")
data_manager.ajouter_element("Élément 2")
data_manager.ajouter_element("Élément 3")

# Affichage des éléments
data_manager.afficher_elements()

# Suppression d'un élément
data_manager.supprimer_element("Élément 2")

# Affichage des éléments après suppression
data_manager.afficher_elements()
