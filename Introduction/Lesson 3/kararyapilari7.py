urun = input("Lutfen urun adini giriniz : ").lower().replace(" ","")

if (urun == "domates") or (urun == "biber") or (urun == "patlican"):
    print("Sebze Reyonu")
elif (urun == "sampuan") or (urun == "parfum") or (urun == "deodorant"):
    print("Kozmetik Reyonu")
elif (urun == "cep telefonu") or (urun == "televizyon") or (urun == "bilgisayar") or (urun == "kulaklik"):
    print("Teknoloji reyonu")
else:
    print("Bu urun bizde bulunmamaktadir")