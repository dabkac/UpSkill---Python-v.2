from os import makedirs
import string
from time import time
from typing import List
import datetime
nowtime = datetime.datetime.now()
print(nowtime.strftime("%H:%M %d.%m.%Y"))

with open("C:\\Users\\kdabek\\Desktop\\UpSkill - Python\\dane_wejsciowe\\sprint1\\grades1.txt", "r") as file:
    for line in file:
        linesplited = line.strip().split(',')
        name = linesplited[0]
        numbers = linesplited[1:]
        all_marks = []
        for x in numbers: 
            mark = float(x)
            all_marks.append(mark)
        lenght = len(all_marks)
        all = sum(all_marks)
        avg = all/lenght
        int_avg= int(avg)
        dictionary = {name : round(avg, 2)} 
        sorted_list_name = sorted(dictionary)
        #sorted_list_marks = sorted(int_avg)
        

        #sorted_list_marks = sorted(round(avg, 2))
        print(dictionary)
        print(sorted_list_name)
       # print(sorted_list_marks)
        
        
            # słowniki 
            # przypisanie sredniej do ucznia - przypisanie do jednej zmiennej, dać mozliwość wyboru , 
            # sortowanie po im i sredniej
            # w jaki sposób urzytkownik bedzie sortował
            # dokumentacja printa , połączenie w jednej lini
            # 
            
            
            
        
