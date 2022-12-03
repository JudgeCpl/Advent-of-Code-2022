import os

# This __location__ variable provides a path to the directory the python file exists to help find the needed text file. 
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
elfArray = []
elfNum = 0
calorieTotal = 0

# This for loop takes the contense of the input file, uses the else function to total the calories an elf carries and then adds the elves number and calorie count to 
# the elfArray when a break in the file is found. 
with open(os.path.join(__location__, 'Day-1-Input.txt')) as inventory:
    for line in inventory:
        if (line == "\n"):
            elfNum += 1
            elfStats = [elfNum, calorieTotal]
            elfArray.append(elfStats)
            calorieTotal = 0
        else:
            calorieTotal += int(line.split("\n")[0])

# A small function to find the position of an elf in the array
def findPos(array, target):
    pos = 0
    cnt = 0
    for i in array:
        if i[0] == target:
            pos = cnt
        cnt += 1
    return pos

wantedElves = []
e = 0

# The for loop shifts through the whole elfArray comparing the elves calorie totals to find the highest value. 
# The while loop repeats this 3 times, removing the elf with the highest calorie total each time, to find the 3 elves with the highest calorie totals. 
while e < 3:
    wantedElf = 1
    for i in elfArray:
        pos = findPos(elfArray, wantedElf)
        if i[1] > elfArray[pos][1]:
            wantedElf = i[0]
            mostCalories = i[1]
    wantedElves.append([wantedElf, mostCalories])
    elfArray.pop(pos)
    e += 1

calorieSum = wantedElves[0][1] + wantedElves[1][1] + wantedElves[2][1]
print("Elf", wantedElves[0][0], "has", wantedElves[0][1], "calories.")
print("The three elves with the most calories, are carrying a total of", calorieSum, "calories!")