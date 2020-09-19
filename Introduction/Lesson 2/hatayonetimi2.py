try:
    sayi_bir = int(input("Lütfen 1. sayiyi giriniz : "))
    sayi_iki = int(input("Lütfen 2. sayiyi giriniz : "))

    toplam = sayi_bir + sayi_iki
    fark = sayi_bir - sayi_iki
    bolum = sayi_bir / sayi_iki
    carpim = sayi_bir * sayi_iki
    mod = sayi_bir % sayi_iki
    print(f"Sayilarin Toplam : {toplam}\nSayilarin Farki : {fark}\nSayilarin Bolumu : {bolum}\nSSayilarin Carpimi : {carpim}\nSayilarin Modu : {mod}")

except ValueError:
    print("ValueError")    
except ZeroDivisionError:
    print("")
except FileExistsError:
    print("")
except:
    print("Tüm hatalari kabul ediyorum, özür dilerim")