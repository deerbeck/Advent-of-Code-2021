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
        wires = input.split(" ")
        elesegment = dict({"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""})
        for i in range(len(wires)):
            for digits in wires:
                sdigits = sorted(digits)
                seg = len(digits)
                if seg == 2 and elesegment["1"] == "":
                    elesegment["1"]  = sdigits
                elif seg == 4 and elesegment["4"] == "":
                    elesegment["4"] = sdigits
                elif seg == 3 and elesegment["7"] == "":
                    elesegment["7"] = sdigits
                elif seg == 7 and elesegment["8"] == "":
                    elesegment["8"] = sdigits
                elif elesegment["1"] != "" and elesegment["4"] != "" and elesegment["7"] != "" and elesegment["8"] != "":
                    if seg == 6 and (elesegment["9"] == "" or elesegment["6"] == "" or elesegment["0"] == ""):
                        if set(elesegment["4"] + elesegment["7"]).issubset(set(sdigits)) and elesegment["9"] == "":
                            elesegment["9"] = sdigits
                        elif set(elesegment["4"] + elesegment["7"]).issubset(set(sdigits)) and set(elesegment["1"]).issubset(set(sdigits)) and elesegment["0"] == "" :
                            elesegment["0"] = sdigits
                        elif elesegment["6"] == "":
                            elesegment["6"] = sdigits
        print(123)