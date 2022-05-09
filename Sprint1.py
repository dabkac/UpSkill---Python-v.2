oceny = open("C:\\Users\\kdabek\\Desktop\\UpSkill - Python\\dane_wejsciowe\\sprint1\\grades1.txt", 'r')
print(oceny)
content = oceny.read()
print(content)
content_list = content.split("\n")
oceny.close()
print(content_list)

