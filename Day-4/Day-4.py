import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputList = []
with open(os.path.join(__location__, 'Day-4-Input.txt')) as assignments:
    for line in assignments:
        newLine = line.translate({ord("\n"):None})
        split = newLine.split(",")
        append = []
        for i in split:
            append.append(i.split("-"))
        inputList.append(append)

encompass = 0
overlap = 0
for e in inputList:
    one1 = int(e[0][0])
    one2 = int(e[0][1])
    two1 = int(e[1][0])
    two2 = int(e[1][1])

    if ((one1<=two1) and (one2>=two2)) or ((two1<=one1) and (two2>=one2)):
        encompass += 1
        overlap += 1
    elif ((one1<=two1) and (two1<=one2)) or ((one1<=two2) and (two2<=one2)) or ((two1<=one1) and (one1<=two2)) or ((two1<=one2) and (one2<=two2)):
        overlap += 1

print(encompass, "pairs have an assignment that encompesses the other. ")
print(overlap, "assignment pairs overlap. ")
