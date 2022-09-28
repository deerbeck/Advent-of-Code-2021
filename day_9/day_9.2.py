import os
basinsizes = []
allcoordinates = []

def find_basinsize(sizeofmatrix, basincoordinates, currentbasinsize):
    basincoordinates.sort()
    currentbasinbuff = len(basincoordinates)


    for element in basincoordinates:
        r = element[0]
        c = element[1]
        maxrow = sizeofmatrix[0]-1
        maxcolumn = sizeofmatrix[1]-1
        checknum = worklist[r][c]

        try:
            if  int(worklist[r][c+1]) < 9 and int(worklist[r][c+1]) == int(checknum) + 1:
                if (r, c+1) not in basincoordinates:
                    basincoordinates.append((r, c+1))
                    allcoordinates.append((r, c+1))

            if int(worklist[r+1][c]) < 9 and int(worklist[r+1][c]) == int(checknum) + 1:
                if (r+1, c) not in basincoordinates:
                    basincoordinates.append((r+1, c))
                    allcoordinates.append((r+1, c))

            if int(worklist[r][c-1]) < 9 and int(worklist[r][c-1]) == int(checknum) + 1:
                if (r, c-1) not in basincoordinates:
                    basincoordinates.append((r, c-1))
                    allcoordinates.append((r, c-1))

            if int(worklist[r-1][c]) < 9 and int(worklist[r-1][c]) == int(checknum) + 1:
                if (r-1, c) not in basincoordinates:
                    basincoordinates.append((r-1, c))
                    allcoordinates.append((r-1, c))
        except:
            None

    basincoordinates.sort()
    currentbasinsize = len(basincoordinates)
    if currentbasinsize == currentbasinbuff:
        basinsizes.append(currentbasinsize)
    else:
        find_basinsize(sizeofmatrix, basincoordinates, currentbasinsize)


dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\input_day_9.txt', "r") as inputfile:
    workingdata = inputfile.read()
#     workingdata = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""

    buf_list = workingdata.split("\n")
    worklist = []
    datalist = []

    for element in buf_list:
        worklist.append(list(element))

    sizeofmatrix = [len(worklist), len(worklist[0])]

    for r in range(len(worklist)):
        # check first row for low points
        if r == 0:
            for c in range(len(worklist[r])):
                checknum = worklist[r][c]
                basincoordinates = [(r, c)]
                if c == 0:
                    if checknum < worklist[r+1][c] and checknum < worklist[r][c+1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)

                elif c == len(worklist[r])-1:
                    if checknum < worklist[r+1][c] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)
                else:
                    if checknum < worklist[r+1][c] and checknum < worklist[r][c+1] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)

        # check last row for low points
        elif r == len(worklist)-1:
            for c in range(len(worklist[r])):
                checknum = worklist[r][c]
                basincoordinates = [(r, c)]
                if c == 0:
                    if checknum < worklist[r-1][c] and checknum < worklist[r][c+1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)
                elif c == len(worklist[r])-1:
                    if checknum < worklist[r-1][c] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)
                else:
                    if checknum < worklist[r-1][c] and checknum < worklist[r][c+1] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)

        # check remaining numbers
        else:
            for c in range(len(worklist[r])):
                checknum = worklist[r][c]
                basincoordinates = [(r, c)]
                if c == 0:
                    if checknum < worklist[r-1][c] and checknum < worklist[r+1][c] and checknum < worklist[r][c+1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)
                elif c == len(worklist[r])-1:
                    if checknum < worklist[r-1][c] and checknum < worklist[r+1][c] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)
                else:
                    if checknum < worklist[r-1][c] and checknum < worklist[r+1][c] and checknum < worklist[r][c+1] and checknum < worklist[r][c-1]:
                        datalist.append(checknum)
                        if basincoordinates in allcoordinates:
                            continue
                        find_basinsize(sizeofmatrix, basincoordinates, 1)

    endsum = 0
    for element in datalist:
        endsum += int(element)+1
    basinsizes.sort(reverse=True)
    result = basinsizes[0] * basinsizes[1] * basinsizes[2]
    print(len(allcoordinates))
    #print(basinsizes)
    print(result)