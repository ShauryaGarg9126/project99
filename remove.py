import os
import shutil
import time 

def main():
    deletedFolderCount = 0
    deletedFileCount = 0
    path = "/path to delete"
    days = 15
    seconds =time.time()- (days*24*60*60)
    if os.path.exists(path):
        for rootFolder,folders,files in os.walk(path):
            if seconds>=getfileAge(rootFolder):
                removeFolder(rootFolder)
                deletedFolderCount= deletedFolderCount+1
                break 
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder,folder)
                    if seconds>= getfileAge(folderPath):
                        removeFolder(folderPath)
                        deletedFolderCount= deletedFolderCount+1
                for file in files:
                     filePath = os.path.join(rootFolder,file)
                    if seconds>= getfileAge(filePath):
                        removeFile(filePath)
                        deletedFileCount= deletedFileCount+1

        else:
            if seconds>= getfileAge(path):
                removeFile(path)
                deletedFileCount = deletedFileCount+1
    else:
        print("File not found")
        deletedFileCount+=1
    print("Total number of folders deleted",deletedFolderCount)  
    print("Total number of files deleted",deletedFileCount)      

                            


