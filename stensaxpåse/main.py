import random
ppoints = 0
copoints = 0

while True:
    player = int(input("Sten(1), sax(2) eller påse(3) "))

    computer = random.randint(1,3)

    if player == computer:
        print ("Tie")

    if player == 1 and computer == 2:
        print ("Player wins!") 
        ppoints += 1

    if player == 2 and computer == 3:
        print ("Player wins!")
        ppoints += 1

    if player == 3 and computer == 1:
        print ("Player wins!")
        ppoints += 1

    if player == 1 and computer == 3:
        print ("Computer wins!")
        copoints += 1

    if player == 2 and computer == 1:
        print ("Computer wins!")
        copoints += 1

    if player == 3 and computer == 2:
        print ("Computer wins!")
        copoints += 1

    if player > 3 or player < 1:
        print ("only numba 1,2 or 3!!!")
    
    print("Spelare: ", ppoints, " Dator: ", copoints)