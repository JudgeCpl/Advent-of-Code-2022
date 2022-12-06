input = open("Day-6-Input.txt", "r").readlines()

dataStream = [*input[0]]
found = False
pos = 14

while (len(dataStream)>13) and found==False:
    list = []
    for i in range(0, 14, 1):
        list.append(dataStream[i])
    if len(list) == len(set(list)):
        found = True
        print(pos)
    else:
        pos+=1
        dataStream.pop(0)