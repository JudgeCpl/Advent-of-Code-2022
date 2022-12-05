input = open("Day-5-Input.txt", "r")
inputList = input.readlines()

instructionList = []
for line in inputList:
    line.strip('\n')
    split = line.split()
    instructionList.append([split[1], split[3], split[5]])

crates = [ ['B', 'S', 'V', 'Z', 'G', 'P', 'W'],  
['J', 'V', 'B', 'C', 'Z', 'F'], 
['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
['L', 'G', 'C', 'Z', 'V'],
['N', 'L', 'G'],
['J', 'F', 'H', 'C'] ]


for line in instructionList:
    limit = int(line[0])
    one = int(line[2])-1
    two = int(line[1])-1
    """
    cnt = 0
    while cnt < limit:
        crates[one].append(crates[two].pop())
        cnt += 1
    """
    while limit > 0:
        crates[one].append(crates[two].pop(-limit))
        limit -= 1


string = ""
for row in crates:
    string += row[-1]

print(string)