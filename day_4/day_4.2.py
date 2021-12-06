import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def bingo_run(bingolist):
    p = 500
    w_element = []
    w_bingo = []
    for b_ele in bingolist:
        columns = [[],[],[],[],[]]
        for i in range(5):
            for d in range(5):
                columns[i].append(b_ele[d][i])
        


        ###Check which row wins the fastest!
        for ele in b_ele:
            c = 0
            n = 0
            for num in bingonumbers:
                n+=1
                if num in ele and c < 5:
                    c+=1
                elif c == 5:
                    if n < p:
                        p = n
                        n = 0
                        w_element = ele
                        w_bingo = b_ele
                        break
                    elif n == p:
                        break
        
        ###Check which column wins the fastest!
        for ele in columns:
            c = 0
            n = 0
            for num in bingonumbers:
                n+=1
                if num in ele and c < 5:
                    c+=1
                elif c == 5:
                    if n < p:
                        p = n
                        n = 0
                        w_element = ele
                        w_bingo = b_ele
                        break
                    elif n == p:
                        break
    print(p)
    if (len(bingolist)) > 1:
        bingolist.remove(w_bingo)
        return bingo_run(bingolist)
    else:
        return bingolist

with open(dir_path + '\input_day_4.txt', "r") as inputfile:
    workingdata = inputfile.read()
    l1 = workingdata.split("\n")
    bingonumbers = l1.pop(0).split(",")

    l2 = []
    for i in range(len(l1)):
        if l1[i] == "":
            continue
        l2.append(l1[i])
    l3 = []
    for element in l2:
        l3.append(element.split(" "))
    for element in l3:
        for ele in element:

            if ele == "":
                element.remove(ele)
            else: 
                continue

    bingolist1 = [[] for i in range(int(len(l2)/5))]

    for i in range(len(bingolist1)):
        for i2 in range(5):
                bingolist1[i].append(l3.pop(0))

    print(bingo_run(bingolist1))