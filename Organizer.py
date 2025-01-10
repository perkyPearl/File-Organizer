import os
import shutil
import time
from datetime import datetime

path = os.path.join(os.path.expanduser("~"), "Downloads")
fileExtPath = os.path.join(path, "FileExt.txt")
logPath = os.path.join(path, "organizer_log.txt")

defaultExt = {
    "PDFs": ["pdf"],
    "Text Document": ["txt"],
    "Executables": ["exe"],
    "Images": ["png", "jpg", "jpeg", "webp"],
    "Videos": ["mp4"],
    "Audios": ["mp3", "m4a"]
}

extensionsDict = {}

def logWrite(event):
    with open(logPath, "a", encoding="utf-8") as logF:
        logF.write(f"{datetime.now()} - {event}\n")

if os.path.exists(fileExtPath):
    logWrite("Importing File Extensions from the FileExt.txt file.")
    with open(fileExtPath, "r", encoding="utf-8") as file:
        for line in file.readlines():
            parts = line.strip().split(" : ")
            if len(parts) == 2:
                folderName = parts[0].strip()
                extensions = parts[1].strip().split(",")
                extensionsDict[folderName] = [ext.strip() for ext in extensions]
    logWrite("File extensions imported successfully.")
else:
    with open(fileExtPath, "w", encoding="utf-8") as file:
        logWrite("No FileExt.txt file found. Creating with default configurations.")
        for folder, extensions in defaultExt.items():
            file.write(f"{folder} : {','.join(extensions)}\n")
    extensionsDict = defaultExt
    logWrite("Default FileExt.txt file created.")

def organize():
    files = os.listdir(path)
    
    for file in files:
        if file != "FileExt.txt" and file != "organizer_log.txt":
            filePath = os.path.join(path, file)
            
            if os.path.isdir(filePath):
                continue
            
            fileExt = file.split('.')[-1]
            
            moved = False
            for folder_name, extensions in extensionsDict.items():
                if fileExt in extensions:
                    folder_path = os.path.join(path, folder_name)
                    
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    shutil.move(filePath, os.path.join(folder_path, file))
                    logWrite(f"Moved {file} to {folder_name}/")
                    moved = True
                    break
            
            if not moved:
                misc_folder = os.path.join(path, "Miscellaneous")
                
                if not os.path.exists(misc_folder):
                    os.makedirs(misc_folder)
                
                shutil.move(filePath, os.path.join(misc_folder, file))
                logWrite(f"Moved {file} to Miscellaneous/")

print("Starting Organizer...")

while True:
    organize()
    time.sleep(10)