import os
os.system('clear')

metin = input("Lütfen bir sayi giriniz : ")

i = 0
toplam = 0
a = 0

while (i < len(metin)):
    a = int(metin[i])
    toplam += a
    i += 1
print(f"Sayilarin toplami : {toplam}")