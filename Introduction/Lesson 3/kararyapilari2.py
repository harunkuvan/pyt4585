# Kullanici disaridan not degerini girecek ve girilen not 0'dan kucukse, 0'dan kucuk not giremezsiniz uyarisi, 100'den buyukse 100'den buyuk not girisi yapamazsiniz uyarisi, girilen no 0'a veya 100'e esit veya kucukse notu gosteriniz.


try:
    x = float(input("Lütfen notunuzu giriniz : "))
    
    if (x < 0):
        print("Sifirdan kucuk not giremezsiniz")
    elif (x > 100):
        print("Yuzden buyuk not giremezsiniz")
    else:
        print("Notunuz : ", x)
except ValueError as crn:
    print(crn)
    print("Sadece not gireceksin , ne kadar zor olabilir")

