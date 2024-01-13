# четыре однопалубных корабля,
# три двухпалубных корабля,
# два трёхпалубных корабля,
# один четырёхпалубный корабль
from collections import *

def counterShips() :
    spis  = []
    countKit = int(input("Введите количество вводимых наборов - "))
    for i in range(countKit):
        spis = [int(a) for a in input("Ведите набор чисел ").split()]
        if spis.count(4)==1 and spis.count(3)==2 and spis.count(2) == 3 and spis.count(1) == 4:    
            print("yes")
        else:
            print("No")
    

counterShips()