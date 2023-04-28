import os
import shutil
FileCount = 0
FolderCount = 0
dic = {}
left=[]

#Reads the File.txt and updates the dic Dictionary
try:
    file = open("FileExt.txt")
    for i in file.readlines():
        i = i.strip("\n").split(" : ")
        dic.update({i[1]: i[0]})    
except:
    pass

#Prints out the Supported File Extension
#print("\nValid File Extensions: ",end='')
#for i in dic.keys():
#    print(i,end=" ")
#print()

files = os.listdir()
path = os.getcwd()

for i in files:
    if i != "Organizer.py" and i!="FileExt.txt":
        file = i.split('.')                                          #Splits the File Name and Extension
        if len(file) >= 2:
            fileExt = file[1]
            if fileExt in dic.keys():                               #Checks the File Extension is supported 
                if not os.path.exists(path+"\\"+dic[fileExt]):      #Checks the Folder exists
                    os.mkdir(dic[fileExt])                          #Creates the Folder
                    FolderCount+=1
                shutil.move(path+"\\"+i,path+"\\"+dic[fileExt])     #Moves the File into the Folder
                FileCount+=1
            else:
                left.append(i)                                      

if len(left) != 0:
    print("Files Ignored: ")
    for i in left:
        print(i)

print(f"\nFiles Moved: {FileCount}\nFolder Created: {FolderCount}")