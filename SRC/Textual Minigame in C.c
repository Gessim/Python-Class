#include <stdio.h>
#include <stdlib.h>

int main() {
    int nombreMystere, nombreJoueur, essais = 0;
    
    // Génération d'un nombre aléatoire entre 1 et 100
    srand(time(0));
    nombreMystere = rand() % 100 + 1;
    
    printf("Bienvenue dans le jeu du nombre mystere !\n");
    
    do {
        printf("Entrez un nombre entre 1 et 100 : ");
        scanf("%d", &nombreJoueur);
        
        essais++;
        
        if (nombreJoueur < nombreMystere) {
            printf("C'est plus !\n");
        } else if (nombreJoueur > nombreMystere) {
            printf("C'est moins !\n");
        } else {
            printf("Bravo, vous avez trouvé le nombre mystere en %d essai(s) !\n", essais);
        }
        
    } while (nombreJoueur != nombreMystere);
    
    return 0;
}
