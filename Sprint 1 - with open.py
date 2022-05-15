with open("C:\\Users\\kdabek\\Desktop\\UpSkill - Python\\dane_wejsciowe\\sprint1\\grades1.txt", "r") as file:
    for line in file:
        # print(line)
        linesplited = line.strip().split(',')
        # print(linesplited)
        name = linesplited[0]
        print(name)
        oceny = linesplited[1:]
        print(oceny)
        # srednia = sum(oceny)/len(oceny)
        # print(srednia)