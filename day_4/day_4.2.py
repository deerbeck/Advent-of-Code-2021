import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '\input_day_4.txt', "r") as inputfile:
    workingdata = inputfile.read()
    l1 = workingdata.split("\n")
    bingonumbers = (list(map(int, l1.pop(0).split(","))))
    l2 = []
    for i in range(len(l1)):
        if l1[i] == "":
            continue
        l2.append(l1[i])
    l3 = []
    for element2 in l2:
        l3.append(element2.split(" "))
    
    for element in l3:
        for ele in element:
            if ele == "":
                element.remove(ele)
            else: 
                continue
    l4 = []
    for element in l3:
        l4.append(list(map(int, element)))
    
    bingolist = [[] for i in range(int(len(l4)/5))]

    for i in range(len(bingolist)):
        for i2 in range(5):
                bingolist[i].append(l4.pop(0))
    




    w_dict = dict()
    for b_ele in bingolist:
        p = 1000000
        columns = [[],[],[],[],[]]
        for i in range(5):
            for d in range(5):
                columns[i].append(b_ele[d][i])
        
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
                        break
                    elif n == p:
                        break
        

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
                        break
                    elif n == p:
                        break
        diagonal_ltop_rbot = []
        for i in range(5):
            diagonal_ltop_rbot.append(b_ele[i][i])
        diagonal_lbot_rtop = []
        for i in range(5):
            diagonal_lbot_rtop.append(b_ele[-(i+1)][i])
        
        c = 0
        n = 0
        for num in bingonumbers:
            n+=1
            if num in diagonal_ltop_rbot and c < 5:
                c+=1
            elif c == 5:
                if n < p:
                    p = n
                    n = 0
                    break
                elif n == p:
                    break
        for num in bingonumbers:
            n+=1
            if num in diagonal_ltop_rbot and c < 5:
                c+=1
            elif c == 5:
                if n < p:
                    p = n
                    n = 0
                    break
                elif n == p:
                    break
        w_dict[p-2] = b_ele
    biggest_key = 0
    for k, v in w_dict.items():
        if k > biggest_key:
            biggest_key = k
        else:
            continue
    print(biggest_key)
    print(w_dict[biggest_key])
    print(bingonumbers[biggest_key])
    print(123)