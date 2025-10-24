
nom=str(input("Quelle est votre nom ? : "))
print(f"Bienvenue {nom} sur le jeu du Master Mind ! ")

combinaison = []

for i in range(4):
    while True:
        try:
            chiffre = int(input(f"Entrez le chiffre n°{i+1} (entre 1 et 6) : "))
            if 1 <= chiffre <= 6:
                combinaison.append(chiffre)
                break
            else:
                print("Le chiffre doit être entre 1 et 6.")
        except ValueError:
            print("Veuillez entrer un chiffre valide (entre 1 et 6).")

print("Votre combinaison est :", combinaison)
