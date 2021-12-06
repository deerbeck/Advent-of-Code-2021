import os
testdata = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


### Selfwritten function to convert a binary number that is saved as a list of integers to a decimal number
## Maybe expanded to a function with string as input type
def bin_to_dec(binin):
    if type(binin) == list:
            
        bincalc = binin[::-1]
        dec = 0
        for i in range(len(bincalc)):
            dec += int(bincalc[i]) * 2**i
        return dec
    elif type(binin) == str:
        binlist = []
        for i in binin:
            binlist.append(i)
        bincalc = binlist[::-1]
        dec = 0
        for i in range(len(bincalc)):
            dec += int(bincalc[i]) * 2**i
        return dec

###Function to recursively search for the binary with the most common bit throughout every index
def find_most_common_bin(l2:list, index:int):
    nlistz = []
    nlisto = []
    zcnt = 0
    ocnt = 0
    if len(l2) == 1:
        return l2
    for element in l2:
        if element[index] == "0":
            zcnt += 1
            nlistz.append(element)
        elif element[index] == "1":
            ocnt += 1
            nlisto.append(element)
    if ocnt >= zcnt:
        return find_most_common_bin(nlisto, index+1)
    elif zcnt > ocnt:
        return find_most_common_bin(nlistz, index+1)

###Function to recursively search for the binary with the least common bit throughout every index
def find_least_common_bin(l2:list, index:int):
    nlistz = []
    nlisto = []
    zcnt = 0
    ocnt = 0
    if len(l2) == 1:
        return l2
    for element in l2:
        if element[index] == "0":
            zcnt += 1
            nlistz.append(element)
        elif element[index] == "1":
            ocnt += 1
            nlisto.append(element)
    if ocnt < zcnt:
        return find_least_common_bin(nlisto, index+1)
    elif zcnt <= ocnt:
        return find_least_common_bin(nlistz, index+1)

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '\input_day_3.txt', "r") as inputfile:
    workingdata = inputfile.read()
    l1 = workingdata.split("\n")
    oxy_gen_rating = find_most_common_bin(l1, 0)
    co_scr_rating = find_least_common_bin(l1, 0)

    print(oxy_gen_rating[0])
    print(co_scr_rating[0])

    l_sup_rating = bin_to_dec(oxy_gen_rating[0]) * bin_to_dec(co_scr_rating[0])
    print(l_sup_rating)