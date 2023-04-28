import os
import shutil
FileCount = 0
FolderCount = 0
dic = {}

try:
    file = open("FileExt.txt")
    for i in file.readlines():
        i = i.strip("\n").split(" : ")
        dic.update({i[1]: i[0]})    
except:
    pass

print("Valid File Extensions: ")

for i in dic.keys():
    print(i,end=" | ")

files = os.listdir()
path = os.getcwd()

for i in files:
    if i != "Organizer.py" and i!="FileExt.txt":
        file = i.split('.')
        if len(file) >= 2:
            fileExt = file[1]
            if fileExt in dic.keys():
                if not os.path.exists(path+"\\"+dic[fileExt]):
                    os.mkdir(dic[fileExt])
                    FolderCount+=1
            shutil.move(path+"\\"+i,path+"\\"+dic[fileExt])
            FileCount+=1

print(f"\n\nFiles Moved: {FileCount}\nFolder Created: {FolderCount}")