with open('C:/Users/Johannes/OneDrive/Documents/PythonProgramming/projects/Advent of Code/Advent-of-Code-2021/day_2/input_day_2.txt', "r") as inputfile:
    input_data = inputfile.read()


    input_list = input_data.split("\n")

    print(input_list)

    aim=0
    h_pos = 0
    depth = 0
    for i in input_list:
        calcdata = i.split(" ")
        if calcdata[0] == "forward":
            h_pos += int(calcdata[1])
            depth  += int(calcdata[1]) * aim
        
        elif calcdata[0] == "down":
            aim += int(calcdata[1])
        
        elif calcdata[0] == "up":
            aim -= int(calcdata[1])

    endresult = depth * h_pos
    print(h_pos)
    print(depth)
    print(endresult)
