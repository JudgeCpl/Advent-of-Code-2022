import os

input = open("Day-7-Input.txt", "r").readlines()
path = ""

def addDir(path, dir):
    newDir = os.path.join(path, dir)
    if os.path.exists(newDir):
        print("Directory Found!")
    else:
        os.mkdir(newDir)

def addFile(path, file):
    newFile = os.path.join(path, file)
    if os.path.exists(newFile):
        print("File found!")
    else:
        file = open(newFile, "x")
        file.close()

for line in input:
    line = line.strip("\n")
    print(path)
    if line[0]=="$":
        if line=="$ cd /":
            addDir(path, "Dir")
            path = os.path.join(path, "Dir")
        elif line=="$ cd ..":
            path = os.path.dirname(path)
        elif line.__contains__("cd"):
            path = os.path.join(path, line[5::])
    else:
        if line[:3]=="dir":
            addDir(path, line[4::])
        else:
            addFile(path, line)