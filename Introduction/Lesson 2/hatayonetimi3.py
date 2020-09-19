try:
    sayi = int(input("Lutfen sadece sayisal deger giriniz : "))
    print("Gelen sayi : ", sayi)
    sayi = sayi / 0
    print("İslem sonucu : ")
except ValueError as ex:
    print("Lütfen tekrar deneyiniz")
    print("Sistem mesajı : ",ex)
except Exception as ex:
    print("İslem Hatasi")
    print("Sistem mesajı : ", ex)