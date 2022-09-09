import os
import shutil

fromDir = "C:/Users/rwgoe/Downloads"
toDir = "C:/Users/rwgoe/Desktop"

listOfFiles = os.listdir(fromDir)
#print(listOfFiles)

for fileName in listOfFiles:
    name, extension = os.path.splitext(fileName)

    if extension == "":
        continue

    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = fromDir +"/" +fileName
        path2 = toDir +"/" +"DocumentFiles"
        path3 = toDir +"/" +"DocumentFiles" +"/" +fileName

        if os.path.exists(path2):
            print("Moving " +fileName +"...")
            
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " +fileName +"...")

            shutil.move(path1, path3)