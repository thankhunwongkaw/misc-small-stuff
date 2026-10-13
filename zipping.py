import zipfile
import os
import patoolib
z = r'C:\Users\thank\Documents\project\zip' # put your zipped obj here
unz = r'C:\Users\thank\Documents\project\unzip'
import shutil
print(shutil.which("7z"))

def unzip(file , ex):
    
    with zipfile.ZipFile(file , "r") as zip:
        print(f"extracted {file}")
        zip.extractall(ex)

for fold in os.listdir(z):
    foldp = os.path.join(z,fold)
    if fold.endswith(".zip"):
        print(foldp)
        
        unzip(foldp , unz)
    elif fold.endswith(".rar"):
        patoolib.extract_archive(foldp, outdir=unz)