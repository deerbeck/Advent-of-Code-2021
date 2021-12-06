from collections import Counter
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\input_day_5.txt', "r") as inputfile:
    workingdata = inputfile.read()
    l1 = workingdata.split("\n")

    l2 = []
    for element in l1:
        l2.append(element.split("->"))

    pointlist = []
    for element in l2:
        varRange = 0
        startpoint = element[0].split(",")
        endpoint = element[1].split(",")
        x1 = int(startpoint[0])
        y1 = int(startpoint[1])
        x2 = int(endpoint[0])
        y2 = int(endpoint[1])
        switchx = x2 - x1
        switchy = y2 - y1

        if switchx < 0 or switchy < 0:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        if x1 == x2:
            varRange = (y2-y1)+1
            vertical = True
        elif y1 == y2:
            varRange = (x2-x1)+1
            vertical = False

        for i in range(varRange):
            if vertical:
                bufferpoint = f"{str(x1)}/{str(y1+i)}"
                pointlist.append(bufferpoint)
            else:
                bufferpoint = f"{str(x1+i)}/{str(y1)}"
                pointlist.append(bufferpoint)
        
    print(len([item for item, count in Counter(pointlist).items() if count > 1]))