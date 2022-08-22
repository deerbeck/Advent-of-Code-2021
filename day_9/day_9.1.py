import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\input_day_9.txt', "r") as inputfile:
    workingdata1 = inputfile.read()
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
        if r == 0:
            for c in range(len(worklist[r])):
                checknum = worklist[r][c]
                if c == 0:
                    if checknum
                if c == len(worklist[r]):

                else:
        elif r == len(worklist):
            for c in range(len(worklist[r])):
                if c == 0:

                if c == len(worklist[r]):

                else:


print(worklist)
    