import math
import re

def somme(nomfichier):
    donnees = list(open(nomfichier,"r"))
    caracteres = {(i,j) : [] for i in range(140) for j in range(140) if donnees[i][j] not in '0123456789.'} #dictionnaire stockant les symboles
    for i, ligne in enumerate(donnees): #couple (numéro_ligne, contenu_ligne)
        for n in re.finditer(r'\d+',ligne): #matche tous les chiffres
            bord = {(i,j) for i in (i-1,i,i+1) for j in range(n.start()-1,n.end()+1)} #définit une région 3*3 autour de l'occurence
            for coord in bord & caracteres.keys():
                caracteres[coord].append(int(n.group()))
    return sum(math.prod(p) for p in caracteres.values() if len(p) == 2)

if __name__ == '__main__':
    print(somme("input.txt"))