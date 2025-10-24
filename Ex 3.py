secret=[3,2,1,2]
essai=[2,5,1,2]

def bienPlaces(secret,essai):
    bonne_place= 0
    for i in range(4):
        if (essai[i])==(secret[i]) :
            bonne_place += 1
    return bonne_place

def malPlaces(secret,essai):
    bon_nombre = 0
    for i in range(4):
        if ((essai.count(secret[i]))) > 0 and (essai[i])!=(secret[i]):
            bon_nombre += 1
    return bon_nombre

print(bienPlaces(secret,essai))
print(malPlaces(secret,essai))
