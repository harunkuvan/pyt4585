# Ornek : Disaridan kullanici not girisi saglayacak
# 0 - 30 => FF
# 31 - 50 => DD
# 51 - 70 => CC
# 71 - 84 => BB
# 85 - 100 => AA harf notu aldiniz uyarisi veriniz.

try:
    x = float(input("Lutfen notunuzu giriniz : "))

    if ((x < 0) or (x > 100)):
        print("Lufen 0,100 araliginda deger giriniz")
    elif (x >= 0) and (x <= 30):
        print("Notunuz : FF")
    elif (x >= 31) and (x <= 50):
        print("Notunuz : DD")
    elif (x >= 51) and (x <= 70):
        print ("Notunuz : CC")
    elif (x >= 71) and (x <= 84):
        print("Notunuz : BB")
    else:
        print("Notunuz : AA")
except Exception as ex:
    print(ex)
    print("Lutfen sayisal deger giriniz")