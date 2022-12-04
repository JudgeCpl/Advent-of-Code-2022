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

cnt = 0
for e in inputList:
    one1 = int(e[0][0])
    one2 = int(e[0][1])
    two1 = int(e[1][0])
    two2 = int(e[1][1])

    if (one1<=two1) and (one2>=two2):
        cnt += 1
        print(e[0], "contains", e[1])
    elif (two1<=one1) and (two2>=one2):
        cnt += 1
        print(e[1], "contains", e[0])

print(cnt, "pairs have an assignment that encompesses the other")