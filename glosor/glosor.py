def main():
    

    glosLista = {}

    print("-:glosor:-")
    antal_ratt = 0
    glosor = {}

    while True:
        svglosa = input("\n\tMata in svensk glosa: ")
        englosa = input("\n\tmata in engelsk glosa: ")

        glosor[svglosa] = englosa

        glosLista.update({svglosa : englosa})

        stoppa = input("\n\tVill du mata in en glosa till? j/n: ")
     
        if (stoppa == "n"):
            break

    while True:
        print("\n Nu start glosförhöret!")

        antal_ratt = 0

        for glosa in glosLista:
         svar = input(f"\n {glosa} : ")

         if svar == glosLista[glosa]:
            print("Rätt svar!")
            antal_ratt += 1
            print(f"\n{antal_ratt}")
         else :
            print(f"\nFel svar, det är {glosLista[glosa]}")
            print(f"\n{antal_ratt}")

        fortsatt2 = input("Vill du köra om? j/n: ")
        if fortsatt2 == "n":
            break
    

import os
import sqlite3
from sqlite3 import DataError

def main():
   Add_Glosor_To_Table()


def Add_Glosor_To_Table()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    sqliteConnection = sqlite3.connect("glosor.db")
    cursor =sqliteConnection.cursor()

    sqlite_insert_query = f"""INSERT INTO glosor (Sv, Eng) VALUES ('{svglosa}', '{englos}')"""
    cursor.execute(sqlite_insert_query)
    #stänger cursor
    cursor.close()
    #stänger connection
    sqliteConnection.close
            


main()