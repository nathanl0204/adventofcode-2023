def hash(chaine):
    curr = 0
    for car in chaine:
        curr += ord(car)
        curr *= 17
        curr %= 256
    return curr

somme = 0
fichier = open("input.txt","r")
elements = fichier.read().split(",")
for element in elements:
    element = element.rstrip()
    somme += hash(element)
print(somme)
