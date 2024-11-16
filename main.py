import random
import json
import os

# Entrée: taille de mdp demandée / Sortie: mdp aléatoire
def generateur_mdp(taille):
    mdp = ""
    for i in range(taille):
        mdp = mdp + caracteres[int(random.randint(0, len(caracteres)-1))] # chaque terme du mdp est ajouté après le précédent
    print(mdp)

    # Ajouter ce nouveau mdp au dictionnaire "donnees" dans le json
    donnees[lieu_mdp] = mdp
    with open(fichier_json, "w") as fichier:
        json.dump(donnees, fichier, indent=4)

# Retrouver un mdp précis dans le json en cherchant son nom puis en affichant le mdp attribué
def retrouver_mdp():
    if lieu_mdp_demande in donnees:
        print(f"Le mot de passe pour {lieu_mdp_demande} est :\n" + donnees[lieu_mdp_demande])
    else:
        print(f"Le mot de passe {lieu_mdp_demande} n'existe pas!")

#------------------ Affectation des variables ------------------

demande = input("------------ Que voulez vous faire ? ------------\n Tapez 'generer' pour générer un nouveau mot de passe \n Tapez 'chercher' pour chercher un nouveau mot de passe\n")
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890;:!%/.?&'(-_)=@+$[{#|`^]}µ*"
fichier_json = "passwords.json"

taille_demandee = ""
lieu_mdp = ""
lieu_mdp_demande = ""

#------------------ Programme principal ------------------

if os.path.exists(fichier_json): # Vérifier que le fichier existe
    with open(fichier_json, "r") as fichier:
        contenu = fichier.read().strip()
        donnees = json.loads(contenu) if contenu else {}  # Charger les données ou initialiser un dictionnaire
else:
    donnees = {} # créer un dictionnaire "donnees"

if demande == "generer":
    taille_demandee = int(input(f"Veuillez choisir une longueur de mot de passe [ MAXIMUM = {len(caracteres) - 1} ]"))
    lieu_mdp = input("Pour quel compte souhaiterez-vous générer un mot de passe ?")
    if taille_demandee > len(caracteres)-1:
        print("nombre trop élevé!")
    else:
        generateur_mdp(taille_demandee)

elif demande == "chercher":
    lieu_mdp_demande = input("Quel mot de passe souhaitez-vous chercher ?")
    retrouver_mdp()

else: print("Veuillez formuler l'une des 2 commandes proposées")