# Kullanicinin disaridan girdigi sayinin tek veya cift olma durumunu kontrol etme, sayi tek ise sayi tektir uyarisi cift ise sayi cifttir uyarisi veriniz.

try:
    y = int(input("Lutfen bir sayi giriniz : "))
    
    if ((y % 2) == 1):
        print("Sayi tek sayidir")
    else:
        print("Sayi cift sayidir")
except ValueError as vb:
    print(vb)
    print("Lutfen sayi girisi yapiniz")
