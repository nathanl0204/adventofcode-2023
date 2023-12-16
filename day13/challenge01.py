def trouve_mirroir(pattern):
    for l in range(1,len(pattern)):
        haut = pattern[:l][::-1]
        bas = pattern[l:]
        haut = haut[:len(bas)]
        bas = bas[:len(haut)]
        if haut == bas:
            return l
    return 0

somme = 0
fichier = open("input.txt","r")
for bloc in fichier.read().split("\n\n"):
    pattern = bloc.splitlines()
    ligne = trouve_mirroir(pattern)
    somme += ligne * 100
    colonne = trouve_mirroir(list(zip(*pattern)))
    somme += colonne
print(somme)