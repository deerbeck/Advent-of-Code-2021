import os
dir_path = os.path.dirname(os.path.realpath(__file__))

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
## Maybe expanded to a function where u get a binary number written as an integer and not a list
def bin_to_dec(binin:list):
    bincalc = binin[::-1]
    dec = 0
    for i in range(len(bincalc)):
        dec += int(bincalc[i]) * 2**i
    return dec

with open(dir_path + '\input_day_3.txt', "r") as inputfile:
    workingdata = inputfile.read()
    l1 = workingdata.split("\n")
    gamma = []
    for i in range(len(l1[0])):
        zcnt = 0
        ocnt = 0
        for ele in l1:
            if ele[i] == "0":
                zcnt += 1
            elif ele[i] == "1":
                ocnt += 1
        if ocnt > zcnt:
            d = 1
        else:
            d = 0
        gamma.append(d)
    epsilon = []
    for num in gamma:
        if num == 0:
            epsilon.append(1)
        elif num == 1:
            epsilon.append(0)
    
    pcons = bin_to_dec(gamma) * bin_to_dec(epsilon)
    print(pcons)
