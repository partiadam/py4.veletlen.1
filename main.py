"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""
from random import randint

szam = randint(1, 3)
beker = int(input('Adj meg egy számot: \t'))
if beker == szam:
    print('Eltaláltad!')
        
if beker > szam:
    print('Nagyobb az általad gondolt szám.')
if beker < szam:
    print('Kisebb az általad gondolt szám.')