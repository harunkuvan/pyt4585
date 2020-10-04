# dışarıdan girilen sesli ve sessiz harfleri ayristiriniz ve bu kullaniciya toplam adetlerini gosteriniz.

sesliharf = ["a","e","ı","i","o","ö","u","ü"]

metinsesli = []
metinsessiz = []

metin = input("Lütfen bir cumle yaziniz : ")

i = 0

while (i < len(metin)):
    if (metin[i] in sesliharf):
        metinsesli.append(metin[i])
    else:
        metinsessiz.append(metin[i])
    i += 1
print(metinsesli)
print(metinsessiz)
print("Sesli harf sayisi : {}\nSessiz harf sayisi : {}".format(len(metinsesli),len(metinsessiz)))
    
