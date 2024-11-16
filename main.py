import random
import json
import os

def generateur_mdp(taille):
    """
    Génère un mot de passe (mdp) aléatoire.
    Entrée : taille de mdp demandée par l'utilisateur
    Sortie : mdp aléatoire et nommé dans un fichier json
    """
    mdp = ""
    for i in range(taille):
        # Chaque caractère est choisi aléatoirement puis ajouté au mdp
        mdp = mdp + CARACTERES[int(random.randint(0, len(CARACTERES)-1))]
    print(f"Le mot de passe généré pour {lieu_mdp} est :\n{mdp}")

    # Ajoute ce nouveau mdp au dictionnaire "donnees" dans le fichier json
    donnees[lieu_mdp] = mdp
    with open(FICHIER_JSON, "w") as fichier:
        json.dump(donnees, fichier, indent=4)


def retrouver_mdp():
    """
    Retrouve un mdp dans le fichier json a partir de son nom
    Entrée : nom donné par l'utilisateur
    Sortie : mot de passe renseigné à ce nom
    """
    if lieu_mdp_demande in donnees:
        print(f"Le mot de passe pour {lieu_mdp_demande} est :\n" + donnees[lieu_mdp_demande])
    else:
        print(f"Le mot de passe {lieu_mdp_demande} n'existe pas!")

#------------------ Affectation des variables ------------------

DEMANDE = input("------------ Que voulez vous faire ? ------------\n Tapez 'generer' pour générer un nouveau mot de passe \n Tapez 'chercher' pour chercher un nouveau mot de passe\n")
CARACTERES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890;:!%/.?&'(-_)=@+$[{#|`^]}µ*"
FICHIER_JSON = "passwords.json"

taille_demandee = ""
lieu_mdp = ""
lieu_mdp_demande = ""

#------------------ Programme principal ------------------

# Vérifier que le fichier existe
if os.path.exists(FICHIER_JSON):
    with open(FICHIER_JSON, "r") as fichier:
        contenu = fichier.read().strip()
        # Charger les données ou initialiser un dictionnaire
        donnees = json.loads(contenu) if contenu else {}
else:
    # créer un dictionnaire "donnees"
    donnees = {}

if DEMANDE == "generer":
    taille_demandee = int(input(f"Veuillez choisir une longueur de mot de passe [ MAXIMUM = {len(CARACTERES) - 1} ]"))
    # Vérifie que la taille demandée ne dépasse pas le nombre de caractères disponibles
    if taille_demandee > len(CARACTERES)-1:
        print("nombre trop élevé!")
    else:
        # Demande le nom a attribué au mdp puis le génère
        lieu_mdp = input("Pour quel compte souhaiterez-vous générer un mot de passe ?")
        generateur_mdp(taille_demandee)

elif DEMANDE == "chercher":
    # Demande quel mdp veut il récupérer puis le récupère
    lieu_mdp_demande = input("Quel mot de passe souhaitez-vous chercher ?")
    retrouver_mdp()

else:
    print("Veuillez formuler l'une des 2 commandes proposées")
