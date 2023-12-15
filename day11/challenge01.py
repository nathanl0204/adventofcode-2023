fichier = open("input.txt","r")
universe = fichier.read().splitlines()
lignes_vides = [l for l, ligne in enumerate(universe) if all(ch == "." for ch in ligne)]
colonnes_vides = [c for c, colonne in enumerate(zip(*universe)) if all(ch == "." for ch in colonne)]
points = [(l,c) for l, ligne in enumerate(universe) for c, ch in enumerate(ligne) if ch == "#"]
somme = 0
espace = 2
for i, (l1,c1) in enumerate(points):
    for (l2,c2) in points[:i]:
        for l in range(min(l1,l2), max(l1,l2)):
            somme += espace if l in lignes_vides else 1
        for c in range(min(c1,c2), max(c1,c2)):
            somme += espace if c in colonnes_vides else 1
print(somme)