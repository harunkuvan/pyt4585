# Disaridan isim ve soyisim alan bir method yaziniz. method ilk parametredeki kelimenin ilk 2 harfini buyuk kalanini kucuk alsin 2. parametrenin ise hepsini kucuk alip a harflerini e ile degistirip bize @hotmail.com mail adresi olarak teslim etsin

def sacmasoru(x, y):

    if len(x) <= 2:  # girilen isim 2 veya daha az karakter ise
        x = x.upper()
    else:
        x = f"{x[0:2].upper()}{x[2:].lower()}"
    y = y.lower().replace("a", "e")

    return f"{x}.{y}@hotmail.com".replace(" ", "")


sonuc = sacmasoru("harun", "kuvan")
print(sonuc)
