# Karar yapilari
# Karsilastirma Operatorleri

# == (esit esittir) soldaki degerin, sagdaki degere esit olma durumu
# 1 == 1 => true - if
# 1 == 2 => false - else

# != (esit degildir) soldaki degerin sagdaki degere esit olmama durumu
# 1 != 1 => false - else
# 1 != 2 => true - if

# > (buyuktur) soldaki degerin sagdaki degerden buyuk olma durumu
# 2 > 1 => true - if
# 1 > 2 => false - else

# < (kucuktur) soldaki degerin sagdaki degerden kucuk olma durumu
# 2 < 1 => false - else
# 1 < 2 => true - if

# >= (buyuk esit) soldaki degerin sagdaki degerden buyuk veya esit olma durumu
# 1 >= 1 => true - esit olma - if
# 2 >= 1 => true - buyuk olma - if
# 1 >=2 => false - else

# <= (kucuk esit) soldaki degerin sagdaki degerden kucuk veya esit olma durumu
# 1 <= 1 => true - esit olma - if
# 2 <= 1 => false - else
# 1 <=2 => true - kucuk olma - if 


username = input("Lutfen kullanici adinizi giriniz : ")
username = username.lower()\
.replace("ı","i")\
.replace("ç","c")\
.replace("ş","s")\
.replace("ö","o")\
.replace("ğ","g")\
.replace("ü","u")

print(username)

if (username == "admin"):
    print("Tebrikler, giris yaptiniz")
else:
    print("Kullanici adiniz yanlis")

