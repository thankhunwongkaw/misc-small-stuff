import zipfile
import os
import patoolib
import shutil
z = r'C:\Users\thank\Documents\project\unzip' # put your foledered obj here
unz = r'C:\Users\thank\Documents\project\unzip'
import shutil
print(shutil.which("7z"))

for fold in os.listdir(z):
    foldp = os.path.join(z,fold)
    if os.path.isdir(foldp):
        for file in os.listdir(foldp):
            filep = os.path.join(foldp,file)
            shutil.move(filep,unz)