import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '\input_day_3.txt', "r") as inputfile:
    input = inputfile.read()
input1 = """00100
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

oxygen = list(numbers)
co2_scrubber = list(numbers)

for i in range(0, len(numbers[0])):
    one = 0
    zero = 0

    for ele in oxygen:
        buffer = list(ele)
        if int(buffer[i]) == 1:
            one += 1
        else:
            zero += 1
    if len(oxygen) > 1:
        if one >= zero:
            for ele in numbers:
                buffer = list(ele)
                try:
                    if int(buffer[i]) == 0:
                        oxygen.remove(ele)
                except:
                    continue
        else:
            for ele in numbers:
                buffer = list(ele)
                try:
                    if int(buffer[i]) == 1:
                        oxygen.remove(ele)
                except:
                    continue
    else:
        break

for i in range(0, len(numbers[0])):
    one = 0
    zero = 0

    for ele in co2_scrubber:
        buffer = list(ele)
        if int(buffer[i]) == 1:
            one += 1
        else:
            zero += 1
    if len(co2_scrubber) > 1:
        if zero <= one:
            for ele in numbers:
                buffer = list(ele)
                try:
                    if int(buffer[i]) == 1:
                        co2_scrubber.remove(ele)
                except:
                    continue
        else:
            for ele in numbers:
                buffer = list(ele)
                try:
                    if int(buffer[i]) == 0:
                        co2_scrubber.remove(ele)
                except:
                    continue
    else:
        break

oxycalc = list(oxygen[0])
co2calc = list(co2_scrubber[0])

oxycalc.reverse()
co2calc.reverse()

oxycalc_dec = 0
co2calc_dec = 0
for i in range(0, len(oxycalc)):
    oxycalc_dec += int(oxycalc[i])* (2**i)

for i in range(0, len(co2calc)):
    co2calc_dec += int(co2calc[i])* (2**i)

print(oxycalc_dec * co2calc_dec)
        
    