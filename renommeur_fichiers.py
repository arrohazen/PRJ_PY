import os
import shutil
import getpass

print("Vous êtes situé ici :", os.getcwd())

print("Souhaitez-vous vous déplacer dans un autre répertoire? Oui/Non : ")
rep_quest = input()
user = getpass.getuser()

def demander_repertoire():
    rep_quest = str(input("Spécifiez le repertoire voulu (ex : /home/user/dossier) : "))
    os.chdir(rep_quest)
    localisation = os.getcwd()

def renommage() :
    for fichier in fichiers:
     os.rename(fichier, fichier.replace(" ", "-").lower())

def trier_fichiers():
    emplacement_dest = "/home/"+user+"/"
    repertoire_noms = ['Images', 'archives', 'Musique' , 'Paquets_Debian']
    
    for repertoire in range(0,4):
        if not os.path.exists(emplacement_dest+repertoire_noms[repertoire]):
         os.makedirs(emplacement_dest+repertoire_noms[repertoire])

        for fichier in fichiers:
            if ".jpg" in fichier and not os.path.exists(emplacement_dest+'Images/'+fichier):
                shutil.move(emplacement+"/"+fichier, emplacement_dest+'Images/'+fichier)
            if ".jpeg" in fichier and not os.path.exists(emplacement_dest+'Images/'+fichier):
                shutil.move(emplacement+"/"+fichier, emplacement_dest+'Images/'+fichier)
            if ".png" in fichier and not os.path.exists(emplacement_dest+'Images/'+fichier):
                shutil.move(emplacement+"/"+fichier, emplacement_dest+'Images/'+fichier)
            if ".zip" in fichier and not os.path.exists(emplacement_dest+'archives/'+fichier):
                shutil.move(emplacement+"/"+fichier, emplacement_dest+'archives/'+fichier)
            if ".mp3" in fichier and not os.path.exists(emplacement_dest+'Musique/'+fichier):
                shutil.move(emplacement+"/"+fichier, emplacement_dest+'Musique/'+fichier)
            if ".deb" in fichier and not os.path.exists(emplacement_dest+'Paquets_Debian/'+fichier):
                shutil.move(emplacement+"/"+fichier, emplacement_dest+'Paquets_Debian/'+fichier)

if rep_quest == "Oui":
    emplacement = demander_repertoire()
    fichiers = os.listdir(emplacement)
   
    print("Votre répertoire contient :", fichiers)
   
    renommage()
    
    print("Vos fichiers ont été renommés : ", os.listdir(emplacement)) 

    trier_fichiers()

elif rep_quest == "Non":

    os.chdir("/home/"+user+"/Téléchargements/")
    emplacement = os.getcwd()
    print(emplacement)
    print("Le repertoire par défaut sera choisi : ", emplacement)

    fichiers = os.listdir(emplacement)

    print("Votre répertoire contient :", fichiers)
        
    renommage()

    print("Vos fichiers ont été renommés : ", os.listdir(emplacement)) 

    trier_fichiers()

else :
    print("Choisissez Oui ou Non!")
