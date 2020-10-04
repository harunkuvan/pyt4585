# dictionary() key value formatinda datalari listelemek icin kullanilir. Json formatinda data tutar, WebApi (servisler), JavaScript, Angular, React (js-native), mongodb gibi bircok platform desteklemektdir.


personeller = [
    {
        "Id": 1,
        "firstname": "harun",
        "lastname": "kuvan",
        "mail": "harunkuvan@gmail.com",
        "phone": "5554443322"
    },
    {
        "Id": 2,
        "firstname": "mehmet",
        "lastname": "civelek",
        "mail": "mehmetcivelek@gmail.com",
        "phone": "5554443323"
    }
]

print(personeller[0])

kullanicilar = [
    {"username": "admin"},
    {"username": "ceo"},
    {"username": "moderator"}
]

print(kullanicilar[0])

# dictionary icerisinde yer alan bir kaydi guncellemek isterseniz

i = 0 #hangi eleman guncellenecek
key = "firstname"
value = "sahin"

oldRecord = personeller[i][key]
personeller[i][key] = value
newRecord = personeller[i][key]

print(oldRecord)
print(newRecord)

personeller.append({"Id": 3, "firstname": "sezgin", "lastname": "kaya", "mail": "sezginkaya@gmail.com", "phone":"658289"})
print(personeller)
