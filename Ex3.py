# secret=[4,5,1,6]
# essai= [5,1,1,5]
# essai= [1,1,1,1]
# essai= [2,2,2,2]
# essai= [1,5,1,5]

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
    nb_mal_places =[]
    for i in range(4):
        if (essai.count(secret[i])) and (essai[i])!=(secret[i]) :
        # if (essai[i])!=(secret[i]) and (secret.count(essai[i])) > 0 and (nb_mal_places.count(essai[i])) == 0 :
            bon_nombre += 1
        #     nb_mal_places.append(essai[i])
    return bon_nombre

# print(bienPlaces(secret,essai), "bien placé")
# print(malPlaces(secret,essai), "mal placé")