import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def lantfish_counter(x0, x1, x2, x3, x4, x5, x6, x7, x8, days):
    if days >0:
        x_8 = x0
        x_7 = x8
        x_6 = x7 + x0
        x_5 = x6
        x_4 = x5
        x_3 = x4
        x_2 = x3
        x_1 = x2
        x_0 = x1
        return lantfish_counter(x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, days-1)
    else:
        sum = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8
        return sum
    
    


with open(dir_path + '\input_day_6.txt', "r") as inputfile:
        workingdata = inputfile.read()
        l1 = list(map(int, workingdata.split(",")))
        days = 256
        x0 = 0
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        x6 = 0
        x7 = 0 
        x8 = 0
        for element in l1:
            if element == 0:
                x0 +=1
            elif element == 1:
                x1 +=1
            elif element == 2:
                x2 +=1
            elif element == 3:
                x3 +=1
            elif element == 4:
                x4 +=1
            elif element == 5:
                x5 +=1
            elif element == 6:
                x6 +=1
        
        
        
        
        print(lantfish_counter(x0, x1, x2, x3, x4, x5, x6, x7, x8, days))