import os
import sys
import pathlib
import zipfile

dirName=input("Enter a dir name:")
if not os.path.isdir(dirName):
    print("No such directory")
    sys.exit(0)
curDir=pathlib.Path(dirName)
with zipfile.ZipFile('myzip.zip',mode='w') as archive:
    for file_path in curDir.rglob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curDir))
        
    if os.path.isfile("myzip.zip"):
        print("Successfully created")
    else:
        print("ERROR")