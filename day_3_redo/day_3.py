import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '\input_day_3.txt', "r") as inputfile:
    input1 = inputfile.read()
input = """00100
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

numbers = input.split("\n")

gamma = []
epsilon = []
for i in range(0, len(numbers[0])):
    one = 0
    zero = 0

    for ele in numbers:
        buffer = list(ele)
        if int(buffer[i]) == 1:
            one += 1
        else:
            zero += 1
    if one > zero:
        gamma.append(1)
        epsilon.append(0)

    else:
        gamma.append(0)
        epsilon.append(1)

gamma.reverse()
epsilon.reverse()

gamma_dec = 0
epsilon_dec = 0
for i in range(0, len(gamma)):
    gamma_dec += gamma[i]* (2**i)

for i in range(0, len(epsilon)):
    epsilon_dec += epsilon[i]* (2**i)

print(gamma_dec * epsilon_dec)
print(epsilon_dec)
        
    