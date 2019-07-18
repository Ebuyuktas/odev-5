#ödev 2
#sayı tahmin programı


sayi="1234"  
sayac=1 

while True:
    dogru=0
    yanlıs=-0
    tahmin=input("{}. Tahmininizi Giriniz: ".format(sayac))
    sayac+=1

    if sayi==tahmin:   
        print("tebrikler dogru sayiyi buldunuz")
        break
    elif not tahmin:
        print("boş gecmeyelim aub")
        continue
    elif tahmin.isdigit()==False:
        print("lütfen sadece sayı giriniz")
        continue
    elif len(tahmin)!=4:
        print("sadece dört haneli bir sayı girebilirsiniz!!")
        continue
    

    for i in tahmin:
        if i in sayi and tahmin.index(i)==sayi.index(i):  
            dogru+=1
        if i in sayi and tahmin.index(i)!=sayi.index(i):  
            yanlıs+=1
            
    print("+",dogru,"-",yanlıs)
