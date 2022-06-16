import pytesseract
import cv2

dosya_yolu = "C:\\Users\\Bora\\Downloads\\lfs-plaka.png"

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Bora\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

plaka_fotografi = cv2.imread(dosya_yolu)

plaka = pytesseract.image_to_string(plaka_fotografi)

def indirim(a):
    return a-(a*0.25) 

def hizcezasi():
    hizsiniri=int(input("Hız sınırını giriniz: "))
    hiz=int(input("Hızı giriniz: "))
    if (hizsiniri+(hizsiniri*0.10))>hiz :
        return print("Ceza uygulanmasını gerektirecek bir durum yoktur.")
    elif (hizsiniri+(hizsiniri*0.10))<hiz<=(hizsiniri+(hizsiniri*0.30)): 
        return print("51/2-a Ceza maddesi gereğince Hız sınırını %10 ile %30 arasında geçtiği için {} Plakalı araç sahibine 427₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse 320.25₺'ye indirim uygulanacaktır.".format(plaka))
    elif (hizsiniri+(hizsiniri*0.30))<hiz<=(hizsiniri+(hizsiniri*0.50)):
        return print("51/2-b Ceza maddesi gereğince Hız sınırını %30 ile %50 arasında geçtiği için {} Plakalı araç sahibine 888₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse 666₺'ye indirim uygulanacaktır.".format(plaka))
    elif (hizsiniri+(hizsiniri*0.50))<hiz:
        return print("51/2-c Ceza maddesi gereğince Hız sınırını %50’den fazla geçtiği için {} Plakalı araç sahibine 1823₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse 1367.25₺'ye indirim uygulanacaktır.".format(plaka))

ceza = input("İşlenen cezayı giriniz: ")

Hurdayacikarilanaracinislemleriniyapmamak=427
Sattigiaraciilgilikurumlarabildirmemek=3340
İhaledenalinanaraclardagereklibilgilerivermemek=427
Tescilplakasizarackullanmak=1823
Hurdabelgeliarackullanmak=3674
Aractaruhsatbulundurmamak=166
Plakayiyanlisyeretakmak=166 
Appplakakullanmak=750
Izinverilensuredeuygunplakatakmamak=1536
Araccinsinegorebelirlenensayidaplakatakmamak=750
Plakauzerindedegisiklikyapmak=750
Plakasizarackullanmak=3093
Baskaaracinplakasinikullanmak=9107
Sahteplakatakmak=9107
Gecicitescilislemleriyapmamak=427
Aractabulundurulmasigerekendonanimlaribulundurmamak=196
Mevzuataaykiriisikkullanmak=1823
Aracuzerindekirenkdegisikligiveyareklamyapistirmak=196
Gerekliisikdonanimlaricalismayanarackullanmak=196
Abartiegzozveyacamfilmikullanmak=427
Araccinsindebulundurulmasigereklidonanimlaribulundurmamak=196
Ticariaraclarintakografkullanmamasi=888
Lpgruhsataisletmemek=196
Araclaruzerindekidegisikliklerinuygunolmasi=1823
Muayenesizarackullanmak=427
Muayenesiolmadigiicintrafiktenmenedilenarackullanmak=888
Muayenedeagirkusurluarackullanmak=888
Ehliyetsizarackullanmak=3674
Ehliyetineelkonulmuskisilerinarackullanmasi=3674
Ehliyetiiptaledilmiskisilerinarackullanmasi=3674
Ehliyetsinifidisindaarackullanmak=1823
Gecerliliksuresibitenehliyetlearackullanma=739
Disulkeehliyetiylebelirlenensartlardisindaarackullanmak=739	
Surucusertifikasiniehliyetecevirmedenarackullanma=1823
Ikametadresinitescilbiriminebildirmemek=427
Ehliyetiyanindaolmadanarackullanmak=427
Hiziningerektirdigiserittearackullanmamak=427
Seritdegistirmedenoncegirecegiseritikontroletmemek=427
Tehlikelisekildeseritdegistirmek=427
Sureklisolseridikullanmak=427
Emniyetseridinikullanmak=1823
Makasatmak=1823
Tersyondearackullanmak=1823
Hayvansurulerinintasityolunacikmasiniengellememek=427
Polisindurihtarinauymamak=427
Kirmiziisiktagecmek=427
Trafiklevhalarinauymamak=196
Trafikguvenliginitehlikeyedusurmek=196
Alkolluarackullanmak=1823
Uyusturucumaddekullaniparackullanmak=9411
Alkolmetreyeuflememek=5224
Ticariarackullanmasurelerineuymamak=196
Kavsaklarayaklasirkenhızınıyavaslatmamak=196
Yolvetrafikdurumunagoredavranmamak=196
Ondekiaraclaguvenlimesafebirakmak=196
Konvoyhalindearaclararasindagereklimesafebirakmak=196
Sagadonuskurallarinauymamak=196
Soladonuskurallarinauymamak=196
Donelkavsaklarauymamak=196
Donelkavsaktageridonuskurallarinauymamak=196
Sagaveyasoladonusteyayalarayolvermemek=196
Hatalisollamayapmak=427
Sollamayapmaninyasakolduğuyerdesollamayapmak=427
Gecilmekurallarinauymak=196
Seritizlemevedegistirmekurallarinauymamak=196
Karsidangelenaracingecisinizorlastirmak=196
Yakintakip=196
Hizsinirinincokaltindaarackullanmak=196
Daryollardaaracsinifinagoregeciskolayligisaglamamak=196
Kavsaklardailkgecishakkinivermemek=196
Kontrollukavsaklardailkgecishakkinivermemek=196
Kontrolsuzkavsaklardailkgecishakkinivermemek=196
Yesilisikyansabileduraktrafiktekavsagagirmek=196
Kavsaklardaduraklamak=196
Aksineisaretolmasabilerayuzerindekiaracailkgecishakkinivermemek=196
Yolcuindirmebindirmekurallarinauymamak=196
Yerlesimyeridisindaparketmek=196
Tasıtyoluuzerindeduraklamak=196
Solseritteduraklamak=196
Yayagecidindeduraklamak=196
Kavsaklarabesmetrekaladuraklamak=196
Donemeclerdeduraklamak=196
Otobusduraklarindaduraklamak=196
Ikincisiradaduraklamak=196
Trafikisaretlerininaltindaduraklamak=196
Tasityoluuzerindeparketmek=196
Solseritteparketmek=196
Yayagecidindeparketmek=196
Kavsaklarabesmetrekalaparketmek=196
Donemeclerdeparketmek=196
Otobusduraklarindaparketmek=196
Ikincisiradaparketmek=196
Trafikisaretlerininaltinaparketmek=196
Izinverilenzamandisindaparketmek=196
Kamununfaydalandigialanlaringiriscikislarinaparketmek=196
Altveyaustgecitlerdeparketmek=196
Izinverilensuredenfazlaparketmek=196
Resmiaraclaraayrilmisalanlaraparketmet=196
Yayayollarinaparketmek=196
Engelliaracparkyerineparketmek=392
Araclardabulundurulmasigerekenisikdonanimlarinibulundurmamak=888
Gereklialanlardauzunfarlarikullanmamak=196
Aksamfarlariyakmamak=427
Arkakenarisiklarininfarlarlabirliktekullanilmasi=196
Sisfarlarinigereksizyerekullanmak=196
Donusisiklarinifarklianlamdakullanmak=196
Gecekarsilasmalarindaisiklarisondurmemek=196
Ondekiaracigecerkenkisasuredenfazlauzunisiklarikullanmak=196
Yonetmeligeaykiriisiklandırmayapmak=196
Sadeceparklambalariylaseyretmek=196
Tasimasiniriustundeyolcualmak=153
Dingilagirligindanfazlayukyuklemek=1665
Tehlikeolusturabileceksekildeyukyuklemek=408
Gerekliiznialmadantehlikelimaddetasimak=828
Ozeliznetabiolanyukleriizinalmadantasimak=828
Gabaridisiyuktasimak=1665
Yukukarayolunadusecekveyadegeceksekildeyukyuklemek=408
Egimliyollardadengeyibozacaksekildeyukyuklemek=408
Surucunungorusuneengelolacaksekildeyukyuklemek=408
Cekenvecekilenaraclardatedbiralmamak=408
Yoldenetimistasyonunagirmemek=3340
Kislastigikullanmamak=1138
Tehlikelimanevrayapmak=427
Yonetmeliktekibelirtilensartlardisindageriyedonmek=427
Donuslerdeniyetinibelliedeceksekildeisaretvermemek=427
Driftyapmak=9125
Yayalararahatsizlikvereceksekildesagseritiisgaletmek=196
Yarisduzenlemek=888
Gecisustunlugukurallarinauymamak=196
Cevreyirahatsizediciarackullanmak=196
Saygisizcaarackullanmak=196
Aractanbirseyleratmakveyadokmek=196
Arackullanirkenceptelefonuilekonusmak=427
Kavsakgiriscikislarindayayalarailkgecishakkinivermemek=888
Yayagecitlerindeyayalarailkgecishakkinivermemek=888
Okultasitindadurisaretineuymamak=427
Demiryolugecidindekurallarauymamak=427
Emniyetkemeritakmamak=196
Kasktakmamak=196
Trafikkazasindatedbiralmamak=427
Trafikkazasindaevraklarinivermemek=427
Trafikkazasindakarsitarafabilgivermemek=427
Trafikpolisiizinvermedenkazayerindenayrilmak=888
Aracsigortasınıyaptirmamak=196
Amacdisindaarackullanmak=1823
Belediyedenizinalmadanyolcutasimak=9125
Belediyedenizinalinasartlardisindayolcutasimak=3674
Belediyedenizinalınanbölgedisindayolcutasima=1823
Belediyedenalinanizinbitmesineragmenyolcutasima=1823

if  (ceza=="Hurdaya çıkarılan aracın işlemlerini yapmamak"):
    print("20/1-a/1 Ceza maddesi gereğince hurdaya çıkarılan aracın işlemleri yapılmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indciim iygulanaiaksır.".format(plaka,Hurdayacikarilanaracinislemleriniyapmamak,indirim(Hurdayacikarilanaracinislemleriniyapmamak))) 

elif (ceza=="Sattığı aracı ilgili kurumlara bildirmemek"):
    print("20/1-d Ceza maddesi gereğince satılan araç ilgili kurumlara bildirilmediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Sattigiaraciilgilikurumlarabildirmemek,indirim(Sattigiaraciilgilikurumlarabildirmemek)))  

elif (ceza=="İhaleden alınan araçlarda gerekli bilgileri vermemek"):
    print("20/1-d-8 Ceza maddesi gereğince ihaleden alınan araçlarda gerekli bilgiler verilmediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,İhaledenalinanaraclardagereklibilgilerivermemek,indirim(İhaledenalinanaraclardagereklibilgilerivermemek)))

elif (ceza=="Tescil plakasız araç kullanmak"):
    print("21/1 Ceza maddesi gereğince tescil plakasız araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Tescilplakasizarackullanmak,indirim(Tescilplakasizarackullanmak)))

elif (ceza=="Hurda belgeli araç kullanmak"):
    print("21/5 Ceza maddesi gereğince hurda belgeli araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Hurdabelgeliarackullanmak,indirim(Hurdabelgeliarackullanmak)))

elif (ceza=="Araçta ruhsat bulundurmamak"): 
    print("23/2-a Ceza maddesi gereğince araçta ruhsat bulundurulmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Aractaruhsatbulundurmamak,indirim(Aractaruhsatbulundurmamak)))

elif (ceza=="Plakayı yanlış yere takmak"):
    print("23/2-b Ceza maddesi gereğince plakanın yanlış yere takılmasından dolayı {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Plakayiyanlisyeretakmak,indirim(Plakayiyanlisyeretakmak)))

elif (ceza=="App plaka kullanmak"):
    print("23/3-a-1 Ceza maddesi gereğince app plaka kullanımından dolayı {} Plakalı araç sahibine {}₺ para cezası  uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Appplakakullanmak,indirim(Appplakakullanmak)))

elif (ceza=="İzin verilen sürede uygun plaka takmamak"):
    print("23/3-a-2 Ceza maddesi gereğince izin verilen süre içerisinde uygun plaka takılmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Izinverilensuredeuygunplakatakmamak,indirim(Izinverilensuredeuygunplakatakmamak)))
  
elif (ceza=="Araç cinsine göre belirlenen sayıda plaka takmamak"):
    print("23/3-b-1 Ceza maddesi gereğince araç cinsine göre belirlenen sayıda plaka kullanılmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Araccinsinegorebelirlenensayidaplakatakmamak,indirim(Araccinsinegorebelirlenensayidaplakatakmamak)))

elif (ceza=="Plaka üzerinde değişiklik yapmak"):
    print("23/3-c-1 Ceza maddesi gereğince plaka üzerinde değişiklik yapıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Plakauzerindedegisiklikyapmak,indirim(Plakauzerindedegisiklikyapmak)))

elif (ceza=="Plakasız araç kullanmak"):
    print("23/4 Ceza maddesi gereğince plakasız araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Plakasizarackullanmak,indirim(Plakasizarackullanmak)))

elif (ceza=="Başka aracın plakasını kullanmak"):
    print("23/5-a Ceza maddesi gereğince başka aracın plakası kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Baskaaracinplakasinikullanmak,indirim(Baskaaracinplakasinikullanmak)))

elif (ceza=="Sahte plaka takmak"):
    print("23/5-b Ceza maddesi gereğince sahte plaka takıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Sahteplakatakmak,indirim(Sahteplakatakmak)))

elif (ceza=="Geçici tescil işlemleri yapmamak"):
    print("25 Ceza maddesi gereğince geçici tescil işlemleri yapılmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gecicitescilislemleriyapmamak,indirim(Gecicitescilislemleriyapmamak)))

elif (ceza=="Araçda bulundurulması gereken donanımları bulundurmamak"):
    print("26/1 Ceza maddesi gereğince araçda bulundurulması gereken donanımların bulundurulmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Aractabulundurulmasigerekendonanimlaribulundurmamak,indirim(Aractabulundurulmasigerekendonanimlaribulundurmamak)))

elif (ceza=="Mevzuata aykırı ışık kullanmak"):
    print("26/2 Ceza maddesi gereğince mevzuata aykırı ışık kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Mevzuataaykiriisikkullanmak,indirim(Mevzuataaykiriisikkullanmak)))

elif (ceza=="Araç üzerinde renk değişikliği veya reklam yapıştırmak"):
    print("26/3 Ceza maddesi gereğince araç üzerinde renk değişikliği veya reklam yapıştırıldığından dolayı {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Aracuzerindekirenkdegisikligiveyareklamyapistirmak,indirim(Aracuzerindekirenkdegisikligiveyareklamyapistirmak)))

elif (ceza=="Gerekli ışık donanımı çalışmayan araç kullanmak"):
     print("30/1-a Ceza maddesi gereğince gerekli ışık donanımı çalışmayan araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gerekliisikdonanimlaricalismayanarackullanmak,indirim(Gerekliisikdonanimlaricalismayanarackullanmak)))

elif (ceza=="Abartı egzoz veya cam filmi kullanmak"):
    print("30/1-b Ceza maddesi gereğince abartı egzoz veya cam filmi kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Abartiegzozveyacamfilmikullanmak,indirim(Abartiegzozveyacamfilmikullanmak)))

elif (ceza=="Araç cinsinde bulundurulması zorunlu gereçleri bulundurmamak"):
    print("31/1-a Ceza maddesi gereğince araç cinsinde bulundurulması zorunlu olan gereçlerin bulundurulmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Araccinsindebulundurulmasigereklidonanimlaribulundurmamak,indirim(Araccinsindebulundurulmasigereklidonanimlaribulundurmamak)))

elif (ceza=="Ticari araçların takoğraf kullanmaması"):
    print("31/1-b Ceza maddesi gereğince ticari aracın takoğraf kullanmadığı gerekçesiyle {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ticariaraclarintakografkullanmamasi,indirim(Ticariaraclarintakografkullanmamasi)))

elif (ceza=="30 gün içerisinde lpg ruhsata işletmemek"):
    print("32/1 Ceza maddesi gereğince 30 gün içerisinde lpg ruhsata işletilmediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Lpgruhsataisletmemek,indirim(Lpgruhsataisletmemek)))

elif (ceza=="Araçlar üzerindeki değişikliklerin uygun olmaması"): 
    print("32/3 Ceza maddesi gereğince araç üzerindeki değişikliklerin uygun olmaması sebebiyle {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Araclaruzerindekidegisikliklerinuygunolmasi,indirim(Araclaruzerindekidegisikliklerinuygunolmasi)))

elif  (ceza=="Muayenesiz araç kullanmak"):
    print("34/a Ceza maddesi gereğince muayenesiz araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Muayenesizarackullanmak,indirim(Muayenesizarackullanmak)))

elif (ceza=="Muayenesi olmadığı için trafikten men edilen araç kullanmak"):
    print("34/b Ceza maddesi gereğince muayenesi olmadığı için trafikten men edilen araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Muayenesiolmadigiicintrafiktenmenedilenarackullanmak,indirim(Muayenesiolmadigiicintrafiktenmenedilenarackullanmak)))

elif (ceza=="Muayenede ağır kusurlu olan aracı kullanmak"):
    print("34/c Ceza maddesi gereğince muayenede ağır kusurlu olan aracın kullanıldığı gerekçesiyle {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Muayenedeagirkusurluarackullanmak,indirim(Muayenedeagirkusurluarackullanmak)))

elif (ceza=="Ehliyetsiz araç kullanmak"):
    print("36/3-a Ceza maddesi gereğince ehliyetsiz araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ehliyetsizarackullanmak,indirim(Ehliyetsizarackullanmak)))

elif (ceza=="Ehliyetine el konulmuş kişilerin araç kullanması"):
    print("36/3-b Ceza maddesi gereğince ehliyetine el konulmuş kişinin araç kullandığı gerekçesiyle {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ehliyetineelkonulmuskisilerinarackullanmasi,indirim(Ehliyetineelkonulmuskisilerinarackullanmasi)))

elif (ceza=="Ehliyeti iptal edilmiş kişilerin araç kullanması"):
    print("36/3-c Ceza maddesi gereğince ehliyeti iptal edilmiş kişinin araç kullandığı gerekçesiyle {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ehliyetiiptaledilmiskisilerinarackullanmasi,indirim(Ehliyetiiptaledilmiskisilerinarackullanmasi)))

elif (ceza=="Ehliyet sınıfı dışında araç kullanmak"):
    print("39/2 Ceza maddesi gereğince ehliyet sınıfı dışında araç kullanıldığı gerekçesiyle {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ehliyetsinifidisindaarackullanmak,indirim(Ehliyetsinifidisindaarackullanmak)))

elif (ceza=="Geçerlilik süresi biten ehliyetle araç kullanmak"):
    print("39/3 Ceza maddesi gereğince geçerlilik süresi biten ehliyetle araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gecerliliksuresibitenehliyetlearackullanma,indirim(Gecerliliksuresibitenehliyetlearackullanma)))

elif (ceza=="Dış ülke ehliyetiyle belirlenen şartlar dışında araç kullanmak"):
    print("39/4 Ceza maddesi gereğince dış ülke ehliyetiyle belirlenen şartlar dışında araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Disulkeehliyetiylebelirlenensartlardisindaarackullanmak,indirim(Disulkeehliyetiylebelirlenensartlardisindaarackullanmak)))

elif (ceza=="Sürücü sertifakasını ehliyete dönüştürmeden araç kullanmak"):
    print("42/11 Ceza maddesi gereğince sürücü sertifakasını ehliyete dönüştürmeden araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Surucusertifikasiniehliyetecevirmedenarackullanma,indirim(Surucusertifikasiniehliyetecevirmedenarackullanma)))

elif (ceza=="İkamet adresini tescil birimine bildirmemek"):
    print("44/1-a Ceza maddesi gereğince ikamet adresini tescil birimine bildirilmediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ikametadresinitescilbiriminebildirmemek,indirim(Ikametadresinitescilbiriminebildirmemek)))

elif (ceza=="Ehliyeti yanında olmadan araç kullanmak"):
    print("44/1-b Ceza maddesi gereğince ehliyeti yanında olmadan araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ehliyetiyanindaolmadanarackullanmak,indirim(Ehliyetiyanindaolmadanarackullanmak)))

elif (ceza=="Hızının gerektirdiği şeritte araç kullanmamak"):
    print("46/2-a Ceza maddesi gereğince hızının gerektirdiği şeritte araç kullanılmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Hiziningerektirdigiserittearackullanmamak,indirim(Hiziningerektirdigiserittearackullanmamak)))

elif (ceza=="Şerit değiştirmeden önce gireceği şeridi kontrol etmemek"):
    print("46/2-b Ceza maddesi gereğince şerit değiştirmeden önce gireceği şeridi kontrol etmediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Seritdegistirmedenoncegirecegiseritikontroletmemek,indirim(Seritdegistirmedenoncegirecegiseritikontroletmemek)))

elif (ceza=="Tehlikeli şekilde şerit değiştirmek"):
    print("46/2-c Ceza maddesi gereğince tehlikeli şekilde şerit değiştirildiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Tehlikelisekildeseritdegistirmek,indirim(Tehlikelisekildeseritdegistirmek)))

elif (ceza=="Sürekli sol şeridi kullanmak"):
    print("46/2-d Ceza maddesi gereğince sürekli sol şeridi kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Sureklisolseridikullanmak,indirim(Sureklisolseridikullanmak)))

elif (ceza=="Emniyet şeridini kullanmak"):
    print("46/2-f Ceza maddesi gereğince emniyet şeridinin kullanılasından dolayı {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Emniyetseridinikullanmak,indirim(Emniyetseridinikullanmak)))

elif (ceza=="Ardı ardına tehlikeli şerit değiştirmek (makas atmak)"):
    print("46/2-g Ceza maddesi gereğince ardı ardına tehlikeli şerit değiştirildiği (Makas atmak) için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Makasatmak,indirim(Makasatmak)))

elif (ceza=="Ters yönde araç kullanmak"):
    print("46/2-h Ceza maddesi gereğince ters yönde araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Tersyondearackullanmak,indirim(Tersyondearackullanmak)))

elif (ceza=="Hayvan sürülerinin taşıt yoluna çıkmasını engellememek"):
    print("46/3 Ceza maddesi gereğince hayvan sürülerinin taşıt yoluna çıkmasının engellendiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Hayvansurulerinintasityolunacikmasiniengellememek,indirim(Hayvansurulerinintasityolunacikmasiniengellememek)))

elif (ceza=="Polisin dur ihtarına uymamak"):
    print("47/1-a Ceza maddesi gereğince polisin dur ihtarına uyulmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Polisindurihtarinauymamak,indirim(Polisindurihtarinauymamak)))

elif (ceza=="Kırımızı ışıkta geçmek"):
    print("47/1-b Ceza maddesi gereğince kırımızı ışıkta geçildiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kirmiziisiktagecmek,indirim(Kirmiziisiktagecmek)))

elif (ceza=="Trafik levhalarına uymamak"):
    print("47/1-c Ceza maddesi gereğince trafik levhalarına uyulmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Trafiklevhalarinauymamak,indirim(Trafiklevhalarinauymamak)))

elif (ceza=="Trafik güvenliğini tehlikeye düşürmek"):
    print("47/1-d Ceza maddesi gereğince trafik güvenliğini tehlikeye soktuğu gerekçesiyle {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Trafikguvenliginitehlikeyedusurmek,indirim(Trafikguvenliginitehlikeyedusurmek)))

elif (ceza=="Alkollü araç kullanmak"):
    print("48/5 Ceza maddesi gereğince alkollü araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Alkolluarackullanmak,indirim(Alkolluarackullanmak)))

elif (ceza=="Uyuşturucu madde kullanıp araç kullanmak"):
    print("48/8 Ceza maddesi gereğince uyuşturucu madde kullanıp araç kullanıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Uyusturucumaddekullaniparackullanmak,indirim(Uyusturucumaddekullaniparackullanmak)))

elif (ceza=="Alkolmetreye üflememek"):
    print("48/9 Ceza maddesi gereğince alkolmetreye üflemeyi reddettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Alkolmetreyeuflememek,indirim(Alkolmetreyeuflememek)))

elif (ceza=="Ticari araç kullanma sürelerine uymamak"):
    print("49/3 Ceza maddesi gereğince ticari araç kullanma sürelerine uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ticariarackullanmasurelerineuymamak,indirim(Ticariarackullanmasurelerineuymamak)))

elif (ceza=="Hız cezası"):
    hizcezasi()

elif (ceza=="Kavşaklara yaklaşırken hızını azaltmamak"):
    print("52/1-a Ceza maddesi gereğince Kavşaklara yaklaşırken hızını azaltmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kavsaklarayaklasirkenhızınıyavaslatmamak,indirim(Kavsaklarayaklasirkenhızınıyavaslatmamak)))

elif (ceza=="Yol ve trafik durumuna göre davranmamak"):
    print("52/1-b Ceza maddesi gereğince yol ve trafik durumuna göre davranmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yolvetrafikdurumunagoredavranmamak,indirim(Yolvetrafikdurumunagoredavranmamak)))

elif (ceza=="Öndeki araçla güvenli mesafe bırakmamak"):
    print("52/1-c Ceza maddesi gereğince öndeki araçla güvenli mesafe bırakmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ondekiaraclaguvenlimesafebirakmak,indirim(Ondekiaraclaguvenlimesafebirakmak)))

elif (ceza=="Konvoy halinde araçlar arasında gerekli mesafe bırakmamak"):
    print("52/1-d Ceza maddesi gereğince konvoy halinde araçlar arasında gerekli mesafe bırakmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Konvoyhalindearaclararasindagereklimesafebirakmak,indirim(Konvoyhalindearaclararasindagereklimesafebirakmak)))

elif (ceza=="Sağa dönüş kurallarına uymamak"):
    print("53/1-a Ceza maddesi gereğince sağa dönüş kurallarına uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Sagadonuskurallarinauymamak,indirim(Sagadonuskurallarinauymamak)))

elif (ceza=="Sola dönüş kurallarına uymamak"):
    print("53/1-b Ceza maddesi gereğince sola dönüş kurallarına uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Soladonuskurallarinauymamak,indirim(Soladonuskurallarinauymamak)))

elif (ceza=="Dönel kavşak kurallarına uymamak"):
    print("53/1-c Ceza maddesi gereğince dönel kavşak kurallarına uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Donelkavsaklarauymamak,indirim(Donelkavsaklarauymamak)))

elif (ceza=="Dönel kavşakta geriye dönüş kurallarına uymamak"):
    print("53/1-d Ceza maddesi gereğince dönel kavşakta geriye dönüş kurallarına uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Donelkavsaktageridonuskurallarinauymamak,indirim(Donelkavsaktageridonuskurallarinauymamak)))

elif (ceza=="Sağa veya sola dönüşte yayalara yol vermemek"):
    print("53/2 Ceza maddesi gereğince sağa veya sola dönüşte yayalara yol vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Sagaveyasoladonusteyayalarayolvermemek,indirim(Sagaveyasoladonusteyayalarayolvermemek)))

elif (ceza=="Hatalı sollama yapmak"):
    print("54/1-a Ceza maddesi gereğince hatalı sollama yaptığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Hatalisollamayapmak,indirim(Hatalisollamayapmak   )))

elif (ceza=="Sollama yapmanın yasak olduğu yerde sollama yapmak"):
    print("54/1-b Ceza maddesi gereğince sollama yapmanın yasak olduğu yerde sollama yaptığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Sollamayapmaninyasakolduğuyerdesollamayapmak,indirim(Sollamayapmaninyasakolduğuyerdesollamayapmak)))

elif (ceza=="Geçilme kurallarına uymamak"):
    print("55. Ceza maddesi gereğince geçilme kurallarına uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gecilmekurallarinauymak,indirim(Gecilmekurallarinauymak)))

elif (ceza=="Şerit izleme ve değiştirme kurallarına uymamak"):
    print("56/1-a Ceza maddesi gereğince şerit izleme ve değiştirme kurallarına uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Seritizlemevedegistirmekurallarinauymamak,indirim(Seritizlemevedegistirmekurallarinauymamak)))

elif (ceza=="Karşıdan gelen aracın geçişini zorlaştırmak"):
    print("56/1-b Ceza maddesi gereğince karşıdan gelen aracın geçişini zorlaştırdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Karsidangelenaracingecisinizorlastirmak,indirim(Karsidangelenaracingecisinizorlastirmak)))

elif (ceza=="Yakın takip"):
    print("56/1-c Ceza maddesi gereğince yakın takipte bulunduğu için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yakintakip,indirim(Yakintakip)))

elif (ceza=="Hız sınırının çok altında araç kullanmak"):
    print("56/1-d Ceza maddesi gereğince hız sınırının çok altında araç kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Hizsinirinincokaltindaarackullanmak,indirim(Hizsinirinincokaltindaarackullanmak)))

elif (ceza=="Dar yollarda araç sınıfına göre geçiş kolaylığı sağlamamak"):
    print("56/1-e Ceza maddesi gereğince dar yollarda araç sınıfına göre geçiş kolaylığı sağlamadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Daryollardaaracsinifinagoregeciskolayligisaglamamak,indirim(Daryollardaaracsinifinagoregeciskolayligisaglamamak)))

elif (ceza=="Kavşaklarda ilk geçiş hakkını vermemek"):
    print("57/1-a Ceza maddesi gereğince kavşaklarda ilk geçiş hakkını vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kavsaklardailkgecishakkinivermemek,indirim(Kavsaklardailkgecishakkinivermemek)))

elif (ceza=="Kontrollü kavşaklarda ilk geçiş hakkını vermemek"):
    print("57/1-b Ceza maddesi gereğince kontrollü kavşaklarda ilk geçiş hakkını vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kontrollukavsaklardailkgecishakkinivermemek,indirim(Kontrollukavsaklardailkgecishakkinivermemek)))

elif (ceza=="Kontrolsüz kavşaklarda ilk geçiş hakkını vermemek"):
    print("57/1-c Ceza maddesi gereğince kontrolsüz kavşaklarda ilk geçiş hakkını vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kontrolsuzkavsaklardailkgecishakkinivermemek,indirim(Kontrolsuzkavsaklardailkgecishakkinivermemek)))

elif (ceza=="Yeşil ışık yansa bile duran trafikte kavşağa girmek"):
    print("57/1-d Ceza maddesi gereğince yeşil ışık yansa bile duran trafikte kavşağa girdiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yesilisikyansabileduraktrafiktekavsagagirmek,indirim(Yesilisikyansabileduraktrafiktekavsagagirmek)))

elif (ceza=="Kavşaklarda duraklamak"):
    print("57/1-e Ceza maddesi gereğince kavşaklarda durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kavsaklardaduraklamak,indirim(Kavsaklardaduraklamak)))

elif (ceza=="Aksine işaret olması bile ray üzerindeki araca ilk geçiş hakkını vermemek"):
    print("57/1-f Ceza maddesi gereğince Aksine işaret olması bile ray üzerindeki araca ilk geçiş hakkını vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Aksineisaretolmasabilerayuzerindekiaracailkgecishakkinivermemek,indirim(Aksineisaretolmasabilerayuzerindekiaracailkgecishakkinivermemek)))

elif (ceza=="Yolcu indirme ve bindirme kurallarına uymamak"):
    print("58. Ceza maddesi gereğince yolcu indirme ve bindirme kurallarına uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yolcuindirmebindirmekurallarinauymamak,indirim(Yolcuindirmebindirmekurallarinauymamak)))

elif (ceza=="Yerleşim yeri dışında park etme"):
    print("59. Ceza maddesi gereğince yerleşim yeri dışında park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yerlesimyeridisindaparketmek,indirim(Yerlesimyeridisindaparketmek)))

elif (ceza=="Taşıt yolu üzerinde duraklamak"):
    print("60/1-a Ceza maddesi gereğince taşıt yolu üzerinde durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Tasıtyoluuzerindeduraklamak,indirim(Tasıtyoluuzerindeduraklamak)))

elif (ceza=="Sol şeritte duraklamak"):
    print("60/1-b Ceza maddesi gereğince sol şeritte durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Solseritteduraklamak,indirim(Solseritteduraklamak)))

elif (ceza=="Yaya geçidinde duraklamak"):
    print("60/1-c Ceza maddesi gereğince yaya geçidinde durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yayagecidindeduraklamak,indirim(Yayagecidindeduraklamak)))

elif (ceza=="Kavşaklara 5 metre kala duraklamak"):
    print("60/1-d Ceza maddesi gereğince kavşaklara 5 metre kala durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kavsaklarabesmetrekaladuraklamak,indirim(Kavsaklarabesmetrekaladuraklamak)))

elif (ceza=="Dönemeçlerde duraklamak"):
    print("60/1-e Ceza maddesi gereğince dönemeçlerde durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Donemeclerdeduraklamak,indirim(Donemeclerdeduraklamak)))

elif (ceza=="Otobüs duraklarında duraklamak"):
    print("60/1-f Ceza maddesi gereğince otobüs duraklarında durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Otobusduraklarindaduraklamak,indirim(Otobusduraklarindaduraklamak)))

elif (ceza=="İkinci sırada duraklamak"):
    print("60/1-g Ceza maddesi gereğince ikinci sırada durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ikincisiradaduraklamak,indirim(Ikincisiradaduraklamak)))

elif (ceza=="Trafik işaretlerinin altında duraklamak"):
    print("60/1-h Ceza maddesi gereğince trafik işaretlerinin altında durakladığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Trafikisaretlerininaltindaduraklamak,indirim(Trafikisaretlerininaltindaduraklamak)))

elif (ceza=="Taşıt yolu üzerinde park etmek"):
    print("61/1-a Ceza maddesi gereğince taşıt yolu üzerinde park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Tasityoluuzerindeparketmek,indirim(Tasityoluuzerindeparketmek)))

elif (ceza=="Sol şeritte park etmek"):
    print("61/1-b Ceza maddesi gereğince sol şeritte park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Solseritteparketmek,indirim(Solseritteparketmek)))

elif (ceza=="Yaya geçidinde park etmek"):
    print("61/1-c Ceza maddesi gereğince yaya geçidine park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yayagecidindeparketmek,indirim(Yayagecidindeparketmek)))

elif (ceza=="Kavşaklara 5 metre kala park etmek"):
    print("61/1-d Ceza maddesi gereğince kavşaklara 5 metre kala park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kavsaklarabesmetrekalaparketmek,indirim(Kavsaklarabesmetrekalaparketmek)))

elif (ceza=="Dönemeçlerde park etmek"):
    print("61/1-e Ceza maddesi gereğince dönemeçlerde park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Donemeclerdeparketmek,indirim(Donemeclerdeparketmek)))

elif (ceza=="Otobüs duraklarında park etmek"):
    print("61/1-f Ceza maddesi gereğince otobüs duraklarında park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Otobusduraklarindaparketmek,indirim(Otobusduraklarindaparketmek)))

elif (ceza=="İkinci sırada park etmek"):
    print("61/1-g Ceza maddesi gereğince ikinci sırada park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ikincisiradaparketmek,indirim(Ikincisiradaparketmek)))

elif (ceza=="Trafik işaretlerinin altında park etmek"):
    print("61/1-h Ceza maddesi gereğince trafik işaretlerinin altında park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Trafikisaretlerininaltinaparketmek,indirim(Trafikisaretlerininaltinaparketmek)))

elif (ceza=="İzin verilen zaman dışında park etmek"):
    print("61/1-ı Ceza maddesi gereğince izin verilen zaman dışında park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Izinverilenzamandisindaparketmek,indirim(Izinverilenzamandisindaparketmek)))

elif (ceza=="Kamunun faydalandığı alanların giriş çıkışına park etmek"):
    print("61/1-j Ceza maddesi gereğince kamunun faydalandığı alanların giriş çıkışına park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kamununfaydalandigialanlaringiriscikislarinaparketmek,indirim(Kamununfaydalandigialanlaringiriscikislarinaparketmek)))

elif (ceza=="Alt veya üst geçitlerde park etmek"):
    print("61/1-k Ceza maddesi gereğince alt veya üst geçitlerde park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Altveyaustgecitlerdeparketmek,indirim(Altveyaustgecitlerdeparketmek)))

elif (ceza=="İzin verilen süreden fazla park etmek"):
    print("61/1-l Ceza maddesi gereğince izin verilen süreden fazla park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Izinverilensuredenfazlaparketmek,indirim(Izinverilensuredenfazlaparketmek)))

elif (ceza=="Resmi araçlara ayrılmış alanlara park etmek"):
    print("61/1-m Ceza maddesi gereğince resmi araçlara ayrılmış alanlara park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Resmiaraclaraayrilmisalanlaraparketmet,indirim(Resmiaraclaraayrilmisalanlaraparketmet)))

elif (ceza=="Yaya yollarına park etmek"):
    print("61/1-n Ceza maddesi gereğince yaya yollarına park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yayayollarinaparketmek,indirim(Yayayollarinaparketmek)))

elif (ceza=="Engelli araç park yerine park etmek"):
    print("61/1-o Ceza maddesi gereğince engelli araç park yerine park ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Engelliaracparkyerineparketmek,indirim(Engelliaracparkyerineparketmek)))

elif (ceza=="Araçlarda olması gereken ışık donanımlarını bulundurmamak"):
    print("63. Ceza maddesi gereğince araçlarda olması gereken ışık donanımlarını bulundurmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Araclardabulundurulmasigerekenisikdonanimlarinibulundurmamak,indirim(Araclardabulundurulmasigerekenisikdonanimlarinibulundurmamak)))

elif (ceza=="Gerekli alanlarda uzun farlarını kullanmamak"):
    print("64/1-a-1 Ceza maddesine göre gerekli alanlarda uzun farlarını kullanmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gereklialanlardauzunfarlarikullanmamak,indirim(Gereklialanlardauzunfarlarikullanmamak)))

elif (ceza=="Akşam farları yakmamak"):
    print("64/1-a-2 Ceza maddesi gereğince akşam farları yakmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Aksamfarlariyakmamak,indirim(Aksamfarlariyakmamak)))

elif (ceza=="Arka kenar ışıklarını farlarla birlikte kullanılması"):
    print("64/1-a-3 Ceza maddesi gereğince arka kenar ışıklarını farlarla birlikte kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Arkakenarisiklarininfarlarlabirliktekullanilmasi,indirim(Arkakenarisiklarininfarlarlabirliktekullanilmasi)))

elif (ceza=="Sis farlarını gereksiz yere kullanmak"):
    print("64/1-b-1 Ceza maddesi gereğince sis farlarını gereksiz yere kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Sisfarlarinigereksizyerekullanmak,indirim(Sisfarlarinigereksizyerekullanmak)))

elif (ceza=="Dönüş ışıklarını farklı anlamlarda kullanmak"):
    print("64/1-b-2 Ceza maddesi gereğince dönüş ışıklarını farklı anlamlarda kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Donusisiklarinifarklianlamdakullanmak,indirim(Donusisiklarinifarklianlamdakullanmak)))

elif (ceza=="Gece karşılaşmalarında ışıkları söndürmemek"):
    print("64/1-b-3 Ceza maddesi gereğince gece karşılaşmalarında ışıkları söndürmediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gecekarsilasmalarindaisiklarisondurmemek,indirim(Gecekarsilasmalarindaisiklarisondurmemek)))

elif (ceza=="Öndeki aracı geçerken kısa süre dışında uzun farları kullanmak"):
    print("64/1-b-4 Ceza maddesi gereğince öndeki aracı geçerken kısa süre dışında uzun farları kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ondekiaracigecerkenkisasuredenfazlauzunisiklarikullanmak,indirim(Ondekiaracigecerkenkisasuredenfazlauzunisiklarikullanmak)))

elif (ceza=="Yönetmeliğe aykırı ışıklandırma yapmak"):
    print("64/1-b-5 Ceza maddesi gereğince yönetmeliğe aykırı ışıklandırma kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yonetmeligeaykiriisiklandırmayapmak,indirim(Yonetmeligeaykiriisiklandırmayapmak)))

elif (ceza=="Sadece park lambalarıyla seyretmek"):
    print("64/1-b-6 Ceza maddesi gereğince sadece park lambalarıyla seyrettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Sadeceparklambalariylaseyretmek,indirim(Sadeceparklambalariylaseyretmek)))

elif (ceza=="Taşıma sınırı üstünde yolcu almak"):
    print("65/1-a Ceza maddesi gereğince taşıma sınırı üstünde yolcu aldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Tasimasiniriustundeyolcualmak,indirim(Tasimasiniriustundeyolcualmak)))

elif (ceza=="Dingil ağırlığından fazla yük taşımak"):
    print("65/1-c Ceza maddesi gereğince dingil ağırlığından fazla yük taşıdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Dingilagirligindanfazlayukyuklemek,indirim(Dingilagirligindanfazlayukyuklemek)))

elif (ceza=="Tehlike oluşturabilecek şekilde yük yüklemek"):
    print("65/1-d Ceza maddesi gereğince tehlike oluşturabilecek şekilde yük yüklediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Tehlikeolusturabileceksekildeyukyuklemek,indirim(Tehlikeolusturabileceksekildeyukyuklemek)))

elif (ceza=="Gerekli izin almadan tehlikeli madde taşımak"):
    print("65/1-e Ceza maddesi gereğince gerekli izin almadan tehlikeli madde taşıdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gerekliiznialmadantehlikelimaddetasimak,indirim(Gerekliiznialmadantehlikelimaddetasimak)))

elif (ceza=="Özel izne tabi olan yükleri izin almadan taşımak"):
    print("65/1-f Ceza maddesi gereğince özel izne tabi olan yükleri izin almadan taşıdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Ozeliznetabiolanyukleriizinalmadantasimak,indirim(Ozeliznetabiolanyukleriizinalmadantasimak)))

elif (ceza=="Gabari dışı yük taşımak"):
    print("65/1-g Ceza maddesi gereğince gabari dışı yük taşıdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gabaridisiyuktasimak,indirim(Gabaridisiyuktasimak)))

elif (ceza=="Yükü karayoluna düşecek veya değecek şekilde yüklemek"):
    print("65/1-h Ceza maddesi gereğince yükü karayoluna düşecek veya değecek şekilde yük yüklendiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yukukarayolunadusecekveyadegeceksekildeyukyuklemek,indirim(Yukukarayolunadusecekveyadegeceksekildeyukyuklemek)))

elif (ceza=="Eğimli yollarda dengeyi bozacak şekilde yük yüklemek"):
    print("65/1-i Ceza maddesi gereğince eğimli yollarda dengeyi bozacak şekilde yük yüklendiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Egimliyollardadengeyibozacaksekildeyukyuklemek,indirim(Egimliyollardadengeyibozacaksekildeyukyuklemek)))

elif (ceza=="Sürücünün görüşüne engel olaşak şelikde yük yüklemek"):
    print("65/1-j Ceza maddesi gereğince sürücünün görüşüne engel olacak şelikde yük yüklediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Surucunungorusuneengelolacaksekildeyukyuklemek,indirim(Surucunungorusuneengelolacaksekildeyukyuklemek)))

elif (ceza=="Çeken ve çekilen araçlarda tedbir almamak"):
    print("65/1-k Ceza maddesi gereğince çeken ve çekilen araçlarda tedbir alınmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Cekenvecekilenaraclardatedbiralmamak,indirim(Cekenvecekilenaraclardatedbiralmamak)))

elif (ceza=="Yol denetim istasyonuna girmemek"):
    print("65/4 Ceza maddesi gereğince Yol denetim istasyonuna girmediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yoldenetimistasyonunagirmemek,indirim(Yoldenetimistasyonunagirmemek)))

elif (ceza=="Kış lastiği kullanmamak"):
    print("65/a Ceza maddesi gereğince kış lastiği kullanmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kislastigikullanmamak,indirim(Kislastigikullanmamak)))

elif (ceza=="Tehlikeli manevra yapmak"):
    print("67/1-a Ceza maddesi gereğince tehlikeli manevra yaptığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Tehlikelimanevrayapmak,indirim(Tehlikelimanevrayapmak)))

elif (ceza=="Yönetmelikteki belirtilen şartlar dışında geriye dönmek"):
    print("67/1-b Ceza maddesi gereğince yönetmelikteki belirtilen şartlar dışında geriye döndüğü için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yonetmeliktekibelirtilensartlardisindageriyedonmek,indirim(Yonetmeliktekibelirtilensartlardisindageriyedonmek)))

elif (ceza=="Dönüşlerde niyetini belli edecek şekilde işaret vermemek"):
    print("67/1-c Ceza maddesi gereğince dönüşlerde niyetini belli edecek şekilde işaret vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Donuslerdeniyetinibelliedeceksekildeisaretvermemek,indirim(Donuslerdeniyetinibelliedeceksekildeisaretvermemek)))

elif (ceza=="Drift yapmak"):
    print("67/1-d Ceza maddesi gereğince drift yaptığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Driftyapmak,indirim(Driftyapmak)))

elif (ceza=="Yayalara rahatsızlık verecek şekilde sağ şeridi işgal etmek"):
    print("68/1-a-1 Ceza maddesi gereğince yayalara rahatsızlık verecek şekilde sağ şeridi işgal ettiği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yayalararahatsizlikvereceksekildesagseritiisgaletmek,indirim(Yayalararahatsizlikvereceksekildesagseritiisgaletmek)))

elif (ceza=="Yarış düzenlemek"):
    print("70. Ceza maddesi gereğince yarış düzenlediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yarisduzenlemek,indirim(Yarisduzenlemek)))

elif (ceza=="Geçiş üstünlüğü kurallarına uymamak"):
    print("71. Ceza maddesi gereğince geçiş üstünlüğü kurallarına uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Gecisustunlugukurallarinauymamak,indirim(Gecisustunlugukurallarinauymamak)))

elif (ceza=="Çevreyi rahatsız edici araç kullanmak"):
    print("72. Ceza maddesi gereğince çevreyi rahatsız edici araç kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Cevreyirahatsizediciarackullanmak,indirim(Cevreyirahatsizediciarackullanmak)))

elif (ceza=="Saygısızca araç kullanmak"):
    print("73/a Ceza maddesi gereğince saygısızca araç kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Saygisizcaarackullanmak,indirim(Saygisizcaarackullanmak)))

elif (ceza=="Araçtan birşeyler atmak veya dökmek"):
    print("73/b Ceza maddesi gereğince araçtan bir şeyler attığı veya döktüğü için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Aractanbirseyleratmakveyadokmek,indirim(Aractanbirseyleratmakveyadokmek)))

elif (ceza=="Araç kullanırken cep telefonu ile konuşmak"):
    print("73/c Ceza maddesi gereğince araç kullanırken cep telefonu ile konuştuğu için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Arackullanirkenceptelefonuilekonusmak,indirim(Arackullanirkenceptelefonuilekonusmak)))

elif (ceza=="Kavşak giriş çıkışlarında yayalara ilk geçiş hakkını vermemek"):
    print("74/a Ceza maddesi gereğince kavşak giriş çıkışlarında yayalara ilk geçiş hakkını vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kavsakgiriscikislarindayayalarailkgecishakkinivermemek,indirim(Kavsakgiriscikislarindayayalarailkgecishakkinivermemek)))

elif (ceza=="Yaya geçitlerinde yayayalara ilk geçiş hakkını vermemek"):
    print("74/b Ceza maddesi gereğince yaya geçitlerinde yayayalara ilk geçiş hakkını vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Yayagecitlerindeyayalarailkgecishakkinivermemek,indirim(Yayagecitlerindeyayalarailkgecishakkinivermemek)))

elif (ceza=="Okul taşıdında dur işaretine uymamak"):
    print("75. Ceza maddesi gereğince okul taşıdında dur işaretine uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Okultasitindadurisaretineuymamak,indirim(Okultasitindadurisaretineuymamak)))

elif (ceza=="Demir yolu geçidinde kurallara uymamak"):
    print("76. Ceza maddesi gereğince demir yolu geçidinde kurallara uymadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Demiryolugecidindekurallarauymamak,indirim(Demiryolugecidindekurallarauymamak)))

elif (ceza=="Emniyet kemeri takmamak"):
    print("78/1-a Ceza maddesi gereğince emniyet kemeri takmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Emniyetkemeritakmamak,indirim(Emniyetkemeritakmamak)))

elif (ceza=="Kask takmamak"):
    print("78/1-b Ceza maddesi gereğince kask takmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Kasktakmamak,indirim(Kasktakmamak)))

elif(ceza=="Trafik kazasında tedbir almamak"):
    print("81/1-a Ceza maddesi gereğince trafik kazasında tedbir almadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Trafikkazasindatedbiralmamak,indirim(Trafikkazasindatedbiralmamak)))

elif (ceza=="Trafik kazasında evraklarını vermemek"):
    print("81/1-c Ceza maddesi gereğince trafik kazasında evraklarını vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Trafikkazasindaevraklarinivermemek,indirim(Trafikkazasindaevraklarinivermemek)))

elif (ceza=="Trafik kazasında karşı tarafa bilgi vermemek"):
    print("81/1-e Ceza maddesi gereğince trafik kazasında karşı tarafa bilgi vermediği için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Trafikkazasindakarsitarafabilgivermemek,indirim(Trafikkazasindakarsitarafabilgivermemek)))

elif (ceza=="Trafik polisi izin vermeden kaza yerinden ayrılmak"):
    print("81/3 Ceza maddesi gereğince trafik polisi izin vermeden kaza yerinden ayrıldığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Trafikpolisiizinvermedenkazayerindenayrilmak,indirim(Trafikpolisiizinvermedenkazayerindenayrilmak)))

elif (ceza=="Araç sigortasını yaptırmamak"):
    print("76. Ceza maddesi gereğince araç sigortasını yaptırmadığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Aracsigortasınıyaptirmamak,indirim(Aracsigortasınıyaptirmamak)))

elif (ceza=="Amaç dışında araç kullanmak"):
    print("Ek-2/1 Ceza maddesi gereğince amaç dışında araç kullandığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Amacdisindaarackullanmak,indirim(Amacdisindaarackullanmak)))

elif (ceza=="Belediyeden izin almadan yolcu taşımak"):
    print("Ek-2/3-a Ceza maddesi gereğince belediyeden izin almadan yolcu taşıdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Belediyedenizinalmadanyolcutasimak,indirim(Belediyedenizinalmadanyolcutasimak)))

elif (ceza=="Belediyeden izin alınan şartlar dışında yolcu taşımak"):
    print("Ek-2/3-b Ceza maddesi gereğince belediyeden izin alınan şartlar dışında yolcu taşıdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Belediyedenizinalinasartlardisindayolcutasimak,indirim(Belediyedenizinalinasartlardisindayolcutasimak)))

elif (ceza=="Belediyeden izin alınan bölge dışında yolcu taşımak"):
    print("Ek-2/3-c Ceza maddesi gereğince belediyeden izin alınan bölge dışında yolcu taşıdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Belediyedenizinalınanbölgedisindayolcutasima,indirim(Belediyedenizinalınanbölgedisindayolcutasima)))

elif (ceza=="Belediyeden alınan izin bitmesine rağmen yolcu taşımak"):
    print("Ek-2/5 Ceza maddesi gereğince belediyeden izin alınan izin bitmesine rağmen yolcu taşıdığı için {} Plakalı araç sahibine {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(plaka,Belediyedenalinanizinbitmesineragmenyolcutasima,indirim(Belediyedenalinanizinbitmesineragmenyolcutasima)))

