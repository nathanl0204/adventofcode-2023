#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char chiffres[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

int somme_calibration_values(char* nom_fichier) {
    FILE *fichier = fopen(nom_fichier, "r");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        exit(1);
    }
    char ligne[100];
    int somme = 0;
    while (fgets(ligne, sizeof(ligne), fichier) != NULL) {
        char* mot = strtok(ligne, " \n");
        while (mot != NULL) {
            char premier_chiffre, dernier_chiffre;
            for (int i = 0; i < strlen(mot); i++) {
                if (strchr(chiffres, mot[i]) != NULL) {
                    premier_chiffre = mot[i];
                    break;
                }
            }
            for (int i = strlen(mot) - 1; i>= 0; i--) {
                if (strchr(chiffres, mot[i]) != NULL) {
                    dernier_chiffre = mot[i];
                    break;
                }
            }
            char calibration_value[3];
            calibration_value[0] = premier_chiffre;
            calibration_value[1] = dernier_chiffre;
            calibration_value[2] = '\0';
            somme += atoi(calibration_value);
            mot = strtok(NULL, " \n");
        }
    }
    fclose(fichier);
    return somme;
}

int main() {
    printf("Réponse challenge 1 : %d\n", somme_calibration_values("input.txt"));
    return 0;
}