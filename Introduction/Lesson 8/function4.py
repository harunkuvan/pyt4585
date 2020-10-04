# Disaridan bir sayisal dizi alacak, method parametredeki yer alan elemanlarin toplaminin karekokunu geriye teslim etsin.
import math


def toplam(sayilar):
    top = 0
    for sayi in sayilar:
        top += sayi
    return math.sqrt(top)


dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = toplam(dizi)
print(result)
