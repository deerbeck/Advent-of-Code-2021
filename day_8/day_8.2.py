import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\input_day_8.txt', "r") as inputfile:
    workingdata = inputfile.read()
    l1 = workingdata.split("\n")
    c = 0
    for element in l1:
        input = element.split("|")[0]
        signal = element.split("|")[1]
        wires = signal.split(" ")
        
    print(123)