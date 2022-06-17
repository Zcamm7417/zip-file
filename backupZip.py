#This program back up your files and folder into a named zip folder just by calling the function 'backupToZip' defined.
import os, zipfile
from pathlib import Path
p = Path.home()
def backupToZip(backupFolder):
    backupFolder = os.path.abspath(backupFolder)
    number = 1
    while True:
        zipFilename = os.path.basename(backupFolder)+'_'+str(number)+'.zip'
        if os.path.exists(zipFilename):
            continue
        else:
            break
        number = number + 1
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    for foldername, subfolders, filenames in os.walk(backupFolder):
        print(f'Adding files in {foldername}...')
    backupZip.write(foldername)
    for filename in filenames:
        newBase = os.path.basename(backupFolder)+ '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue
        backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
#This is the point where you call the backupToZip() function
#eg.............................
#backupToZip('C:\\Users\\USER\\Desktop\\DoneMaterials')