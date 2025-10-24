# verifie si un nombre est correct et à la bonne place
def bienPlaces(secret,essai):
    bonne_place= 0
    for i in range(4):
        if (essai[i])==(secret[i]) :
            bonne_place += 1
    return bonne_place

# verifie si un nombre est correcte mais pas à la bonne place
def malPlaces(secret,essai):
    bon_nombre = 0
    for i in range(4):
        if (essai.count(secret[i])) and (essai[i])!=(secret[i]) :
            bon_nombre += 1
    return bon_nombre