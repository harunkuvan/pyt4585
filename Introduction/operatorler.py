# Aritmetik operatorler

# +, -, /, *, %, **

sayi1 = 120
sayi2 = 50

toplam = sayi1 + sayi2
print("islem sonucu" + " "*50 + str(toplam))


#disaridan girilen 2 sayinin toplamasi

sayi3 = int(input("Birinci sayi: "))
sayi4 = int(input("ikinci sayi: "))

toplam = sayi3 + sayi4
fark = sayi3 - sayi4
carpim = sayi3 * sayi4
bolum = sayi3 / sayi4
kalan = sayi3 % sayi4

print("Toplam : " + str(toplam), "\nFark : " + str(fark), "\nCarpim : " + str(carpim), "\nBolum : " + str(bolum), "\nKalan : " + str(kalan))