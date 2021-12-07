import os
dir_path = os.path.dirname(os.path.realpath(__file__))



with open(dir_path + '\input_day_7.txt', "r") as inputfile:
    workingdata = inputfile.read()
    l1 = list(map(int, workingdata.split(",")))
    max_x = 0
    min_x = 10000000000
    for e in l1:
        if e > max_x:
            max_x = e
        elif e < min_x:
            min_x = e
        else:
            continue
    
    fuel_consumpt = 10000000000000000
    for i in range(max_x-min_x):
        f_buffer = 0
        for e in l1:
            f_buffer += abs((min_x + i) - e)
        if f_buffer < fuel_consumpt:
            fuel_consumpt = f_buffer
        else: continue
    
    print(fuel_consumpt)
    

