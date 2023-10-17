import os
import sqlite3
from sqlite3 import DataError

def main():
    add_dog_to_table()

def add_dog_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    hundnamn = input("Mata in hundnamn:")
    hundras = input("Mata in hundras:")

    sqliteConnection = sqlite3.connect("dogs.db")
    cursor =sqliteConnection.cursor()

    sqlite_insert_query = f"""INSERT INTO dogs (namn, ras) VALUES ('{hundnamn}', '{hundras}')"""
    cursor.execute(sqlite_insert_query)
    #stänger cursor
    cursor.close()
    #stänger connection
    sqliteConnection.close

main()