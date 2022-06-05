gözlem_toplam = int(input("Gözlem Sayısı Giriniz: "))
yetenek_rating = {"A1":15,"A2":13,"B1":11,"B2":8,"C1":6,"C2":3,"D":0,"E1":-5,"E2":-10,"F1":-16,"F2":-22}    
çaba_rating = {"A1":13,"A2":12,"B1":10,"B2":8,"C1":5,"C2":2,"D":0,"E1":-4,"E2":-8,"F1":-12,"F2":-17}
çevre_rating = {"A":6,"B":4,"C":2,"D":0,"E":-3,"F":-7}
tutarlılık_rating = {"A":4,"B":3,"C":1,"D":0,"E":-2,"F":-4}
ortalama_tempo = 0
ortalama_süre = 0

for i in range(gözlem_toplam):
    i+=1
    gözlem_süresi = float(input("{}. Kişi İçin Gözlem Süresini Dakika Cinsinden yazınız...\n\n>>  ".format(i)))
    
    toplam = 0
    
    normal_tempo = 100
    
    çaba_kontrol = True
    
    yetenek_kontrol = True
    
    çevre_kontrol = True
    
    tutarlılık_kontrol = True
    
    
    çaba = input("{}. Kişi İçin Çaba Puanlarından Birisini giriniz...{}\n\n>>  ".format(i,çaba_rating.keys()))
    çaba=çaba.upper()
    while çaba_kontrol == True:
        if çaba in çaba_rating.keys():
            çaba = çaba_rating[çaba]
            toplam+=çaba
            çaba_kontrol=False
            break
        else:
            çaba=input("{}. Kişinin Çaba Puanınını Hatalı Girdiniz... Yandaki Verilerden Giriniz...{}\n\n>>  ".format(i,çaba_rating.keys()))
            çaba=çaba.upper()
        
    yetenek = input("{}. Kişinin Yetenek Puanlarından Birisini giriniz...{}\n\n>>  ".format(i,yetenek_rating.keys()))
    yetenek=yetenek.upper()
    while yetenek_kontrol == True:
        if yetenek in yetenek_rating.keys():
            yetenek = yetenek_rating[yetenek]
            toplam+=yetenek
            yetenek_kontrol=False
            break
        else:
            yetenek=input("{}. Kişinin Yetenek Puanınını Hatalı Girdiniz... Yandaki Verilerden Giriniz...{}\n\n>>  ".format(i,yetenek_rating.keys()))
            yetenek=yetenek.upper()
        
    çevre = input("{}. Kişinin Çevre Puanlarından Birisini giriniz...{}\n\n>>  ".format(i,çevre_rating.keys()))
    çevre=çevre.upper()
    while çevre_kontrol == True:   
        if çevre in çevre_rating.keys():
            çevre = çevre_rating[çevre]
            toplam+=çevre
            çevre_kontrol=False
            break
        else:
            çevre=input("{}. Kişinin Çevre Puanınını Hatalı Girdiniz... Yandaki Verilerden Giriniz...{}\n\n>>  ".format(i,çevre_rating.keys()))
            çevre=çevre.upper()
        
    tutarlılık = input("{}. Kişinin Tutarlılık Puanlarından Birisini giriniz...{}\n\n>>  ".format(i,tutarlılık_rating.keys()))
    tutarlılık=tutarlılık.upper()
    while tutarlılık_kontrol == True:
        if tutarlılık in tutarlılık_rating.keys():
            tutarlılık = tutarlılık_rating[tutarlılık]
            toplam+=tutarlılık
            tutarlılık_kontrol=False
            break
        else:
            tutarlılık=input("{}. Kişinin Tutarlılık Puanınını Hatalı Girdiniz... Yandaki Verilerden Giriniz...{}\n\n>>  ".format(i,tutarlılık_rating.keys()))
            tutarlılık=tutarlılık.upper()
        
    nihai_tempo = toplam + normal_tempo
    normal_süre =nihai_tempo*gözlem_süresi
    metin = "{}. Kişi için \nNihai Tempo : %{} \nNormal Süre: {}".format(i,nihai_tempo,normal_süre)
    print(metin)
    ortalama_tempo+=nihai_tempo
    ortalama_süre+=normal_süre
ortalama_tempo=ortalama_tempo/gözlem_toplam
ortalama_süre=ortalama_süre/gözlem_toplam


print(f"{gözlem_toplam} Tane Kişinin Ortalama Temposu: %{ortalama_tempo}\n                Ortalama süresi: {ortalama_süre}")