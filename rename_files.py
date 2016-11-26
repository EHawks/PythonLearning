import os

def renameFiles():
    fileList = os.listdir(r"C:\Users\Elliott\Downloads\prank\prank")
    print(fileList)
    currentDir = os.getcwd()
    os.chdir("C:\Users\Elliott\Downloads\prank\prank")
    for fileName in fileList:
        os.rename(fileName, fileName.translate(None, "0123456789"))

    os.chdir(currentDir)

renameFiles();

