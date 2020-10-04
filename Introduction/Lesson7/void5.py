# Parametre Alan Methodlar

# aldigi parametreye gore islem seyrini degistiren yapilardir.
# kural 1: Kesinlikle method icerisinde parametrenin nereden gelecegi tanimlanmaz
# kural 2: Kesinlikle method icerisinde parametreye deger atanmaz.

# Disaridan alinan 2 sayiyi ekrana yazdiran method:

def Hesapla(sayi1, sayi2):
    toplam = sayi1 + sayi2
    print(toplam)


Hesapla(10, 10)

s1 = int(input("Lütfen birinci sayiyi giriniz : "))
s2 = int(input("Lütfen ikinci sayiyi giriniz : "))

Hesapla(s1, s2)
