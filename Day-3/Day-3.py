import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputList = []
cnt=0
with open(os.path.join(__location__, 'Day-3-Input.txt')) as stratergy:
    for line in stratergy:
        cnt+=1
        newLine = line.translate({ord("\n"):None})
        length = int(len(newLine) / 2)
        inputList.append([newLine[i:i+length] for i in range(0, len(newLine), length)])

cnt = 0
sharedItemsList = []
for i in inputList:
    cnt+=1
    letterFound = False
    for e in i[0]:
        if letterFound:
            break
        for f in i[1]:
            if (e == f):
                sharedItemsList.append(e)
                letterFound = True
                break

list = [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l'], ['m'], ['n'], ['o'], ['p'], ['q'], ['r'], ['s'], ['t'], ['u'], ['v'], ['w'], ['x'], ['y'], ['z'], ['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['G'], ['H'], ['I'], ['J'], ['K'], ['L'], ['M'], ['N'], ['O'], ['P'], ['Q'], ['R'], ['S'], ['T'], ['U'], ['V'], ['W'], ['X'], ['Y'], ['Z']]
cnt = 0
for i in list:
    cnt += 1
    list[cnt-1].append(cnt)

sumOfPriorities = 0
for i in sharedItemsList:
    for e in list:
        if i == e[0]:
            sumOfPriorities += e[1]
            break

print(sharedItemsList[0], sharedItemsList[1], sharedItemsList[2])
print("The sum of priorities is", sumOfPriorities)