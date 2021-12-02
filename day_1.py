with open('C:/Users/Johannes/OneDrive/Documents/PythonProgramming/projects/Advent of Code/Advent-of-Code-2021/input_day_1.txt', "r") as inputfile:
    test1 = inputfile.read()


    test = []
    test = test1.split("\n")

    for i in range(len(test)):
        if i == 0:
            c = 0
        if test[i] > test[i-1]:
            c+=1
        else:
            continue

    print(c)

    newlist  = []
    for i in range(len(test)):
        if i+2 >= len(test):
            break
        else:
            s1 = int(test[i]) + int(test[i+1]) + int(test[i+2])
            newlist.append(s1)


    for i in range(len(newlist)):
        if i == 0:
            d = 0
        if newlist[i] > newlist[i-1]:
            d+=1
        else:
            continue

    print(d)