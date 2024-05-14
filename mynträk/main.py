bengar = [20,9,5,2]
print("du har 20 enkrona, 9 tvåkron, 5 femkron och 2 tiokronor")

kost_int = int(input("Hur mycke kosta? "))
""" 
20 *1
9 *2
5 *5
2 * 10
20 + 18 +25 + 20 = 83
"""
def count_money(benga_lista):
    summa = 0
    summa += benga_lista[0] * 1
    summa += benga_lista[1] * 2
    summa += benga_lista[2] * 5
    summa += benga_lista[3] * 10

    return summa

def calc_kost(benga_lista, kostnad):
    tot_mon = count_money(benga_lista)
    if tot_mon >= kostnad:
        print("yo man you rich")
    else:
        print("nah you broke")


calc_kost(bengar, kost_int)
"""
print(count_money(bengar))
"""