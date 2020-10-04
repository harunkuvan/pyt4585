# dizi uzerinde islemler yapmak icin o nesneye ait methodlar kullanilir.

# .append() - dizi icerisine eleman eklemek icin kullanilir, JavaScript icin de gecerlidir.
# append() ekleme işlemini dizinin sonuna ekleyerek gerceklestirir.

sehirler = [] #bos dizi

sehirler.append("ankara")

sehirler.append("edirne")

sehirler.append("istanbul")

print(sehirler[:])



# .insert() - dizi icerisinde belirli bir alana veri eklemek icin kullanilir.

sehirler.insert(1,"bursa")

print(sehirler)


# .pop() - dizi icerisinden eleman silme, parametre verilirse, verilen index degerindeki elemanı, parametre verilmezse dizinin en son elemanini siler.

print(sehirler)

sehirler.pop(1)

print(sehirler)

sehirler.pop()

print(sehirler)

print(sehirler.pop())


arabalar = ["mercedes", "bmw", "range rover", "bugatti", "aston martin", "tofas", "kartal", "serce"]

# .remove() - dizi icerisinden eleman silmekle mukellef diger bir methodumuzdur, pop() methodundan farki birisi index mekanizmasi uzerinden silme islemi yaparken remove() object parametre alarak isleme devam eder.
# dizi icerisinde birden fazla ayni deger var ise, soldan saga ilk buldugu elemani siler.
# remove methodu, pop methodu gibi silinen elemani geriye etmez void methodtur.

print(arabalar[:])

print(arabalar.remove("tofas")) # geriye teslim etmez

print(arabalar[:])


# .sort() - dizi icerisinde yer alan elemanlari a'dan z'ye - 0'dan 9'a siralar.

print(arabalar)

arabalar.sort()

print(arabalar)

print(arabalar[::-1])

# .reverse() - dizi icerisindeki elemanlari siralamadan tersine cevirir.

print(arabalar)

arabalar.reverse()

print(arabalar)

# .len() - dizinin uzunlugunu teslim eder.

print(len(arabalar))

del arabalar # arabalar dizisini tamamen silmis olursunuz, bu satir derlendikten sonra alt satirlarda arabalar dizisine ulasamayacaksiniz.

print(arabalar) #silindigi icin hata verdi.

