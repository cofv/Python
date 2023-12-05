import random

# min_lista = ["Nej", "ja", "kanske"]

DeJa_lista = ["Verkligen ja", "100% ja", "Såklart!"] 
Jatro_lista = ["Troligen ja", "Jag tror det", "Som jag ser det ja"]
Kanske_lista = ["aeh k-kanske", "Får se, kanske", "Jag vet inte"]
Nej_lista = ["NEJ!", "Nej", "Verkligen inte"]

# print(random.choice(min_lista))

while True:
    Balls = input ("Do you wanna shake my balls???? ;) " )
    valj = random.randint(0,3)

    if valj == 0:
        print (random.choice(DeJa_lista))
    elif valj == 1:
        print (random.choice(Jatro_lista))
    elif valj == 2:
        print (random.choice(Kanske_lista))
    elif valj == 3:
        print (random.choice(Nej_lista))