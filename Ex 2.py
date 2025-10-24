# fonction qui ne prends pas de paramètres et renvoie une liste qui correspond à la combinaison secrete
def init_combinaison():

    # importation du module pour l'aléatoire
    from random import randint

    liste=[]
    for i in range(4):
        liste.append(randint(1,6))
    return liste