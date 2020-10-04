# Kullanici input araciligi ile uygulamaya sayi girecek ve kullanici diledigi kadar sayi girebilir. Her sayi girildiginde kullaniciya yeni bir sayi girecek misin diye sorulacak. Kullanici y tusuna basarsa lütfen sayi giriniz diyip iceriye yeni sayi alinacak. y harici bir tusa basarsa iceride yer alan tek sayilarin en kucuk ve en buyuk sayisinin birbirine olan farkini geriye donsun.
def hesapla():
    liste = []
    liste2 = []
    while True:
        sayi = int(input("Lütfen sayi giriniz : "))
        liste.append(sayi)
        sonuc = input("Yeni bir sayi girecek misin? y/?")
        if sonuc.lower() == "y":
            continue
        else:
            # print(liste)
            for sayi in liste:
                if sayi % 2 == 1:
                    liste2.append(sayi)

        liste2.sort()
        # print(liste2)
        a = len(liste2)
        fark = liste2[a-1] - liste2[0]
        break
    return fark


result = hesapla()
print(result)
