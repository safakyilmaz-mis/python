import os
from os import path
import shutil

mainPath = path.realpath("fileReader.py")
# Learning the real path of this py file

os.mkdir("results")
# Create a file in which we will put our result

textFile = open("results.txt","w+")
# Opening Txt file to write our result

size = 0

head,tail = mainPath.split("fileReader.py")
# We will seperate folder path and file path

listFolders = os.listdir(head)
# We want to learn folder location and we are choosing the head variable

textFile.write("Files list:\n--------------------------\n")
# files list in txt file

for i in range(len(listFolders)):
    # We want to add all files in txt file and we are using the len() function to get all files name
    textFile.write(listFolders[i])
    # Write all files name in txt file
    size += path.getsize(listFolders[i])
    # get sizes of all files
    textFile.write("\n")

textFile.write("\n--------------------------")
textFile.write("\nFiles size: ")
textFile.write(str(size)+" byte")
# size of files

textFile.close()
# After all processes we have to close the txt file with the close() function
shutil.move("results.txt",".\\results")
# and after closing we are moving our txt file into the "results" folder
