import os

input = open("Day-7-Input.txt", "r").readlines()
path = ""

def addDir(path, dir):
    newDir = os.path.join(path, dir)
    if os.path.exists(newDir)==False:
        os.mkdir(newDir)

def addFile(path, file):
    newFile = os.path.join(path, file)
    if os.path.exists(newFile)==False:
        file = open(newFile, "x")
        file.close()

def cntSize(path):
    cnt = 0
    for i in os.listdir(path):
        if i.__contains__(" "):
            e = i.split(" ")
            cnt += int(e[0])
        elif (i.__contains__("."))==False:
            e = os.path.join(path, i)
            eE = os.path.join(e, "count.txt")
            fCnt = open(eE, "r").readlines()
            cnt += int(fCnt[0])
    
    file = os.path.join(path, "count.txt")
    if os.path.exists(file)==False:
        cntFile = open(file, "x")
        cntFile.write(str(cnt))
        cntFile.close
    else:
        cntFile = open(file, "w")
        cntFile.write(str(cnt))
        cntFile.close

    if cnt < 100000:
        return cnt
    else:
        return 0

for line in input:
    line = line.strip("\n")
    #print(path)
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

total = 0
path = ""
for line in input:
    line = line.strip("\n")
    if line[0]=="$":
        if line=="$ cd /":
            path = os.path.join(path, "Dir")
            total += cntSize(path)
        elif line=="$ cd ..":
            path = os.path.dirname(path)
        elif line.__contains__("cd"):
            path = os.path.join(path, line[5::])
            total += cntSize(path)

print(total)