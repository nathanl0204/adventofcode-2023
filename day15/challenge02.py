def hash(chaine):
    curr = 0
    for car in chaine:
        curr += ord(car)
        curr *= 17
        curr %= 256
    return curr

fichier = open("input.txt","r")
boites = [[] for _ in range(256)]
focales = {}
for inst in fichier.read().replace("\n","").split(","):
    if "-" in inst:
        label = inst[:-1]
        i = hash(label)
        if label in boites[i]:
            boites[i].remove(label)
    else:
        label, longueur = inst.split("=")
        longueur = int(longueur)
        i = hash(label)
        if label not in boites[i]:
            boites[i].append(label)
        focales[label] = longueur

somme = 0
for nb_boite, boite in enumerate(boites,1):
    for fente, label in enumerate(boite,1):
        somme += nb_boite * fente * focales[label]
print(somme)