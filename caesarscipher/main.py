alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

sentence = input("Input letters/words \n")
steps = int(input("input steps \n"))

result = ""

for letter in sentence:
    if letter == " ":
        result += " "
    else:   
        index = alphabet.index(letter)
        new_index = index + steps
        new_letter = alphabet[new_index]
        result += new_letter

print(result)