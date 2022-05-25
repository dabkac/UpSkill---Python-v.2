import string
from typing import List


with open("C:\\Users\\kdabek\\Desktop\\UpSkill - Python\\dane_wejsciowe\\sprint1\\grades1.txt", "r") as file:
    for line in file:
        linesplited = line.strip().split(',')
        name = linesplited[0]
        print(str(name))
        liczby = linesplited[1:]
        all_oceny = []
        for x in liczby: 
            ocena = float(x)
            all_oceny.append(ocena)
        # print(all_oceny)
        dlugosc = len(all_oceny)
        suma = sum(all_oceny)
        avg = suma/dlugosc
        print(avg)

            # przypisanie sredniej do ucznia 
                        
            
            
            
        