with open("C:\\Users\\kdabek\\Desktop\\UpSkill - Python\\dane_wejsciowe\\sprint1\\grades1.txt", "r") as file:
    for line in file:
        print(line)
        linesplited = line.split()
        
        # line = [float(x) for x in line.split()]
        # print(line, line)