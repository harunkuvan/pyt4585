def seslisessiz(cumle):
    liste = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    seslisayilar = 0
    sessizsayilar = 0
    for i in cumle:
        if i in liste:
            seslisayilar += 1
        else:
            sessizsayilar += 1
    print(f"Sesli sayilar : {seslisayilar} \nSessiz sayilar : {sessizsayilar}")


metin = input("Lütfen cümle giriniz:").replace(" ", "").lower()
seslisessiz(metin)
