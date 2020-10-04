# Birden fazla elemanla çalışacak ise, tek tek değişken tanımlamak yerine dizi kullaniyoruz.
# Tanımlama sekli
sehirler = ["istanbul" , "edirne" , "konya" , "rize" , "ankara" , "eskisehir" , "adana" , "kayseri"]


# # Not : Bir dizinin maksimum index degeri, o dizinin eleman sayisi (uzunlugu) 1- degeridir

#     # eleman sayi  => 1 2 3 4 5 6 7 8 => dizi icerisindeki toplam adet
#     # index degeri => 0 1 2 3 4 5 6 7 => dizi icerisinde yer alan, herhangi bir elemana ulasma sekli

# # print(sehirler[0]) # dizinin ilk elemanini ekrana yazdirdik


# # dizinin son elemanini ekrana yazdiriniz.

# a = len(sehirler)

# a = len(sehirler) - 1

# print(sehirler[a])

# print(sehirler[2 : 7])

# # dizinin tüm elemanlarını ekrana yazdırmak istersek ?

# print(sehirler[:])

# print('adana' in sehirler)  # adana dizi icerisinde gecmekte mi?

#Kullanici disaridan sehir adi girecek, var ise bu sehir dizi icerisinde yer almaktadir, yok ise, bu dizi sehir icerisinde yer almamaktadir mesaji veriniz.

il = input("Sehir adi giriniz : ")

mesaj = ""


# if il in sehirler:
#     mesaj = f"parametrede gönderdiginiz {il} sehri, dizi icerisinde almaktadir"
# else:
#     mesaj = f"parametrede gönderdiginiz {il} sehri, dizi icerisinde almamaktadir"

# print(mesaj)

# result = f"parametrede gönderdiginiz {il} sehri, dizi icerisinde almaktadir" if il in sehirler else f"parametrede gönderdiginiz {il} sehri, dizi icerisinde almamaktadir"

# ternary opt.

# kosul icerisinde true donerse, soldaki alan , false donerse sagdaki alan calisir.


print(f"parametrede gonderdiginiz {il} sehri, dizi icerisinde yer alma{ '' if il in sehirler else 'ma'}ktadir")

print("parametrede gonderdiginiz {} sehri, dizi icerisinde yer alma{}ktadır".format(il,("" if il in sehirler else "ma")))


myList1 = ["Sehirler Dizisi"]
print(myList1)

myList2 = ["Arabalar Dizisi"]
print(myList2)

myList3 = ["Renkler Dizisi"]
print(myList3)

result = list(zip(myList1, myList2, myList3))
print(result)
