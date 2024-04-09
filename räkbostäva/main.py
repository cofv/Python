dictionary = {
   
}

user_input = input("Skriv in något och jag räknar hur många av varje bokstav det finns. ").upper().replace(" ", "")


for letter in user_input:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1


print(dictionary)

