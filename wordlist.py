import itertools as t
import time
print("""
                 _    ____       _     _
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/
""")

print("""
Seçenekler : 
1.  Wordlist Oluştur
2.  Wordlist Oku
3.  Not
99. Kaynak
""")
while True : 

    try:

        a = input("Seçenek : ")

        if a == "1":
            try:


                chars = input("Karakterler : ")
                n1 = int(input("Başlama İndexi : "))
                n2 = int(input("Bitiş İndexi : "))
                f = input("Kaydedilecek isim (.txt) : ")



                if f == "" or f is None:
                    if n1==n2:
                        for i in t.product(chars,repeat=n1):
                            s = ''.join(i)
                            print(s)
                    


                    elif n2 > n1:
                        for i in range(n1,n2+1):
                            for l in t.product(chars,repeat=i):
                                s = ''.join(l)
                                print(s)

                    else:
                        print("Hata Oluştu !!!!")


                else:
                    with open(f,"w",encoding="utf-8") as file:
                        if n1 == n2:
                            for l in t.product(chars,repeat=n1):
                                s = ''.join(l)
                                file.write(s+"\n")

                        elif n2 > n1:
                            for i in range(n1,n2+1):
                                for l in t.product(chars,repeat=i):
                                    s = ''.join(l)
                                    file.write(s+"\n")
                        else:
                            print("Hata Oluştu !!!!")
            except:
                print("İşlem 1 Hata Oluştu !!!")

        elif a == "2":
            try:

                kelime = 1 

                dosya = input("Dosya adı (.txt) : ")

                süre = float(input("Bekleme Süresi : ")) 

                with open(dosya,"r",encoding="utf-8") as file:

                    for sözcük in file:

                        print(kelime,".",sözcük)

                        time.sleep(süre)

                        kelime += 1

                print("Satır Sayısı : ",(kelime - 1))
            except:
                print("İşlem 2 Hata Oluştu !!!")

        elif  a == "3":
            try:

                dosya = input("""
Dosya Adı (uzantısıyla giriniz) :
==>>> 
                """)
                time.sleep(0.6)
                with open(
                    dosya,
                    "w",
                    encoding="utf-8"
                ) as file :
                    print("""
Dosya Oluşturuldu !       
                    """)
                    yazı = input("Not :")
                    file.write(yazı)
                
                   
            except:
                print("İşlem 3 Hata Oluştu !!!")

        elif a == "exit" or a == "çıkış" or a == "q":
            print("Çıkış Yapılıyor.")
            time.sleep(0.8)
            print("Çıkış Yapılıyor..")
            time.sleep(0.8)
            print("Çıkış Yapılıyor...")
            time.sleep(0.8)
            break
        
        elif a == "99":
            time.sleep(1)
            print("coded by root@ebby")
            time.sleep(1)
            print("IG : emirkan_esme ")
            time.sleep(1)
            print("2003emirkanesme@gmail.com")
            time.sleep(2)
            print("""

                 _    ____       _     _
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/
            """)
            time.sleep(2)
        else:
            print("Geçerli Bir Değer Giriniz !!!")
        
    except:
        print("İlk Kolonda Hata Oluştu !")
