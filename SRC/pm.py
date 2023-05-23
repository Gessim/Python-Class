#include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMENTS 100

struct DataManager {
    int data[MAX_ELEMENTS];
    int count;
};

void initialiser(struct DataManager* dataManager) {
    dataManager->count = 0;
}

void ajouter_element(struct DataManager* dataManager, int element) {
    if (dataManager->count < MAX_ELEMENTS) {
        dataManager->data[dataManager->count++] = element;
        printf("Element ajoute avec succes.\n");
    } else {
        printf("Impossible d'ajouter l'element. Le tableau est plein.\n");
    }
}

void afficher_elements(struct DataManager* dataManager) {
    if (dataManager->count == 0) {
        printf("Aucun element a afficher.\n");
    } else {
        printf("Liste des elements :\n");
        for (int i = 0; i < dataManager->count; i++) {
            printf("%d\n", dataManager->data[i]);
        }
    }
}

void supprimer_element(struct DataManager* dataManager, int element) {
    int index = -1;
    for (int i = 0; i < dataManager->count; i++) {
        if (dataManager->data[i] == element) {
            index = i;
            break;
        }
    }
    
    if (index != -1) {
        for (int i = index; i < dataManager->count - 1; i++) {
            dataManager->data[i] = dataManager->data[i + 1];
        }
        dataManager->count--;
        printf("Element supprime avec succes.\n");
    } else {
        printf("Element non trouve.\n");
    }
}

// Exemple d'utilisation du DataManager

int main() {
    struct DataManager dataManager;
    
    // Initialisation du DataManager
    initialiser(&dataManager);
    
    // Ajout d'elements au tableau
    ajouter_element(&dataManager, 10);
    ajouter_element(&dataManager, 20);
    ajouter_element(&dataManager, 30);
    
    // Affichage des elements
    afficher_elements(&dataManager);
    
    // Suppression d'un element
    supprimer_element(&dataManager, 20);
    
    // Affichage des elements apres suppression
    afficher_elements(&dataManager);
    
    return 0;
}
