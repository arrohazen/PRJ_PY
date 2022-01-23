# PRJ_PY_UTC503 - File Renamer and sorter
The goal is to make a script for a school project.
# renommeur_fichiers.py
The script itself take in arguments to run differents functions.
# Build with
- VSCODE
- Python3.9.2
# Functions
- Rename files (Images and Music) with an incremental name (ex : Image_1.jpg, Image_2.png, Image_3.bmp)
- Delete spaces in files names
- Sort files and move them to their own directory (ex : Images in /home/<user>/Images ; Music in /home/<user>/Music ..ect)
  it sort : Images ; Musics ; Package(.deb, .pkg, .rpm...) ; Disk Images(.iso, .img, .vdi...) ; Archives(.zip, .tar, .xz...).
- If the directory does not exist, it create it.
# How to use
  Usage
  
    usage: renommeur_fichiers.py [-h] [-s] [-r] [-l LOCATION]

    Choose a function (sorter, renamer, )

    optional arguments:
      -h, --help            show this help message and exit
      -s, --sorter          Sorter of files by extension
      -r, --rename          Renaming files : replace spaces to -
      -l LOCATION, --location LOCATION
                            Giving a directory location
