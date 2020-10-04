# Kullanici disaridan sifre girecek girilen sifre 3 ile 8 araliginda ise; sifreniz : sifre olarak ayarlandı.

# Kullanici üç denemenin sonunda beceremezse, motive edici bir mesaj veriniz.

for i in range(3):

    sifre = input("Sifrenizi 3 ile 8 karakter araliginda giriniz: ")

    if len(sifre) in range(3,8):
        print(f"Sifreniz : {sifre} olarak ayarlandi")
        break
    else:
        print("Sifreniz formata uygun degil")
if len(sifre) not in range(3,8):
    print("Mal mısın")


