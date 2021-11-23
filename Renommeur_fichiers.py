import os

print("Vous êtes situé ici :", os.getcwd())

emplacement = os.getcwd()

fichiers = os.listdir(emplacement)

print("Votre répertoire contient :", fichiers)

for fichier in fichiers:
    os.rename(fichier, fichier.replace(" ", "-").lower())
#PREMIERE mODIF