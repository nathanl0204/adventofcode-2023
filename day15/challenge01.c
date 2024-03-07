#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int hash(char *chaine) {
    int curr = 0;
    for (int i = 0; i < strlen(chaine); i++) {
        curr += (int)chaine[i];
        curr *= 17;
        curr %= 256;
    }
    return curr;
}

int part1(char *nom_fichier) {
    int somme = 0;
    FILE *fichier = fopen(nom_fichier, "r");
    if (fichier == NULL) {
        perror("Erreur lors de l'ouverture du fichier.\n");
        return 1;
    }
    char ligne[100000];
    while (fgets(ligne, sizeof(ligne), fichier) != NULL) {
        char *token = strtok(ligne, ",");
        while (token != NULL) {
            token[strcspn(token, "\n")] = 0;
            somme += hash(token);
            token = strtok(NULL, ",");
        }
    }
    fclose(fichier);
    return somme;
}

int main() {
    printf("%d\n", part1("input.txt"));
}