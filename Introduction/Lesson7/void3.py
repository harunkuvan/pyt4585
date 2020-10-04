# 1000 ile 1 arasındaki sayilari ekrana yazdiran method yaziniz

def saydiriciWhile():
    i = 1000
    while i >= 1:
        print(i)
        i -= 1
saydiriciWhile()

def saydiriciFor():
    for sayi in range(1000,0,-1):
        print(sayi)
saydiriciFor()