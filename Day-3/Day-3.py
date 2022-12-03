import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputList = []
with open(os.path.join(__location__, 'Day-3-Input.txt')) as stratergy:
    for line in stratergy:
        newLine = line.translate({ord("\n"):None})
        length = int(len(newLine) / 2)
        inputList.append([newLine[i:i+length] for i in range(0, len(newLine), length)])

list = [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l'], ['m'], ['n'], ['o'], ['p'], ['q'], ['r'], ['s'], ['t'], ['u'], ['v'], ['w'], ['x'], ['y'], ['z'], ['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['G'], ['H'], ['I'], ['J'], ['K'], ['L'], ['M'], ['N'], ['O'], ['P'], ['Q'], ['R'], ['S'], ['T'], ['U'], ['V'], ['W'], ['X'], ['Y'], ['Z']]
cnt = 0
for i in list:
    cnt += 1
    list[cnt-1].append(cnt)

def findSumPriorities(sumList):
    sumOfPriorities = 0
    for i in sumList:
        for e in list:
           if i == e[0]:
              sumOfPriorities += e[1]
              break

    print("The sum of priorities is", sumOfPriorities)

"""
sharedItemsList = []
for i in inputList:
    letterFound = False
    for e in i[0]:
        if letterFound:
            break
        for f in i[1]:
            if (e == f):
                sharedItemsList.append(e)
                letterFound = True
                break
findSumPriorities(sharedItemList)
"""

teamSharedItemList = []
count = 0
while len(inputList) > 0:
    count += 1
    teamList = []
    cnt = 0
    while cnt < 3:
        teamList.append(inputList[0][0] + inputList[0][1])
        inputList.pop(0)
        cnt += 1

    letterFound = False
    for i in teamList[0]:
        if letterFound == True:
            break
        for o in teamList[1]:
            if letterFound == True:
                break
            for p in teamList[2]:
                if i == o == p:
                    teamSharedItemList.append(o)
                    letterFound = True
                    break
findSumPriorities(teamSharedItemList)