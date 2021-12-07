import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def lantfish_counter(lanternfish:list, days:int):
    newdayfish = []
    calcdays = days
    if calcdays > 0:
        for element in lanternfish:
            if element > 0:
                newdayfish.append(element-1)
            elif element == 0:
                newdayfish.append(8)
                newdayfish.append(6)
        return lantfish_counter(newdayfish, calcdays-1)
    else:
        return len(lanternfish)
        
        


with open(dir_path + '\input_day_6.txt', "r") as inputfile:
        workingdata = inputfile.read()
        l1 = list(map(int, workingdata.split(",")))
        days = 80
        print(lantfish_counter(l1, days))


