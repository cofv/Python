import random

frukter = ("Apelsin", "Banan", "Äpple", "Päron", "Kiwi")
looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print(f"\n {frukter[fnr-1]} kommer här\n")


while looping:
    print("-----------------------------")
    print("\n :FruktAutomat:-\n")

    i = 1
    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i += 1

    fruktnr = input("\nMata in siffra för vald frukt:")

    print_fruit(fruktnr)

    go = input("Vill du välja en frukt till j/n")
    print("\n")
    if (go =="n"):
        break


print("------------------------")
print("Föresten, du får en frukt till!")
slumpfruktnr = random.randint(1, 5)
print_fruit(slumpfruktnr)