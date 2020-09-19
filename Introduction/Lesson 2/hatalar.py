# Programci Hatalari (Error)
# Program Kusurlari
# İstisnai Hatalar
# Mantıksal Hatalar

# telefonNumarasi = int(input("Lütfen telefon numarasi giriniz : "))
# print("Tebrikler, hayatta bir kez bile olsa basari sagladin!")


try :
    telefonNo = int(input("Lütfen telefon numarasi giriniz: "))
    print("Tebrikler")

except ValueError :
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except :
    print("İslem Hatasi")

