f = open("textprog.txt", "r", encoding="utf-8")
lines = f.readlines()

name = input("vilken person vill du ta bort från konversationen? Emma, Alex eller Sofia? ")

new_list = []



for line in lines:
    if line.split()[0] == name + ":":
        new_list.append(line)
file = open('namefile.txt', 'w', encoding="utf-8")
file.writelines(new_list)


print(new_list)





 



