import os
import shutil
import getpass
import argparse

parser = argparse.ArgumentParser(description= 'Choose a function (sorter, renamer, )')
parser.add_argument( '-s', '--sorter',  action='store_true', help='Sorter of files by extension')
parser.add_argument( '-r', '--rename',  action='store_true', help='Renaming files : replace spaces to -')
parser.add_argument( '-l', '--location',  type=str, help='Giving a directory location')

args = parser.parse_args()

print("Bienvenue dans le script de renamer et de tri de fil! ")
print("Vous êtes situé ici :", os.getcwd())

#print("Souhaitez-vous vous déplacer dans un autre répertoire? Oui/Non : ")
#rep_quest = input()
user = getpass.getuser()

def ask_dir():
    rep_quest = str(input("Spécifiez le directory voulu (par défaut : /home/user/Téléchargements/) : "))
    os.chdir(rep_quest)
    localisation = os.getcwd()

def renamer(files) :
    os.chdir(location)
    for file in files:
        os.rename(file, file.replace(" ", "-").lower())

def trier_files():
    location_dest = "/home/"+user+"/"
    directory_names = ['Images', 'archives', 'Musique' , 'Paquets_Debian']
    
    for directory in directory_names:
        if not os.path.exists(location_dest+directory):
         os.makedirs(location_dest+directory)

    for file in files:
        if ".jpg" in file and not os.path.exists(location_dest+'Images/'+file):
            shutil.move(location+"/"+file, location_dest+'Images/'+file)
        if ".jpeg" in file and not os.path.exists(location_dest+'Images/'+file):
            shutil.move(location+"/"+file, location_dest+'Images/'+file)
        if ".png" in file and not os.path.exists(location_dest+'Images/'+file):
            shutil.move(location+"/"+file, location_dest+'Images/'+file)
        if ".zip" in file and not os.path.exists(location_dest+'archives/'+file):
            shutil.move(location+"/"+file, location_dest+'archives/'+file)
        if ".mp3" in file and not os.path.exists(location_dest+'Musique/'+file):
            shutil.move(location+"/"+file, location_dest+'Musique/'+file)
        if ".deb" in file and not os.path.exists(location_dest+'Paquets_Debian/'+file):
            shutil.move(location+"/"+file, location_dest+'Paquets_Debian/'+file)

if args.rename:

    location = args.location

    files = os.listdir(location)
    
    print("Votre répertoire contient :", files)
   
    renamer(files)
    
    print("Vos files ont été renommés : ", os.listdir(location)) 

elif args.sorter and args.location:

    location = args.location
    os.chdir(location)
    print(location)
    print("Le directory par défaut sera choisi : ", location)

    files = os.listdir(location)

    print("Votre répertoire contient :", files)
        
    #renamer(files)

    #print("Vos files ont été renommés : ", os.listdir(location)) 

    trier_files()

    print("Vos files ont été triés : Musique, archives, Images... vers votre dossier personnel")


elif args.sorter and not args.location:

    os.chdir("/home/"+user+"/Téléchargements/")
    location = os.getcwd()
    print(location)
    print("Le directory par défaut sera choisi : ", location)

    files = os.listdir(location)

    print("Votre répertoire contient :", files)
        
    #renamer(files)

    #print("Vos files ont été renommés : ", os.listdir(location)) 

    trier_files()

    print("Vos files ont été triés : Musique, archives, Images... vers votre dossier personnel")

elif args.rename and not args.location:
    
    location = "/home/"+user+"/Téléchargements/"

    os.chdir(location)

    files = os.listdir(location)
    
    print("Votre répertoire contient :", files)
   
    renamer(files)
    
    print("Vos files ont été renommés : ", os.listdir(location)) 

else:
    print("Aucun argument choisi !")