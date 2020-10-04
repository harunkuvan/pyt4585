# Disaridan girilen degerin tek veya cift olma durumunu kontrol ediniz.
# Girilen deger cift ise -1 degerini tek ise bir degerini sifir ise 0 degerini teslim eden method yaziniz

def tekcift(x):
    if x == 0:
        return 0
    elif x % 2 == 0:
        return -1
    else:
        return 1


y = int(input("Lütfen deger giriniz : "))
sonuc = tekcift(y)
print(sonuc)
