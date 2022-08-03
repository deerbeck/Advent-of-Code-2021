import os
from regex import F

from sqlalchemy import false
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\input_day_8.txt', "r") as inputfile:
    workingdata = inputfile.read()
    # workingdata = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    #                 edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
    #                 fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    #                 fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
    #                 aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
    #                 fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
    #                 dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
    #                 bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
    #                 egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
    #                 gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    #workingdata = "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb"
    l1 = workingdata.split("\n")
    c = 0
    segments = dict({"0": "abcefg", "1": "cf", "2": "acdeg", "3": "acdfg", "4": "bcdf",
                    "5": "abdfg", "6": "abdefg", "7": "acf", "8": "abcdefg", "9": "abcdfg"})
    donenumbers = []
    sum = 0
    for element in l1:
        input = element.split("|")[0]
        signal = element.split("|")[1]
        wires = input.split(" ")
        elesegment = dict({"0": "", "1": "", "2": "", "3": "", "4": "",
                          "5": "", "6": "", "7": "", "8": "", "9": ""})
        # for i in range(len(wires)):
        for digits in wires:
            sdigits = sorted(digits)
            seg = len(digits)
            if seg == 2 and elesegment["1"] == "":
                elesegment["1"] = sdigits
            elif seg == 4 and elesegment["4"] == "":
                elesegment["4"] = sdigits
            elif seg == 3 and elesegment["7"] == "":
                elesegment["7"] = sdigits
            elif seg == 7 and elesegment["8"] == "":
                elesegment["8"] = sdigits

        for digits in wires:
            sdigits = sorted(digits)
            seg = len(digits)
            if seg == 6 and (elesegment["9"] == "" or elesegment["0"] == ""):
                if set(elesegment["4"] + elesegment["7"]).issubset(set(sdigits)) and set(elesegment["1"]).issubset(set(sdigits)) and elesegment["9"] == "":
                    elesegment["9"] = sdigits
                elif set(elesegment["1"] + elesegment["7"]).issubset(set(sdigits)) and elesegment["0"] == "":
                    elesegment["0"] = sdigits

        for digits in wires:
            sdigits = sorted(digits)
            seg = len(digits)
            if seg == 6 and (sdigits != elesegment["9"]) and (sdigits != elesegment["0"]):
                elesegment["6"] = sdigits

        for digits in wires:
            sdigits = sorted(digits)
            seg = len(digits)
            if seg == 5 and (elesegment["3"] == ""):
                if set(sdigits).issubset(set(elesegment["9"])) and set(elesegment["1"]).issubset(set(sdigits)):
                    elesegment["3"] = sdigits

        for digits in wires:
            sdigits = sorted(digits)
            seg = len(digits)
            if seg == 5 and (elesegment["5"] == "") and (elesegment["3"] != sdigits):
                if set(sdigits).issubset(set(elesegment["6"])):
                    elesegment["5"] = sdigits
                

        for digits in wires:
            sdigits = sorted(digits)
            seg = len(digits)
            if seg == 5 and (elesegment["2"] == "") and (elesegment["3"] != sdigits) and (elesegment["5"] != sdigits):
                elesegment["2"] = sdigits


        calcsignal = signal.split(" ")
        new_digits = []
        for i in range(len(calcsignal)):
            check_calc = sorted(list(calcsignal[i]))
            if check_calc == elesegment["0"]:
                new_digits.append("0")
            elif check_calc == elesegment["1"]:
                new_digits.append("1")
            elif check_calc == elesegment["2"]:
                new_digits.append("2")
            elif check_calc == elesegment["3"]:
                new_digits.append("3")
            elif check_calc == elesegment["4"]:
                new_digits.append("4")
            elif check_calc == elesegment["5"]:
                new_digits.append("5")
            elif check_calc == elesegment["6"]:
                new_digits.append("6")
            elif check_calc == elesegment["7"]:
                new_digits.append("7")
            elif check_calc == elesegment["8"]:
                new_digits.append("8")
            elif check_calc == elesegment["9"]:
                new_digits.append("9")
            elif check_calc == "":
                continue
        sum_string = ""
        sum += int(sum_string.join(new_digits))
print(sum)
              

