from random import randint
import os
os.system("clear")

sayilar = []

kolon = int(input("Lutfen kolon adedi giriniz : "))
i = 0



while (i < kolon):
    # sayilar = []
    j = 0    
    while (j < 6):
        sayi = randint (1,49)
        if sayi in sayilar:
            continue    
        else:
            sayilar.append(sayi)
        j += 1
    sayilar.sort()
    print(sayilar)
    sayilar.clear()
    i += 1 
