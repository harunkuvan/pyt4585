import os
os.system('clear')


metin = input("Bir metin giriniz : ")

uzunluk = len(metin)

i = 0

while (i < uzunluk):
    print(metin[i])
    i += 1