while True:    
   
    birinci_kahraman = input("____İlk Kahraman____\n Lütfen kahramanınızın adını yazın:")
    
    if len(birinci_kahraman) > 1:
        print ("Birinci kahramanın adı", birinci_kahraman.capitalize())
        break
    else:
        print("İsmin uzunluğu 1 karakterden uzun olmalıdır.")
        
# Birinci kahraman adını girdiğinde break komutuyla döngüden çıkacak, boş bıraktığında ise sürekli else içindeki komutu 
# yazdırarak birinci kahramanın ismini tekrar tekrar yazmasını isteyecek bir while döngüsü kullandım.        

# input kullanıcı girdisi ilk kahramanın adını girmesini sağlar.
# len ise uzunluk belirtmek için kullanılır. Mesela len(birinci_kahraman) demek birinci kahramanın harf sayısına tekabül eder.
# len(birinci_kahraman) birden büyükse if'in altındaki komut gerçekleşir. Birden büyük değilse else'in içindeki komut gerçekleşir.

while True:    
   
    ikinci_kahraman = input("____İkinci Kahraman____ \n Lütfen kahramanınızın adını yazın: ")
    
    if len(ikinci_kahraman) < 1:
        print("İsmin uzunluğu 1 karakterden uzun olmalıdır.")       
    elif ikinci_kahraman == birinci_kahraman:
        print ("{} alındı,lütfen başka bir isim seçin!".format(birinci_kahraman))

    else:
        print(("İkinci kahramanın adı"), ikinci_kahraman.capitalize()) #.capitalize komutu ilk harfi büyük harfe çevirir
        break

# İkinci kahraman adını girdiğinde break komutuyla döngüden çıkacak,birinci isme eşitse elif'in altındaki komutu yazdıracak,harf sayısı 1 den küçükse
# if'in altındaki komutu yazdıracak bir while döngüsü kullandım.

# input kullanıcı girdisi ikinci kahramanın adını girmesini sağlar.

# len ise uzunluk belirtmek için kullanılır. Mesela len(ikinci_kahraman) demek ikinci kahramanın harf sayısına tekabül eder.

# len(ikinci_kahraman) birden küçükse if'in altındaki komut gerçekleşir. Eğer ikinci kahramanın ismi ile birinci kahramanın ismi aynı ise
# elif'in altındaki komutu yazdıracak ve tekrardan bir isim girmesini isteyecek. Bu iki durum dışındaki durumlar için else ibaresini kullanırız.
# ve else kullandığımızda else'in altındaki komutu yazdırır. ve döngüden çıkar



key=True # key diye bir değişken atadım ve bunu boolean bir ifadeye eşitledim. Bunu yapmamın sebebi tekrar_istegi fonksiyonunu kurduğumda şartlara göre
         # döngüden çıkmayı ya da döngüye devam etmeyi sağlamak. True ise döngü devam edecek. False ise döngü duracak.

while(key): # Tüm hepsini while döngüsüne soktum. Çünkü fonksiyonların tekrar tekrar çalışması, oyuna tekrardan başlayabilmesi için bir döngüye girmesi gerekiyordu. 
     
    listele = [birinci_kahraman,ikinci_kahraman]   # listele adında bir liste açtım ve kahraman adlarını girdim.
    import random # random komutu kullanmak için import random yazdım.
    yazi_tura = random.choice(listele) # yazi_tura adında bir değişken atadım ve listele adlı listenin içinden rastgele bir isim seçmesini istedim.
    listele.remove(yazi_tura) # rastgele isim seçilince seçilen ismin listele adlı listeden silinmesini sağladım.
    isimler_arasi_bosluk=(70-len(yazi_tura))*" " # isimler_arasi_bosluk diye bir değişken atadım ve isimler arasındaki boşluğun sabit kalması için bir formül yazdım.
    

    print("Yazı turanın sonucu: {} önce başlar!".format(yazi_tura.capitalize())) # yazi_tura yazı turayı kazanan isimdir. Ve bunu print'in içine .formatla yazdırdım.
    print(yazi_tura.capitalize(),isimler_arasi_bosluk, "{}".format(listele[0].capitalize())) # sol tarafa yazı turayı kazanan kişinin adı sağ tarafa kaybeden kişinin adını yazdırdım.
    print("HP[100]:",50*"|","           ","HP[100]:",50*"|") # HP[100] ve 50 sopayla başlamasını printle sağladım.
    

    def birinci_saldiri(var_olan): # birinci_saldiri adında bir fonksiyon kurdum.
          
          print("----- {} Saldırı !!-----".format(yazi_tura.capitalize())) # yazı turayı kazanan kişinin saldırı yapmasını yazdırdım.
         
          hp2 = var_olan # hp2 diye bir değişken atadım ve fonksiyondaki argümana eşitledim.
          
          while True:
6            saldiri_buyuklugu = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
           
            # saldiri_buyuklugu adında bir değişken atadım ve integer(tam sayı) bir input kullanıcı girdisi açtım.
           
            if saldiri_buyuklugu > 50:
                print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
            elif saldiri_buyuklugu < 1:
                print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
            else:
               basari_yuzdesi = random.randint(0,100)
               olasilik = 100- basari_yuzdesi
               if  olasilik >= saldiri_buyuklugu :
                print("{} {} hasar verdi".format(yazi_tura.capitalize(),saldiri_buyuklugu))
                hp2 = hp2 - saldiri_buyuklugu
                return hp2
                
               else:
                print("Ooopsy! {} saldırıyı kaçırdı!".format(yazi_tura))
                return hp2

# Eğer saldiri_buyuklugu 50 den büyük ve 1 den küçükse if ve elif altındaki komutları yazdırmasını istedim. saldiri_buyuklugu 1 ve 50 arasında ise
# else durumuna girmesini istedim. Ve bunu bir while döngüsüne soktum.

# Else durumunda basari_yuzdesi adında bir değişken atadım ve 0 ile 100 arasında random bir sayı seçmesini istedim.Bu random sayıyı 100den çıkararak
# olasilik adındaki değişkene atadım ve eğer olasilik saldiri_buyuklugu ne eşit veya büyükse if'in altındaki komutu yazdırmasını istedim.
# Ve hp2 değerini saldiri büyüklüğünden çıkararak yeni bir hp2 dönüştürmesini istedim. Eğer olasilik saldiri_buyuklugunden eşit veya büyük değilse
# Else'in altındaki komutu yazdırmasını istedim. Ve yine hp2 yi dönüştürmesini istedim.


    
    def ikinci_saldiri(var_olan):
        print("-----{} Saldırı !!-----".format(listele[0].capitalize()))
       
        hp1=var_olan
        
        while True:
            saldiri_buyuklugu = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
            
            if int(saldiri_buyuklugu) > 50:
                print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
            elif saldiri_buyuklugu < 1:
                print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
            else:
                basari_yuzdesi = random.randint(0,100)
                olasilik = 100-basari_yuzdesi
                if  olasilik >= saldiri_buyuklugu :
                  print("{} {} hasar verdi".format(listele[0].capitalize(),saldiri_buyuklugu))
                  hp1 = hp1 - saldiri_buyuklugu
                  return hp1
                else:
                  print("Ooopsy! {} saldırıyı kaçırdı!".format(listele[0].capitalize()))
                  return hp1
              
# Eğer saldiri_buyuklugu 50 den büyük ve 1 den küçükse if ve elif altındaki komutları yazdırmasını istedim. saldiri_buyuklugu 1 ve 50 arasında ise
# else durumuna girmesini istedim. Ve bunu bir while döngüsüne soktum.

# Else durumunda basari_yuzdesi adında bir değişken atadım ve 0 ile 100 arasında random bir sayı seçmesini istedim.Bu random sayıyı 100den çıkararak
# olasilik adındaki değişkene atadım ve eğer olasilik saldiri_buyuklugu ne eşit veya büyükse if'in altındaki komutu yazdırmasını istedim.
# Ve hp1 değerini saldiri büyüklüğünden çıkararak yeni bir hp1 dönüştürmesini istedim. Eğer olasilik saldiri_buyuklugunden eşit veya büyük değilse
# Else'in altındaki komutu yazdırmasını istedim. Ve yine hp1 i dönüştürmesini istedim.
    
    def tekrar_istegi():
        key2 = True
        while (key2):
            print("Bir tur daha oynamak ister misiniz (Evet veya Hayır)? :")
            secim=input()
            secim=secim.capitalize()
            if secim=="Evet":
                key=True
                key2=False
            elif secim=="Hayır":
                key=False
                key2=False
                print("Oynadığınız için teşekkürler! Tekrar görüşürüz!")
            else:
                print("Hatalı seçim yaptınız.Lütfen tekrar deneyin!")
                key2=True
        return key    

# key2 adında bir değişken atadım ve bunu bir boolean ifadeye eşitledim eğer key2=True ise döngünün devam etmesini,key2=false ise döngünün bitmesini sağladım
       
# secim adında bir değişken atadım ve  input kullanıcı girdisi istedim. Ve girdiğim seçimin baş harfini büyüğe ve diğer harfleri küçüğe çevirebilmesi için .capitalize() kullandım.
# secim Evetse bütün döngüye devam edecek bunuda key= True ile sağlayacağız. secim Hayırsa döngü bitecek bunuda key=False ile sağlayacağız.
# Eğer evet veya hayırdan başka birşey girersek else durumu devreye girecek,Else'in altındaki komutu yazdıracak ve while (key2) döngüsüne tekrar girmemizi sağlayacak.
# secim=="Evet" de key2=False olması tekrar isteği fonksiyonundan çıkmak içindir.     
# secim=="Hayır" da key2=False olması tekrar isteği fonksiyonundan çıkmak içindir.
# while döngüsünün sonunda key'i tekrar döndürmesini istedim.       
    
    def ana_fonk(): # Şimdi yaptıklarımızı ana fonksiyonda yazdıracağız.
        
        hp1 = 100   # Olması gereken ilk değer 100 (daha sonra fonksiyonlarla azalacak.)
        hp2 = 100   # Olması gereken ilk değer 100 (daha sonra fonksiyonlarla azalacak.)
        
       
        while True:
            
            
            if hp1<=1 or hp2<=1:
               if hp1 < 1:
                   print("""########################################################
#########################""",yazi_tura.capitalize(),"""kazandı #####################
########################################################""")
                   key = tekrar_istegi()
                   break
               elif hp2 <1:
                   
                   print("""########################################################
#########################""",listele[0].capitalize(),"""kazandı ####################
########################################################""")
                   key = tekrar_istegi()
                   break
# Eğer hp1 değeri veya hp2 değeri birden küçük ya da eşitse altındaki komutları kullanacağız.
# Eğer hp1 değeri birden küçükse birinci_kahraman oyunu kazanır. Ve tekrar_istegi() fonksiyonunu çağırarak oyuncuya tekrar oynamak isteyip istemediği sorulur. Ve buradaki döngüden break komutuyla çıkar.
# Eğer hp2 değeri birden küçükse ikinci_kahraman oyunu kazanır. Ve tekrar_istegi() fonksiyonunu çağırarak oyuncuya tekrar oynamak isteyip istemediği sorulur. Ve buradaki döngüden break komutuyla çıkar.
                


            hp1 = birinci_saldiri(hp1) #birinci_saldiri fonksiyonunu çağırdım.
            
         
            if hp1<=0:
                 
                hp1=0
                cizgiler1=(hp1//2) * "|"  
                cizgiler2=(hp2//2) * "|"
                hp2_bosluk=(60-len(cizgiler2))*" "
               
                if 10<=hp2<=99:
                
                    hp2_bosluk=(61-len(cizgiler2))*" "
             
                elif hp2<10:
                  
                    hp2_bosluk=(62-len(cizgiler2))*" "
          
# Eğer hp1 değeri 0 dan küçük eşitse hp1 negatif olmasın diye 0 a eşitledim. cizgiler2 diye bir değişken atadım ve hp2 nin yarısını integer olarak sopayla çarpmasını istedim.
# hp2_bosluk cizgiler2 nin uzunluğunu 60 dan çıkararak boşlukla çarptım. Bu aradaki boşluğun sabit kalmasını sağlar.           

# Aradaki boşluğun sabit kalması için if açtım ve hp2 çift basamaklı iken 61 den cizgiler2 nin uzunluğunu çıkarıp boşlukla çarpmasını istedim. Eğer tek basamaklıya düşerse (Elif de bu şartı yazdım.) 
# 62 den çıkmasını ve boşlukla çarpılmasını istedim.         
               
                print(yazi_tura.capitalize(),isimler_arasi_bosluk, listele[0].capitalize())
                print("HP [{}]:".format(hp2),cizgiler2,hp2_bosluk, "HP [{}]:".format(hp1),cizgiler1) 
                print("""########################################################
#########################""",yazi_tura.capitalize(),"""kazandı ##################
########################################################""")
                key = tekrar_istegi()
                break
# İlk printte Yazı turayı kazanan sol tarafta kazanamayan sağ tarafta yazacak.                 
# İkinci printte HP leri ve boşlukları yazdırdım
# Üçüncü printte sağlanan şartlarda yazi_turanın kazanması gerekiyor. Kazananı yani yazi_turayı yazdırdım.Ve tekrar oynamak isteyip istemediğini sorması için tekrar_istegi() fonksiyonunu çağırdım. Ve döngüden çıktım.

            else:
               
                cizgiler1=(hp1//2) * "|"
                cizgiler2=(hp2//2) * "|"
                hp2_bosluk=(60-len(cizgiler2))*" "
             
                if 10<=hp2<=99:
                    
                    hp2_bosluk=(61-len(cizgiler2))*" "
                
                elif hp2<10:
                   
                    hp2_bosluk=(62-len(cizgiler2))*" "
               
                print(yazi_tura.capitalize(),isimler_arasi_bosluk, listele[0].capitalize())
                print("HP [{}]:".format(hp2),cizgiler2,hp2_bosluk, "HP [{}]:".format(hp1), cizgiler1) 

#Else durumunda sıfırdan büyük olduğu durumlar için bir inceleme yaptım.

# hp2_bosluk cizgiler2 nin uzunluğunu 60 dan çıkararak boşlukla çarptım. Bu aradaki boşluğun sabit kalmasını sağlar.           

# Aradaki boşluğun sabit kalması için if açtım ve hp2 çift basamaklı iken 61 den cizgiler2 nin uzunluğunu çıkarıp boşlukla çarpmasını istedim. Eğer tek basamaklıya düşerse (Elif de bu şartı yazdım.) 
# 62 den çıkmasını ve boşlukla çarpılmasını istedim.         
            
            hp2 = ikinci_saldiri(hp2) #ikinci_saldiri fonksiyonunu çağırdım.
            
            if hp2<0:
                hp2=0
                cizgiler1= (hp1//2) * "|"
                cizgiler2=(hp2//2) * "|"
                hp2_bosluk=(60-len(cizgiler2))*" "
                if 10<=hp2<=99:
                    hp2_bosluk=(61-len(cizgiler2))*" "
                elif hp2<10:
                    hp2_bosluk=(62-len(cizgiler2))*" "
                print(yazi_tura.capitalize(),isimler_arasi_bosluk, listele[0].capitalize())
                print("HP [{}]:".format(hp2), cizgiler2 ,hp2_bosluk, "HP [{}]:".format(hp1),cizgiler1) 
                print("""#############################################################
#########################""",listele[0].capitalize(),"""kazandı ######################
#############################################################""")
                key = tekrar_istegi()
                break
            else:
                cizgiler1=(hp1//2) * "|"
                cizgiler2=(hp2//2) * "|"
                hp2_bosluk=(60-len(cizgiler2))*" "
                if 10<=hp2<=99:
                    hp2_bosluk=(61-len(cizgiler2))*" "
                elif hp2<10:
                    hp2_bosluk=(62-len(cizgiler2))*" "
                print(yazi_tura.capitalize(),isimler_arasi_bosluk, listele[0].capitalize())
                print("HP [{}]:".format(hp2),cizgiler2 ,hp2_bosluk, "HP [{}]:".format(hp1), cizgiler1) 
                
        return key   #key'i döndürdüm.                      

# Eğer hp2 değeri 0 dan küçük eşitse hp2 negatif olmasın diye 0 a eşitledim. cizgiler2 diye bir değişken atadım ve hp1 nin yarısını integer olarak sopayla çarpmasını istedim.
# hp2_bosluk cizgiler2 nin uzunluğunu 60 dan çıkararak boşlukla çarptım. Bu aradaki boşluğun sabit kalmasını sağlar.           

# Aradaki boşluğun sabit kalması için if açtım ve hp2 çift basamaklı iken 61 den cizgiler2 nin uzunluğunu çıkarıp boşlukla çarpmasını istedim. Eğer tek basamaklıya düşerse (Elif de bu şartı yazdım.) 
# 62 den çıkmasını ve boşlukla çarpılmasını istedim.         
               

    key = ana_fonk()    #ana_fonk() çağırdım.

