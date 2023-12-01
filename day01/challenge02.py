import re

def somme_calibration_values(nom_fichier):
    values = []
    fichier = open(nom_fichier,"r")
    for ligne in fichier:
        values.append(ligne.rstrip())
    somme = 0
    dico = {'one' : 'on1e', 'two' : 'tw2o', 'three' : 'thr3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en','eight' : 
'ei8ght','nine':'ni9ne'}
    for ligne in values:
        for cle,valeur in dico.items():
            ligne = ligne.replace(cle, valeur)
        chiffres = re.sub('\D','',ligne)
        somme += int(chiffres[0] + chiffres[-1])
    return somme

if __name__ == '__main__':
    print("Réponse challenge 2 : " + str(somme_calibration_values("input.txt")))
