import os 

#This initial part finds the input document and puts it in an array.
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputList = []
with open(os.path.join(__location__, 'Day-2-Input.txt')) as stratergy:
    for line in stratergy:
        newLine = line.translate({ord("\n"):None})
        inputList.append(newLine.split(" "))

#print(inputList)

totalScore = 0
"""
# X/A = rock, Y/B = paper, Z/C = scissoers
for i in inputList:
    if i[1] == "X":
        totalScore += 1
        if i[0] == "A":
            totalScore += 3
        elif i[0] == "B":
            totalScore += 0
        else:
            totalScore += 6
    elif i[1] == "Y":
        totalScore += 2
        if i[0] == "A":
            totalScore += 6
        elif i[0] == "B":
            totalScore += 3
        else:
            totalScore += 0
    else:
        totalScore += 3
        if i[0] == "A":
            totalScore += 0
        elif i[0] == "B":
            totalScore += 6
        else:
            totalScore += 3
"""
# X = Loss, Y = Draw, Z = Win
for i in inputList:
    if i[1] == "X":
        totalScore += 0
        if i[0] == "A":
            totalScore += 3
        elif i[0] == "B":
            totalScore += 1
        else:
            totalScore += 2
    elif i[1] == "Y":
        totalScore += 3
        if i[0] == "A":
            totalScore += 1
        elif i[0] == "B":
            totalScore += 2
        else:
            totalScore += 3
    else:
        totalScore += 6
        if i[0] == "A":
            totalScore += 2
        elif i[0] == "B":
            totalScore += 3
        else:
            totalScore += 1

print("You're total score will be:", totalScore)