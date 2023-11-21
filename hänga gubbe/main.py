word = input().upper()
temp = ""

for letter in word:
    if letter == " ":
        temp += "-"
    else:
        temp += "_"


print(temp)                                