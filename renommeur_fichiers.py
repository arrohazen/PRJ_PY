import os
import shutil
import getpass
import argparse
import pathlib


#Usage of argparse to take usage method 
parser = argparse.ArgumentParser(description= 'Choose a function (sorter, renamer, )')
parser.add_argument( '-s', '--sorter',  action='store_true', help='Sorter of files by extension')
parser.add_argument( '-r', '--rename',  action='store_true', help='Renaming files : replace spaces to -')
parser.add_argument( '-l', '--location',  type=str, help='Giving a directory location')
args = parser.parse_args()

music = ['.wav', '.mp3', '.m4a', '.flac', '.aac', '.midi']
pictures = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
packages = ['.deb', '.rpm', '.npm', '.snap','.exe', '.dmg', '.pkg', '.apk']
archives = ['.zip', '.tar', '.xz', '.gz']
disk_img = ['.iso', '.img', '.vdi', '.cso', '.rom']

#Get the user to make 
user = getpass.getuser()
#Function rename : replacing spaces to -
def renamer(files):
    os.chdir(location)
    for file in files:        
        ext = os.path.splitext(file)
        #print(ext[0])
        counter = 1
        for picture_ext in pictures:
            if picture_ext in file:
                new_name = f'Image_{counter}{ext[1]}'
                os.rename(file, new_name)
                os.rename(file, file.replace(" ", "-").lower())
            counter += 1
        for music_ext in music:
            if music_ext in file:
                new_name = f'Music_{counter}{ext[1]}'
                os.rename(file, new_name)
                os.rename(file, file.replace(" ", "-").lower())
            counter += 1


    
#Function who sort files 
def sort_files():
    location_dest = "/home/"+user+"/"
    directory_names = ['Images', 'archives', 'Music' , 'Packages', 'Images_Disques']
    #Create directories if they are not in the user directory
    for directory in directory_names:
        if not os.path.exists(f'{location_dest}{directory}'):
            os.makedirs(location_dest+directory)
  
    #Organise files by extension
    for file in files:
        for picture_ext in pictures:
            if picture_ext in file and not os.path.exists(location_dest+'Images/'+file):               
                shutil.move(f'{location}{"/"}{file}', f'{location_dest}{"Images/"}{file}')    
        for archive_ext in archives:
            if archive_ext in file and not os.path.exists(location_dest+'archives/'+file):
                shutil.move(f'{location}{"/"}{file}', f'{location_dest}{"archives/"}{file}')
        for title_ext in music:
            if title_ext in file and not os.path.exists(location_dest+'Music/'+file):
                shutil.move(f'{location}{"/"}{file}', f'{location_dest}{"Music/"}{file}')
        for package_ext in packages:
            if package_ext in file and not os.path.exists(location_dest+'Packages/'+file):
                shutil.move(f'{location}{"/"}{file}', f'{location_dest}{"Packages/"}{file}')
        for disk_ext in disk_img:
            if disk_ext in file and not os.path.exists(location_dest+'Images_Disques/'+file):
                shutil.move(f'{location}{"/"}{file}', f'{location_dest}{"Images_Disques/"}{file}')
#Rename condition
if args.rename and args.location:
    location = args.location
    files = os.listdir(location)
    print(f'{"Your directory contain :"}{files}')
    renamer(files)
    print(f'{"Your files are now renamed : "}{os.listdir(location)}') 

#Sort and location specification condition
elif args.sorter and args.location:

    location = args.location
    os.chdir(location)
    print(location)
    print(f'{"The directory chosen : "}{location}')

    files = os.listdir(location)

    print(f'{"Your directory contain :"}{files}')

    sort_files()
    print(f'{"Your files have been sorted"}')

#Sort with default location condition
elif args.sorter and not args.location:

    os.chdir(f'{"/home/"}{user}{"/Téléchargements/"}')
    location = os.getcwd()
    print(location)
    print(f'{"Le directory par défaut sera choisi : "}{location}')

    files = os.listdir(location)

    print(f'{"Your directory contain :"}{files}')

    sort_files()

    print(f'{"Your files have been sorted"}')

#Rename condition with default location
elif args.rename and not args.location:   
    location = "/home/"+user+"/Téléchargements/"
    os.chdir(location)

    files = os.listdir(location)
    
    print(f'{"Your directory contain :"}{files}')
   
    renamer(files)
    
    print(f'{"Your files have been renamed : "}{os.listdir(location)}') 

else:
    print(f'{"Please choose one argument!"}')