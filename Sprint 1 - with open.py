import string
from typing import List


with open("C:\\Users\\kdabek\\Desktop\\UpSkill - Python\\dane_wejsciowe\\sprint1\\grades1.txt", "r") as file:
    for line in file:
        # print(line)
        linesplited = line.strip().split(',')
        # print(linesplited)
        name = linesplited[0]
        print(str(name))
        liczby = linesplited[1:]
        for x in liczby: 
            oceny = (float(x))
            print(oceny)
        # srednia = sum(x)/len(x)
        # print(srednia)
        # oceny zmienic na liczb