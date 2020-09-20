# Ornek : Disaridan girilen kelimenin uzunlugu, 8 karaktere esit veya uzunsa, parola onaylandi kisa ise daha uzun bir sifre seciniz uyarisi verdiriniz.



sifre = input("Lutfen sifrenizi giriniz : ")

if (len(sifre) >= 8):
    print("Parola onaylandi")
else:
    print("Daha uzun bir sifre seciniz")
