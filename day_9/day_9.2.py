import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\input_day_9.txt', "r") as inputfile:
    #workingdata = inputfile.read()
    workingdata = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    buf_list = workingdata.split("\n")
    worklist = []
    datalist = []

    for element in buf_list:
        worklist.append(list(element))

    for r in range(len(worklist)):
        #check first row for low points
        if r == 0:
            for c in range(len(worklist[r])):
                checknum = worklist[r][c]
                if c == 0:
                    if checknum < worklist[r+1][c] and checknum < worklist[r][c+1]:
                        datalist.append(checknum)
                elif c == len(worklist[r])-1:
                    if checknum < worklist[r+1][c] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)
                else:
                    if checknum < worklist[r+1][c] and checknum < worklist[r][c+1] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)

        #check last row for low points
        elif r == len(worklist)-1:
            for c in range(len(worklist[r])):
                    checknum = worklist[r][c]
                    if c == 0:
                        if checknum < worklist[r-1][c] and checknum < worklist[r][c+1]:
                            datalist.append(checknum)
                    elif c == len(worklist[r])-1:
                        if checknum < worklist[r-1][c] and checknum < worklist[r][c-1]:
                            datalist.append(checknum)
                    else:
                        if checknum < worklist[r-1][c] and checknum < worklist[r][c+1] and checknum < worklist[r][c-1]:
                            datalist.append(checknum)
        #check remaining numbers
        else:
            for c in range(len(worklist[r])):
                checknum = worklist[r][c]
                if c == 0:
                        if checknum < worklist[r-1][c] and checknum < worklist[r+1][c] and checknum < worklist[r][c+1]:
                            datalist.append(checknum)
                elif c == len(worklist[r])-1:
                    if checknum < worklist[r-1][c] and checknum < worklist[r+1][c] and checknum < worklist[r][c-1]:
                            datalist.append(checknum)
                else:
                    if checknum < worklist[r-1][c] and checknum < worklist[r+1][c] and checknum < worklist[r][c+1] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)
    endsum = 0
    for element in datalist:
        endsum += int(element)+1
    print(endsum)
