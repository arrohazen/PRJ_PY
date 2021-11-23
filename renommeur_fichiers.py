import os

print("Vous êtes situé ici :", os.getcwd())

print("Souhaitez-vous vous déplacer dans un autre répertoire? Oui/Non : ")
Quest1 = input()

if Quest1 == "Oui":
    print("Spécifiez le repertoire voulu (ex : /home/user/dossier) : ")
    Quest2 = input()

        os.walk(Quest2)
        
        emplacement = os.getcwd()
        fichiers = os.listdir(emplacement)

        print("Votre répertoire contient :", fichiers)

            for fichier in fichiers:
                 os.rename(fichier, fichier.replace(" ", "-").lower())

elif Quest1 == "Non":
    os.walk("/home/arrohazen/Documents/cy/fichierpy")
    emplacement = os.getcwd()
    
    print("Le repertoire par défaut sera choisi : ", emplacement)

    fichiers = os.listdir(emplacement)

    print("Votre répertoire contient :", fichiers)

        for fichier in fichiers:
            os.rename(fichier, fichier.replace(" ", "-").lower())

else :
    print("Choisissez Oui ou Non!")


#PREMIERE mODIF avec vs