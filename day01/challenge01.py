chiffres = ["0","1","2","3","4","5","6","7","8","9"]

def somme_calibration_values(nom_fichier):
    fichier = open(nom_fichier,"r")
    L = fichier.readlines()
    L = [mot.rstrip() for mot in L]
    somme = 0
    for mot in L:
        for i in range(len(mot)):
            if mot[i] in chiffres:
                premier_chiffre = mot[i]
                break
        for i in range(1,len(mot)+1):
            if mot[-i] in chiffres:
                dernier_chiffre = mot[-i]
                break
        calibration_value = premier_chiffre + dernier_chiffre
        somme += int(calibration_value)
    fichier.close()
    return somme

if __name__ == '__main__':
    print("Réponse challenge 1 : " + str(somme_calibration_values('input.txt')))
