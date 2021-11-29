import os

print("Vous êtes situé ici :", os.getcwd())

print("Souhaitez-vous vous déplacer dans un autre répertoire? Oui/Non : ")
rep_quest = input()

def demander_repertoire():
    rep_quest = str(input("Spécifiez le repertoire voulu (ex : /home/user/dossier) : "))
    os.chdir(rep_quest)
    localisation = os.getcwd()

def renommage() :
    for fichier in fichiers:
     os.rename(fichier, fichier.replace(" ", "-").lower())

if rep_quest == "Oui":
    emplacement = demander_repertoire()
    fichiers = os.listdir(emplacement)
   
    print("Votre répertoire contient :", fichiers)
   
    renommage()
    
    print("Vos fichiers ont été renommés : ", os.listdir(emplacement)) 

elif rep_quest == "Non":
    
    os.chdir("/home/arrohazen/Documents/cy/fichierpy/")
    emplacement = os.getcwd()
    
    print("Le repertoire par défaut sera choisi : ", emplacement)

    fichiers = os.listdir(emplacement)

    print("Votre répertoire contient :", fichiers)
        
    renommage()

    print("Vos fichiers ont été renommés : ", os.listdir(emplacement)) 

else :
    print("Choisissez Oui ou Non!")

