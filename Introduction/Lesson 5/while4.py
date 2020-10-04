# 1 ile 1000 arasindaki tek sayilar ile çift sayilarin toplam adedini ekrana yazdiriniz.

i = 1

toplam1 = 0
toplam2 = 0

while (i <= 1000):
    if (i % 2) == 0:
        toplam1 += i
    else:
        toplam2 += i
    i += 1
print("Cift sayilarin toplami : ", toplam1)
print("Tek sayilarin toplami : ", toplam2)