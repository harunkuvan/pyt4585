sayilar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# dizi icerisinde yer alan tek sayilari bir diziye cift sayilari ayri bir diziye ekleyiniz. islem sonunda toplamda dizi icerisinde kac eleman var kullaniciya bildirim veriniz.

i = 0 
tek_sayilar = []
cift_sayilar = []

while (i < len(sayilar)):
    if sayilar[i] % 2 == 0:
        cift_sayilar.append(sayilar[i])
    else:
        tek_sayilar.append(sayilar[i])
    i += 1
print(tek_sayilar)
print(cift_sayilar)
print("Tek sayilarin adedi : {}\nCift sayilarin adedi : {}".format(len(tek_sayilar),len(cift_sayilar)))
