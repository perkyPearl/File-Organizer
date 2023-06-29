import os
import shutil

FileCount = 0
FolderCount = 0
dic = {}
Folders = []
left=[]
logs = []
#Reads the File.txt and updates the dic Dictionary
try:
    file = open("FileExt.txt")
    for i in file.readlines():
        i = i.strip("\n").split(" : ")
        Folders.append(i[0])
        dic.update({i[1]: i[0]})    
except:
    pass

while True:
    path = os.getcwd()
    files = [i for i in os.listdir() if i not in Folders]

    files.remove("Organizer.py")
    files.remove("FileExt.txt")

    inp = input('\nType "help" to list out all commands\n>> ').lower()

    if inp == 'start':
        for i in files:
            file = i.split('.')                                          #Splits the File Name and Extension
            if len(file) >= 2:
                fileExt = file[1]
                if fileExt in dic.keys():                               #Checks the File Extension is supported 
                    if not os.path.exists(path+"\\"+dic[fileExt]):      #Checks the Folder exists
                        os.mkdir(dic[fileExt])                          #Creates the Folder
                        FolderCount+=1
                    shutil.move(path+"\\"+i,path+"\\"+dic[fileExt])     #Moves the File into the Folder
                    FileCount+=1
                    logs.append(f"{i} -> {dic[fileExt]}")
                else:
                    left.append(i)                                      

        if len(left) != 0:
            print("\nFiles Ignored: ")
            for i in left:
                print(i)
        print(f"\nFiles Moved: {FileCount}\nFolder Created: {FolderCount}")
    
    elif inp == 'status':
        print("To be Sorted:")
        for i in files:
            print(i)

    elif inp == "logs":
        for i in logs:
            print(i)
    
    elif inp == "help":
        print('''
start   : To Sort/Move the Files According to the File Extensions mentioned in the FileExt.txt.
status  : To Printout the Files to that are going to be sorted.
logs    : To Printout the Which File moved where. For that Particular Session/Instance.
exit    : To Exit the Program.
        ''')
    elif inp == 'exit':
        print("Exited")
        break
    else:
        print("Invalid Command")