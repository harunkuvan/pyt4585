try:
    sayi1 = int(input("Lutfen sayi giriniz : "))
    sayi2 = int(input("Lutfen sayi giriniz : "))
    sonuc = sayi1 / sayi2

except ValueError as mahmud:
    print("İslem Hatasi")
else:
    try:
        print(sayi1/sayi2)
        print("İslem sonucu")
    except ZeroDivisionError as mahmud:
        print(mahmud)
