# importer la fonction pour initialiser la combinaison secrete (-> comb_s) et l'afficher
from Ex2 import *
# importer les fonctions pour vérifier la validités des nombres
from Ex3 import *

comb_s=init_combinaison()
victoire = False
tour = 0
nom=str(input("Quelle est votre nom ? : "))
print(f"Bienvenue {nom} sur le jeu du Master Mind ! ")

while victoire == False and tour < 10:
    # enter la combinaison donnée par le joueur (limité de 1 à 6)
    comb_j = []
    tour += 1
    for i in range(4):
        chiffre=0
        while chiffre >6 or chiffre<1:
            try:
                chiffre = int(input(f"Entrez le chiffre n°{i+1} (entre 1 et 6) : "))    
            except ValueError:
                print("Veuillez entrer un chiffre valide (entre 1 et 6).")
        comb_j.append(chiffre)
    bien_places=bienPlaces(comb_s,comb_j)
    if bien_places == 4 :
        victoire = True
        print(f"Bravo {nom} tu as gagné au tour n°",tour," !!!")
    else :  
        print(f"Il y a {bien_places} nombre(s) bien placé(s) et {malPlaces(comb_s,comb_j)} nombre(s) mal placé(s), {10-tour} tour(s) restant(s)\n")
if victoire == False :
    print("Perdu... La bonne combinaison était ",end=" "),aff_comb(comb_s)