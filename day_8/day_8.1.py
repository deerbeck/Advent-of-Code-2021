import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\input_day_8.txt', "r") as inputfile:
    workingdata = inputfile.read()
    l1 = workingdata.split("\n")
    c = 0
    segments = dict({"0": "abcefg", "1": "cf", "2": "acdeg", "3": "acdfg", "4": "bcdf", "5": "abdfg", "6": "abdefg", "7": "acf", "8": "abcdefg", "9": "abcdfg"})
    donenumbers = []
    

    for element in l1:
        input = element.split("|")[0]
        signal = element.split("|")[1]
        s_count = signal.split(" ")
        for s_ele in s_count:
            len_s_ele = len(s_ele)
            if len_s_ele == 2 or len_s_ele == 3 or len_s_ele == 4 or len_s_ele == 7:
                c += 1
print(c)