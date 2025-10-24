# importer la fonction pour initialiser la combinaison secrete (-> comb_s)
from Ex2 import init_combinaison
from Ex3 import *

comb_s=init_combinaison()
victoire = False
tour = 0
nom=str(input("Quelle est votre nom ? : "))
print(f"Bienvenue {nom} sur le jeu du Master Mind ! ")
while victoire == False or tour < 11:
    # enter la combinaison donnée par le joueur (limité de 1 à 6)
    comb_j = []
    for i in range(4):
        chiffre=0
        while chiffre >6 or chiffre<1:
            try:
                chiffre = int(input(f"Entrez le chiffre n°{i+1} (entre 1 et 6) : "))
                
            except ValueError:
                print("Veuillez entrer un chiffre valide (entre 1 et 6).")
        comb_j.append(chiffre)
    tour += 1
    bien_places=bienPlaces(comb_s,comb_j)
    if bien_places == 4 :
        victoire = True
        print("Bravo tu as gagné au tour n°",i," !!!")
    else :  
        print(f"Il y a {bien_places} nombre(s) bien placés et {malPlaces(comb_s,comb_j)} nombre(s) mal placés")
if victoire == False :
    print("Perdu... La bonne combinaison était ",comb_s)