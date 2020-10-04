# Disaridan kullanicinin adini ve soyadini bir method yaziniz. Method aldigi bu degerleri bize mail adresi olustursun.

# Ornek murat.vuranok@bilgeadam.com

def mail(isim, soyisim):

    print(f"Mailiniz : {isim}.{soyisim}@hotmail.com")


adi = input("Lütfen adinizi giriniz:")
soyadi = input("Lütfen soyadinizi giriniz:")

mail(adi, soyadi)
