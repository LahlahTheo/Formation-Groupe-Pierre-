# demande du nom du joueur et accueil
nom=str(input("Quelle est votre nom ? : "))
print(f"Bienvenue {nom} sur le jeu du Master Mind ! ")

# enter la combinaison donnée par le joueur (limité de 1 à 6)
combinaison = []
for i in range(4):
    chiffre=0
    while chiffre >6 or chiffre<1:
        try:
            chiffre = int(input(f"Entrez le chiffre n°{i+1} (entre 1 et 6) : "))
            
        except ValueError:
            print("Veuillez entrer un chiffre valide (entre 1 et 6).")
    combinaison.append(chiffre)
print("Votre combinaison est :", combinaison)
