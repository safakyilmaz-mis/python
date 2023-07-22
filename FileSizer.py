import os
from os import path
import shutil

mainPath = path.realpath("fileReader.py")
os.mkdir("results")
textFile = open("results.txt","w+")
size = 0

head,tail = mainPath.split("fileReader.py")
listFolders = os.listdir(head)
textFile.write("Files list:\n--------------------------\n")
for i in range(len(listFolders)):
    textFile.write(listFolders[i])
    size += path.getsize(listFolders[i])
    textFile.write("\n")

textFile.write("\n--------------------------")
textFile.write("\nFiles size: ")
textFile.write(str(size)+" byte")

textFile.close()
shutil.move("results.txt",".\\results")
