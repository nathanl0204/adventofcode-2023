def differences(liste):
    if all(element == 0 for element in liste):
        return 0
    liste_diff = [y - x for x,y in zip(liste,liste[1:])]
    diff = differences(liste_diff)
    return liste[-1] + diff

somme = 0

fichier = open("input.txt","r")
for ligne in fichier:
    numeros = list(map(int,ligne.split()))
    somme += differences(numeros)

print(somme)
