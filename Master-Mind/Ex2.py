# fonction qui ne prends pas de paramètres et renvoie une liste qui correspond à la combinaison secrete
def init_combinaison():

    # importation du module pour l'aléatoire
    from random import randint

    liste=[]
    for i in range(4):
        liste.append(randint(1,6))
    return liste

# fonction qui affiche une combinaison sur une seule ligne
def aff_comb(liste):
    for i in range (4):
        print(liste[i], end=" ")
    return