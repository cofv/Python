texten_innan = input("Man im here stroking my dick, stroking my shit: ")
(texten_innan.upper())
texten_efter = ""

for bokstav in texten_innan:
    if bokstav == "O" or bokstav == "A" or bokstav == "Y" or bokstav == "":
        texten_efter += "E"
    else:
        texten_efter += bokstav


print(texten_efter.upper())