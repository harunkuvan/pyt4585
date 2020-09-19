try:
    #db connection open
    sayi = int(input("Lutfen sayi giriniz : "))
    #connection error
    print("Tebrikler bro")
    #db connection close (burada degil)
except:
    print("vazgectim")
    #db connection close (burada degil)
finally:
    print("her durumda bir defa tetiklenir")
    #db connection close (burada olmalı)
    #her iki durumda da yapilmasi gereken islemleriniz var ise bunu finally icerisinde yazmaniz kod tekrarini engelleyecektir.