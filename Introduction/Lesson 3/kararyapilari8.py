try:
    adet = int(input("Kac adet kitap alacaginizi giriniz : "))

    if (adet <= 0):
        print("Lutfen gecerli bir deger giriniz")
    elif (adet >= 1) and (adet <= 20):
        deger = adet * 5 - adet * 5 * 0.05
        print("Yuzde 5 indirim kazandiniz")
        print("Tutar : ", deger)
    elif (adet >= 21) and (adet <= 50):
        deger = adet * 5 - adet * 5 * 0.1
        print("Yuzde 10 indirim kazandiniz")
        print("Tutar : ", deger)
    elif (adet >= 51) and (adet <= 80):
        deger = adet * 5 - adet * 5 * 0.15
        print("Yuzde 15 indirim kazandiniz")
        print("Tutar : ", deger)
    elif (adet >= 81) and (adet <= 100):
        print("Yuzde 20 indirim kazandiniz")
        deger = adet * 5 - adet * 5 * 0.2
        print("Tutar : ", deger)
    else:
        deger = adet * 5 - adet * 5 * 0.25
        print("Yuzde 25 indirim kazandiniz")
        print ("Tutar : ",deger)
except Exception as ex:
    print(ex)
    print("Lutfen sayisal deger giriniz")