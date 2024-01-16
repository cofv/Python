
total_summa = 0
summa1 = 0
summa2 = 0
IS_player1 = True

spel21 = ("willkommen")




while total_summa < 21:
    player1 = int(input("player 1 will you add 1,2 or 3 to the total? "))
    total_summa += player1
    if player1 > 3 or player1 < 1:
        if player1 < 3:
            print("Too big number")
            total_summa = 30
    if player1 == 1 or 2 or 3:
        player1 + total_summa
    if total_summa == 21:
        print("player 2 wins!")

    player2 = int(input("player 2 will you add 1,2 or 3 to the total? "))
    total_summa += player2
    if player2 > 3 or player2 < 1:
        if player2 < 3:
            print("Too big number")
            total_summa = 30
    if player2 == 1 or 2 or 3:
        player2 + total_summa
    if total_summa == 21:
        print("player 2 wins!")

  
    if total_summa > 21:
        print("you botha lose nerds!!")

    
