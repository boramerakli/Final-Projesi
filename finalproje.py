def indirim(a):
    return a-(a*0.25) 

def hizcezasi():
    hizsiniri=int(input("Hız sınırını giriniz: "))
    hiz=int(input("Hızı giriniz: "))
    if (hizsiniri+(hizsiniri*0.10))>hiz :
        return print("Ceza uygulanmasını gerektirecek bir durum yoktur.")
    elif (hizsiniri+(hizsiniri*0.10))<hiz<=(hizsiniri+(hizsiniri*0.30)): 
        return print("51/2-a Ceza maddesi gereğince Hız sınırını %10 ile %30 arasında geçtiği için 427₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse 320.25₺'ye indirim uygulanacaktır.")
    elif (hizsiniri+(hizsiniri*0.30))<hiz<=(hizsiniri+(hizsiniri*0.50)):
        return print("51/2-b Ceza maddesi gereğince Hız sınırını %30 ile %50 arasında geçtiği için 888₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse 666₺'ye indirim uygulanacaktır.")
    elif (hizsiniri+(hizsiniri*0.50))<hiz:
        return print("51/2-c Ceza maddesi gereğince Hız sınırını %50’den fazla geçtiği için 1823₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse 1367.25₺'ye indirim uygulanacaktır.")

ceza = input("İşlenen cezayı giriniz: ")

Hurdayaçıkarılanaracınişlemleriniyapmamak=427
Sattığıaracıilgilikurumlarabildirmemek=3340
İhaledenalınanaraçlardagereklibilgilerivermemek=427
Tescilplakasızaraçkullanmak=1823
Hurdabelgeliaraçkullanmak=3674
Araçtaruhsatbulundurmamak=166
Plakayıyanlışyeretakmak=166 
Appplakakullanmak=750
İzinverilensüredeuygunplakatakmamak=1536
Araçcinsinegörebelirlenensayıdaplakatakmamak=750
Plakaüzerindedeğişiklikyapmak=750
Plakasızaraçkullanmak=3093
Başkaaracınplakasınıkullanmak=9107
Sahteplakatakmak=9107
Geçicitescilişlemleriyapmamak=427
Araçdabulundurulmasıgerekendonanımlarıbulundurmamak=196
Mevzuataaykırıışıkkullanmak=1823
Araçüzerinderenkdeğişikliğiveyareklamyapıştırmak=196
Gerekliışıkdonanımıçalışmayanaraçkullanmak=196
Abartıegzozveyacamfilmikullanmak=427
Araçcinsindebulundurulmasızorunlugereçleribulundurmamak=196
Ticariaraçlarıntakoğrafkullanmaması=888
lpgruhsataişletmemek=196
Araçlarüzerindekideğişikliklerinuygunolmaması=1823
Muayenesizaraçkullanmak=427
Muayenesiolmadığıiçintrafiktenmenedilenaraçkullanmak=888
Muayenedeağırkusurluolanaracıkullanmak=888
Ehliyetsizaraçkullanmak=3674
Ehliyetineelkonulmuşkişilerinaraçkullanması=3674
Ehliyetiiptaledilmişkişilerinaraçkullanması=3674
Ehliyetsınıfıdışındaaraçkullanmak=1823
Geçerliliksüresibitenehliyetlearaçkullanmak=739
Dışülkeehliyetiylebelirlenenşartlardışındaaraçkullanmak=739	
Sürücüsertifakasınıehliyetedönüştürmedenaraçkullanmak=1823
İkametadresinitescilbiriminebildirmemek=427
Ehliyetiyanındaolmadanaraçkullanmak=427
Hızınıngerektirdiğişerittearaçkullanmamak=427
Şeritdeğiştirmedenöncegireceğişeridikontroletmemek=427
Tehlikelişekildeşeritdeğiştirmek=427
Süreklisolşeridikullanmak=427
Emniyetşeridinikullanmak=1823
makasatmak=1823
Tersyöndearaçkullanmak=1823
Hayvansürülerinintaşıtyolunaçıkmasınıengellememek=427
Polisindurihtarınauymamak=427
Kırımızıışıktageçmek=427
Trafiklevhalarınauymamak=196
Trafikgüvenliğinitehlikeyedüşürmek=196
Alkollüaraçkullanmak=1823
Uyuşturucumaddekullanıparaçkullanmak=9411
Alkolmetreyeüflememek=5224
Ticariaraçkullanmasürelerineuymamak=196
Kavşaklarayaklaşırkenhızınıazaltmamak=196
Yolvetrafikdurumunagöredavranmamak=196
Öndekiaraçlagüvenlimesafebırakmamak=196
Konvoyhalindearaçlararasındagereklimesafebırakmamak=196
Sağadönüşkurallarınauymamak=196
Soladönüşkurallarınauymamak=196
Dönelkavşakkurallarınauymamak=196
Dönelkavşaktageriyedönüşkurallarınauymamak=196
Sağaveyasoladönüşteyayalarayolvermemek=196
Hatalısollamayapmak=427
Sollamayapmanınyasakolduğuyerdesollamayapmak=427
Geçilmekurallarınauymamak=196
Şeritizlemevedeğiştirmekurallarınauymamak=196
Karşıdangelenaracıngeçişinizorlaştırmak=196
Yakıntakip=196
Hızsınırınınçokaltındaaraçkullanmak=196
Daryollardaaraçsınıfınagöregeçişkolaylığısağlamamak=196
Kavşaklardailkgeçişhakkınıvermemek=196
Kontrollükavşaklardailkgeçişhakkınıvermemek=196
Kontrolsüzkavşaklardailkgeçişhakkınıvermemek=196
Yeşilışıkyansabiledurantrafiktekavşağagirmek=196
Kavşaklardaduraklamak=196
Aksineişaretolmasıbilerayüzerindekiaracailkgeçişhakkınıvermemek=196
Yolcuindirmevebindirmekurallarınauymamak=196
Yerleşimyeridışındaparketme=196
Taşıtyoluüzerindeduraklamak=196
Solşeritteduraklamak=196
Yayageçidindeduraklamak=196
Kavşaklara5metrekaladuraklamak=196
Dönemeçlerdeduraklamak=196
Otobüsduraklarındaduraklamak=196
İkincisıradaduraklamak=196
Trafikişaretlerininaltındaduraklamak=196
Taşıtyoluüzerindeparketmek=196
Solşeritteparketmek=196
Yayageçidindeparketmek=196
Kavşaklara5metrekalaparketmek=196
Dönemeçlerdeparketmek=196
Otobüsduraklarındaparketmek=196
İkincisıradaparketmek=196
Trafikişaretlerininaltındaparketmek=196
İzinverilenzamandışındaparketmek=196
Kamununfaydalandığıalanlarıngirişçıkışınaparketmek=196
Altveyaüstgeçitlerdeparketmek=196
İzinverilensüredenfazlaparketmek=196
Resmiaraçlaraayrılmışalanlaraparketmek=196
Yayayollarınaparketmek=196
Engelliaraçparkyerineparketmek=392
Araçlardaolmasıgerekenışıkdonanımlarınıbulundurmamak=888
Gereklialanlardauzunfarlarınıkullanmamak=196
Akşamfarlarıyakmamak=427
Arkakenarışıklarınıfarlarlabirliktekullanılması=196
Sisfarlarınıgereksizyerekullanmak=196
Dönüşışıklarınıfarklıanlamlardakullanmak=196
Gecekarşılaşmalarındaışıklarısöndürmemek=196
Öndekiaracıgeçerkenkısasüredışındauzunfarlarıkullanmak=196
Yönetmeliğeaykırıışıklandırmayapmak=196
Sadeceparklambalarıylaseyretmek=196
Taşımasınırıüstündeyolcualmak=153
Dingilağırlığındanfazlayüktaşımak=1665
Tehlikeoluşturabilecekşekildeyükyüklemek=408
Gerekliizinalmadantehlikelimaddetaşımak=828
Özeliznetabiolanyükleriizinalmadantaşımak=828
Gabaridışıyüktaşımak=1665
Yükükarayolunadüşecekveyadeğecekşekildeyüklemek=408
Eğimliyollardadengeyibozacakşekildeyükyüklemek=408
Sürücününgörüşüneengelolaşakşelikdeyükyüklemek=408
Çekenveçekilenaraçlardatedbiralmamak=408
Yoldenetimistasyonunagirmemek=3340
Kışlastiğikullanmamak=1138
Tehlikelimanevrayapmak=427
Yönetmeliktekibelirtilenşartlardışındageriyedönmek=427
Dönüşlerdeniyetinibelliedecekşekildeişaretvermemek=427
Driftyapmak=9125
Yayalararahatsızlıkverecekşekildesağşeridiişgaletmek=196
Yarışdüzenlemek=888
Geçişüstünlüğükurallarınauymamak=196
Çevreyirahatsızediciaraçkullanmak=196
Saygısızcaaraçkullanmak=196
Araçtanbirşeyleratmakveyadökmek=196
Araçkullanırkenceptelefonuilekonuşmak=427
Kavşakgirişçıkışlarındayayalarailkgeçişhakkınıvermemek=888
Yayageçitlerindeyayayalarailkgeçişhakkınıvermemek=888
Okultaşıdındadurişaretineuymamak=427
Demiryolugeçidindekurallarauymamak=427
Emniyetkemeritakmamak=196
Kasktakmamak=196
Trafikkazasındatedbiralmamak=427
Trafikkazasındaevraklarınıvermemek=427
Trafikkazasındakarşıtarafabilgivermemek=427
Trafikpolisiizinvermedenkazayerindenayrılmak=888
Araçsigortasınıyaptırmamak=196
Amaçdışındaaraçkullanmak=1823
Belediyedenizinalmadanyolcutaşımak=9125
Belediyedenizinalınanşartlardışındayolcutaşımak=3674
Belediyedenizinalınanbölgedışındayolcutaşımak=1823
Belediyedenalınanizinbitmesinerağmenyolcutaşımak=1823

if  (ceza=="Hurdaya çıkarılan aracın işlemlerini yapmamak"):
    print("20/1-a/1 Ceza maddesi gereğince hurdaya çıkarılan aracın işlemleri yapılmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Hurdayaçıkarılanaracınişlemleriniyapmamak,indirim(Hurdayaçıkarılanaracınişlemleriniyapmamak))) 

elif (ceza=="Sattığı aracı ilgili kurumlara bildirmemek"):
    print("20/1-d Ceza maddesi gereğince satılan araç ilgili kurumlara bildirilmediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sattığıaracıilgilikurumlarabildirmemek,indirim(Sattığıaracıilgilikurumlarabildirmemek)))  

elif (ceza=="İhaleden alınan araçlarda gerekli bilgileri vermemek"):
    print("20/1-d-8 Ceza maddesi gereğince ihaleden alınan araçlarda gerekli bilgiler verilmediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(İhaledenalınanaraçlardagereklibilgilerivermemek,indirim(İhaledenalınanaraçlardagereklibilgilerivermemek)))

elif (ceza=="Tescil plakasız araç kullanmak"):
    print("21/1 Ceza maddesi gereğince tescil plakasız araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Tescilplakasızaraçkullanmak,indirim(Tescilplakasızaraçkullanmak)))

elif (ceza=="Hurda belgeli araç kullanmak"):
    print("21/5 Ceza maddesi gereğince hurda belgeli araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Hurdabelgeliaraçkullanmak,indirim(Hurdabelgeliaraçkullanmak)))

elif (ceza=="Araçta ruhsat bulundurmamak"): 
    print("23/2-a Ceza maddesi gereğince araçta ruhsat bulundurulmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçtaruhsatbulundurmamak,indirim(Araçtaruhsatbulundurmamak)))

elif (ceza=="Plakayı yanlış yere takmak"):
    print("23/2-b Ceza maddesi gereğince plakanın yanlış yere takılmasından dolayı {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Plakayıyanlışyeretakmak,indirim(Plakayıyanlışyeretakmak)))

elif (ceza=="App plaka kullanmak"):
    print("23/3-a-1 Ceza maddesi gereğince app plaka kullanımından dolayı {}₺ para cezası  uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Appplakakullanmak,indirim(Appplakakullanmak)))

elif (ceza=="İzin verilen sürede uygun plaka takmamak"):
    print("23/3-a-2 Ceza maddesi gereğince izin verilen süre içerisinde uygun plaka takılmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(İzinverilensüredeuygunplakatakmamak,indirim(İzinverilensüredeuygunplakatakmamak)))
  
elif (ceza=="Araç cinsine göre belirlenen sayıda plaka takmamak"):
    print("23/3-b-1 Ceza maddesi gereğince araç cinsine göre belirlenen sayıda plaka kullanılmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçcinsinegörebelirlenensayıdaplakatakmamak,indirim(Araçcinsinegörebelirlenensayıdaplakatakmamak)))

elif (ceza=="Plaka üzerinde değişiklik yapmak"):
    print("23/3-c-1 Ceza maddesi gereğince plaka üzerinde değişiklik yapıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Plakaüzerindedeğişiklikyapmak,indirim(Plakaüzerindedeğişiklikyapmak)))

elif (ceza=="Plakasız araç kullanmak"):
    print("23/4 Ceza maddesi gereğince plakasız araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Plakasızaraçkullanmak,indirim(Plakasızaraçkullanmak)))

elif (ceza=="Başka aracın plakasını kullanmak"):
    print("23/5-a Ceza maddesi gereğince başka aracın plakası kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Başkaaracınplakasınıkullanmak,indirim(Başkaaracınplakasınıkullanmak)))

elif (ceza=="Sahte plaka takmak"):
    print("23/5-b Ceza maddesi gereğince sahte plaka takıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sahteplakatakmak,indirim(Sahteplakatakmak)))

elif (ceza=="Geçici tescil işlemleri yapmamak"):
    print("25 Ceza maddesi gereğince geçici tescil işlemleri yapılmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Geçicitescilişlemleriyapmamak,indirim(Geçicitescilişlemleriyapmamak)))

elif (ceza=="Araçda bulundurulması gereken donanımları bulundurmamak"):
    print("26/1 Ceza maddesi gereğince araçda bulundurulması gereken donanımların bulundurulmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçdabulundurulmasıgerekendonanımlarıbulundurmamak,indirim(Araçdabulundurulmasıgerekendonanımlarıbulundurmamak)))

elif (ceza=="Mevzuata aykırı ışık kullanmak"):
    print("26/2 Ceza maddesi gereğince mevzuata aykırı ışık kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Mevzuataaykırıışıkkullanmak,indirim(Mevzuataaykırıışıkkullanmak)))

elif (ceza=="Araç üzerinde renk değişikliği veya reklam yapıştırmak"):
    print("26/3 Ceza maddesi gereğince araç üzerinde renk değişikliği veya reklam yapıştırıldığından dolayı {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçüzerinderenkdeğişikliğiveyareklamyapıştırmak,indirim(Araçüzerinderenkdeğişikliğiveyareklamyapıştırmak)))

elif (ceza=="Gerekli ışık donanımı çalışmayan araç kullanmak"):
     print("30/1-a Ceza maddesi gereğince gerekli ışık donanımı çalışmayan araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Gerekliışıkdonanımıçalışmayanaraçkullanmak,indirim(Gerekliışıkdonanımıçalışmayanaraçkullanmak)))

elif (ceza=="Abartı egzoz veya cam filmi kullanmak"):
    print("30/1-b Ceza maddesi gereğince abartı egzoz veya cam filmi kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Abartıegzozveyacamfilmikullanmak,indirim(Abartıegzozveyacamfilmikullanmak)))

elif (ceza=="Araç cinsinde bulundurulması zorunlu gereçleri bulundurmamak"):
    print("31/1-a Ceza maddesi gereğince araç cinsinde bulundurulması zorunlu olan gereçlerin bulundurulmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçcinsindebulundurulmasızorunlugereçleribulundurmamak,indirim(Araçcinsindebulundurulmasızorunlugereçleribulundurmamak)))

elif (ceza=="Ticari araçların takoğraf kullanmaması"):
    print("31/1-b Ceza maddesi gereğince ticari aracın takoğraf kullanmadığı gerekçesiyle {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Ticariaraçlarıntakoğrafkullanmaması,indirim(Ticariaraçlarıntakoğrafkullanmaması)))

elif (ceza=="30 gün içerisinde lpg ruhsata işletmemek"):
    print("32/1 Ceza maddesi gereğince 30 gün içerisinde lpg ruhsata işletilmediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(lpgruhsataişletmemek,indirim(lpgruhsataişletmemek)))

elif (ceza=="Araçlar üzerindeki değişikliklerin uygun olmaması"): 
    print("32/3 Ceza maddesi gereğince araç üzerindeki değişikliklerin uygun olmaması sebebiyle {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçlarüzerindekideğişikliklerinuygunolmaması,indirim(Araçlarüzerindekideğişikliklerinuygunolmaması)))

elif  (ceza=="Muayenesiz araç kullanmak"):
    print("34/a Ceza maddesi gereğince muayenesiz araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Muayenesizaraçkullanmak,indirim(Muayenesizaraçkullanmak)))

elif (ceza=="Muayenesi olmadığı için trafikten men edilen araç kullanmak"):
    print("34/b Ceza maddesi gereğince muayenesi olmadığı için trafikten men edilen araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Muayenesiolmadığıiçintrafiktenmenedilenaraçkullanmak,indirim(Muayenesiolmadığıiçintrafiktenmenedilenaraçkullanmak)))

elif (ceza=="Muayenede ağır kusurlu olan aracı kullanmak"):
    print("34/c Ceza maddesi gereğince muayenede ağır kusurlu olan aracın kullanıldığı gerekçesiyle {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Muayenedeağırkusurluolanaracıkullanmak,indirim(Muayenedeağırkusurluolanaracıkullanmak)))

elif (ceza=="Ehliyetsiz araç kullanmak"):
    print("36/3-a Ceza maddesi gereğince ehliyetsiz araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Ehliyetsizaraçkullanmak,indirim(Ehliyetsizaraçkullanmak)))

elif (ceza=="Ehliyetine el konulmuş kişilerin araç kullanması"):
    print("36/3-b Ceza maddesi gereğince ehliyetine el konulmuş kişinin araç kullandığı gerekçesiyle {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Ehliyetineelkonulmuşkişilerinaraçkullanması,indirim(Ehliyetineelkonulmuşkişilerinaraçkullanması)))

elif (ceza=="Ehliyeti iptal edilmiş kişilerin araç kullanması"):
    print("36/3-c Ceza maddesi gereğince ehliyeti iptal edilmiş kişinin araç kullandığı gerekçesiyle {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Ehliyetiiptaledilmişkişilerinaraçkullanması,indirim(Ehliyetiiptaledilmişkişilerinaraçkullanması)))

elif (ceza=="Ehliyet sınıfı dışında araç kullanmak"):
    print("39/2 Ceza maddesi gereğince ehliyet sınıfı dışında araç kullanıldığı gerekçesiyle {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Ehliyetsınıfıdışındaaraçkullanmak,indirim(Ehliyetsınıfıdışındaaraçkullanmak)))

elif (ceza=="Geçerlilik süresi biten ehliyetle araç kullanmak"):
    print("39/3 Ceza maddesi gereğince geçerlilik süresi biten ehliyetle araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Geçerliliksüresibitenehliyetlearaçkullanmak,indirim(Geçerliliksüresibitenehliyetlearaçkullanmak)))

elif (ceza=="Dış ülke ehliyetiyle belirlenen şartlar dışında araç kullanmak"):
    print("39/4 Ceza maddesi gereğince dış ülke ehliyetiyle belirlenen şartlar dışında araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Dışülkeehliyetiylebelirlenenşartlardışındaaraçkullanmak,indirim(Dışülkeehliyetiylebelirlenenşartlardışındaaraçkullanmak)))

elif (ceza=="Sürücü sertifakasını ehliyete dönüştürmeden araç kullanmak"):
    print("42/11 Ceza maddesi gereğince sürücü sertifakasını ehliyete dönüştürmeden araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sürücüsertifakasınıehliyetedönüştürmedenaraçkullanmak,indirim(Sürücüsertifakasınıehliyetedönüştürmedenaraçkullanmak)))

elif (ceza=="İkamet adresini tescil birimine bildirmemek"):
    print("44/1-a Ceza maddesi gereğince ikamet adresini tescil birimine bildirilmediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(İkametadresinitescilbiriminebildirmemek,indirim(İkametadresinitescilbiriminebildirmemek)))

elif (ceza=="Ehliyeti yanında olmadan araç kullanmak"):
    print("44/1-b Ceza maddesi gereğince ehliyeti yanında olmadan araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Ehliyetiyanındaolmadanaraçkullanmak,indirim(Ehliyetiyanındaolmadanaraçkullanmak)))

elif (ceza=="Hızının gerektirdiği şeritte araç kullanmamak"):
    print("46/2-a Ceza maddesi gereğince hızının gerektirdiği şeritte araç kullanılmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Hızınıngerektirdiğişerittearaçkullanmamak,indirim(Hızınıngerektirdiğişerittearaçkullanmamak)))

elif (ceza=="Şerit değiştirmeden önce gireceği şeridi kontrol etmemek"):
    print("46/2-b Ceza maddesi gereğince şerit değiştirmeden önce gireceği şeridi kontrol etmediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Şeritdeğiştirmedenöncegireceğişeridikontroletmemek,indirim(Şeritdeğiştirmedenöncegireceğişeridikontroletmemek)))

elif (ceza=="Tehlikeli şekilde şerit değiştirmek"):
    print("46/2-c Ceza maddesi gereğince tehlikeli şekilde şerit değiştirildiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Tehlikelişekildeşeritdeğiştirmek,indirim(Tehlikelişekildeşeritdeğiştirmek)))

elif (ceza=="Sürekli sol şeridi kullanmak"):
    print("46/2-d Ceza maddesi gereğince sürekli sol şeridi kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Süreklisolşeridikullanmak,indirim(Süreklisolşeridikullanmak)))

elif (ceza=="Emniyet şeridini kullanmak"):
    print("46/2-f Ceza maddesi gereğince emniyet şeridinin kullanılasından dolayı {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Emniyetşeridinikullanmak,indirim(Emniyetşeridinikullanmak)))

elif (ceza=="Ardı ardına tehlikeli şerit değiştirmek (makas atmak)"):
    print("46/2-g Ceza maddesi gereğince ardı ardına tehlikeli şerit değiştirildiği (Makas atmak) için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(makasatmak,indirim(makasatmak)))

elif (ceza=="Ters yönde araç kullanmak"):
    print("46/2-h Ceza maddesi gereğince ters yönde araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Tersyöndearaçkullanmak,indirim(Tersyöndearaçkullanmak)))

elif (ceza=="Hayvan sürülerinin taşıt yoluna çıkmasını engellememek"):
    print("46/3 Ceza maddesi gereğince hayvan sürülerinin taşıt yoluna çıkmasının engellendiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Hayvansürülerinintaşıtyolunaçıkmasınıengellememek,indirim(Hayvansürülerinintaşıtyolunaçıkmasınıengellememek)))

elif (ceza=="Polisin dur ihtarına uymamak"):
    print("47/1-a Ceza maddesi gereğince polisin dur ihtarına uyulmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Polisindurihtarınauymamak,indirim(Polisindurihtarınauymamak)))

elif (ceza=="Kırımızı ışıkta geçmek"):
    print("47/1-b Ceza maddesi gereğince kırımızı ışıkta geçildiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kırımızıışıktageçmek,indirim(Kırımızıışıktageçmek)))

elif (ceza=="Trafik levhalarına uymamak"):
    print("47/1-c Ceza maddesi gereğince trafik levhalarına uyulmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Trafiklevhalarınauymamak,indirim(Trafiklevhalarınauymamak)))

elif (ceza=="Trafik güvenliğini tehlikeye düşürmek"):
    print("47/1-d Ceza maddesi gereğince trafik güvenliğini tehlikeye soktuğu gerekçesiyle {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Trafikgüvenliğinitehlikeyedüşürmek,indirim(Trafikgüvenliğinitehlikeyedüşürmek)))

elif (ceza=="Alkollü araç kullanmak"):
    print("48/5 Ceza maddesi gereğince alkollü araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Alkollüaraçkullanmak,indirim(Alkollüaraçkullanmak)))

elif (ceza=="Uyuşturucu madde kullanıp araç kullanmak"):
    print("48/8 Ceza maddesi gereğince uyuşturucu madde kullanıp araç kullanıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Uyuşturucumaddekullanıparaçkullanmak,indirim(Uyuşturucumaddekullanıparaçkullanmak)))

elif (ceza=="Alkolmetreye üflememek"):
    print("48/9 Ceza maddesi gereğince alkolmetreye üflemeyi reddettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Alkolmetreyeüflememek,indirim(Alkolmetreyeüflememek)))

elif (ceza=="Ticari araç kullanma sürelerine uymamak"):
    print("49/3 Ceza maddesi gereğince ticari araç kullanma sürelerine uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Ticariaraçkullanmasürelerineuymamak,indirim(Ticariaraçkullanmasürelerineuymamak)))

elif (ceza=="Hız cezası"):
    hizcezasi()

elif (ceza=="Kavşaklara yaklaşırken hızını azaltmamak"):
    print("52/1-a Ceza maddesi gereğince Kavşaklara yaklaşırken hızını azaltmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kavşaklarayaklaşırkenhızınıazaltmamak,indirim(Kavşaklarayaklaşırkenhızınıazaltmamak)))

elif (ceza=="Yol ve trafik durumuna göre davranmamak"):
    print("52/1-b Ceza maddesi gereğince yol ve trafik durumuna göre davranmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yolvetrafikdurumunagöredavranmamak,indirim(Yolvetrafikdurumunagöredavranmamak)))

elif (ceza=="Öndeki araçla güvenli mesafe bırakmamak"):
    print("52/1-c Ceza maddesi gereğince öndeki araçla güvenli mesafe bırakmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Öndekiaraçlagüvenlimesafebırakmamak,indirim(Öndekiaraçlagüvenlimesafebırakmamak)))

elif (ceza=="Konvoy halinde araçlar arasında gerekli mesafe bırakmamak"):
    print("52/1-d Ceza maddesi gereğince konvoy halinde araçlar arasında gerekli mesafe bırakmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Konvoyhalindearaçlararasındagereklimesafebırakmamak,indirim(Konvoyhalindearaçlararasındagereklimesafebırakmamak)))

elif (ceza=="Sağa dönüş kurallarına uymamak"):
    print("53/1-a Ceza maddesi gereğince sağa dönüş kurallarına uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sağadönüşkurallarınauymamak,indirim(Sağadönüşkurallarınauymamak)))

elif (ceza=="Sola dönüş kurallarına uymamak"):
    print("53/1-b Ceza maddesi gereğince sola dönüş kurallarına uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Soladönüşkurallarınauymamak,indirim(Soladönüşkurallarınauymamak)))

elif (ceza=="Dönel kavşak kurallarına uymamak"):
    print("53/1-c Ceza maddesi gereğince dönel kavşak kurallarına uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Dönelkavşakkurallarınauymamak,indirim(Dönelkavşakkurallarınauymamak)))

elif (ceza=="Dönel kavşakta geriye dönüş kurallarına uymamak"):
    print("53/1-d Ceza maddesi gereğince dönel kavşakta geriye dönüş kurallarına uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Dönelkavşaktageriyedönüşkurallarınauymamak,indirim(Dönelkavşaktageriyedönüşkurallarınauymamak)))

elif (ceza=="Sağa veya sola dönüşte yayalara yol vermemek"):
    print("53/2 Ceza maddesi gereğince sağa veya sola dönüşte yayalara yol vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sağaveyasoladönüşteyayalarayolvermemek,indirim(Sağaveyasoladönüşteyayalarayolvermemek)))

elif (ceza=="Hatalı sollama yapmak"):
    print("54/1-a Ceza maddesi gereğince hatalı sollama yaptığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Hatalısollamayapmak,indirim(Hatalısollamayapmak   )))

elif (ceza=="Sollama yapmanın yasak olduğu yerde sollama yapmak"):
    print("54/1-b Ceza maddesi gereğince sollama yapmanın yasak olduğu yerde sollama yaptığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sollamayapmanınyasakolduğuyerdesollamayapmak,indirim(Sollamayapmanınyasakolduğuyerdesollamayapmak)))

elif (ceza=="Geçilme kurallarına uymamak"):
    print("55. Ceza maddesi gereğince geçilme kurallarına uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Geçilmekurallarınauymamak,indirim(Geçilmekurallarınauymamak)))

elif (ceza=="Şerit izleme ve değiştirme kurallarına uymamak"):
    print("56/1-a Ceza maddesi gereğince şerit izleme ve değiştirme kurallarına uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Şeritizlemevedeğiştirmekurallarınauymamak,indirim(Şeritizlemevedeğiştirmekurallarınauymamak)))

elif (ceza=="Karşıdan gelen aracın geçişini zorlaştırmak"):
    print("56/1-b Ceza maddesi gereğince karşıdan gelen aracın geçişini zorlaştırdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Karşıdangelenaracıngeçişinizorlaştırmak,indirim(Karşıdangelenaracıngeçişinizorlaştırmak)))

elif (ceza=="Yakın takip"):
    print("56/1-c Ceza maddesi gereğince yakın takipte bulunduğu için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yakıntakip,indirim(Yakıntakip)))

elif (ceza=="Hız sınırının çok altında araç kullanmak"):
    print("56/1-d Ceza maddesi gereğince hız sınırının çok altında araç kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Hızsınırınınçokaltındaaraçkullanmak,indirim(Hızsınırınınçokaltındaaraçkullanmak)))

elif (ceza=="Dar yollarda araç sınıfına göre geçiş kolaylığı sağlamamak"):
    print("56/1-e Ceza maddesi gereğince dar yollarda araç sınıfına göre geçiş kolaylığı sağlamadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Daryollardaaraçsınıfınagöregeçişkolaylığısağlamamak,indirim(Daryollardaaraçsınıfınagöregeçişkolaylığısağlamamak)))

elif (ceza=="Kavşaklarda ilk geçiş hakkını vermemek"):
    print("57/1-a Ceza maddesi gereğince kavşaklarda ilk geçiş hakkını vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kavşaklardailkgeçişhakkınıvermemek,indirim(Kavşaklardailkgeçişhakkınıvermemek)))

elif (ceza=="Kontrollü kavşaklarda ilk geçiş hakkını vermemek"):
    print("57/1-b Ceza maddesi gereğince kontrollü kavşaklarda ilk geçiş hakkını vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kontrollükavşaklardailkgeçişhakkınıvermemek,indirim(Kontrollükavşaklardailkgeçişhakkınıvermemek)))

elif (ceza=="Kontrolsüz kavşaklarda ilk geçiş hakkını vermemek"):
    print("57/1-c Ceza maddesi gereğince kontrolsüz kavşaklarda ilk geçiş hakkını vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kontrolsüzkavşaklardailkgeçişhakkınıvermemek,indirim(Kontrolsüzkavşaklardailkgeçişhakkınıvermemek)))

elif (ceza=="Yeşil ışık yansa bile duran trafikte kavşağa girmek"):
    print("57/1-d Ceza maddesi gereğince yeşil ışık yansa bile duran trafikte kavşağa girdiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yeşilışıkyansabiledurantrafiktekavşağagirmek,indirim(Yeşilışıkyansabiledurantrafiktekavşağagirmek)))

elif (ceza=="Kavşaklarda duraklamak"):
    print("57/1-e Ceza maddesi gereğince kavşaklarda durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kavşaklardaduraklamak,indirim(Kavşaklardaduraklamak)))

elif (ceza=="Aksine işaret olması bile ray üzerindeki araca ilk geçiş hakkını vermemek"):
    print("57/1-f Ceza maddesi gereğince Aksine işaret olması bile ray üzerindeki araca ilk geçiş hakkını vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Aksineişaretolmasıbilerayüzerindekiaracailkgeçişhakkınıvermemek,indirim(Aksineişaretolmasıbilerayüzerindekiaracailkgeçişhakkınıvermemek)))

elif (ceza=="Yolcu indirme ve bindirme kurallarına uymamak"):
    print("58. Ceza maddesi gereğince yolcu indirme ve bindirme kurallarına uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yolcuindirmevebindirmekurallarınauymamak,indirim(Yolcuindirmevebindirmekurallarınauymamak)))

elif (ceza=="Yerleşim yeri dışında park etme"):
    print("59. Ceza maddesi gereğince yerleşim yeri dışında park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yerleşimyeridışındaparketme,indirim(Yerleşimyeridışındaparketme)))

elif (ceza=="Taşıt yolu üzerinde duraklamak"):
    print("60/1-a Ceza maddesi gereğince taşıt yolu üzerinde durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Taşıtyoluüzerindeduraklamak,indirim(Taşıtyoluüzerindeduraklamak)))

elif (ceza=="Sol şeritte duraklamak"):
    print("60/1-b Ceza maddesi gereğince sol şeritte durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Solşeritteduraklamak,indirim(Solşeritteduraklamak)))

elif (ceza=="Yaya geçidinde duraklamak"):
    print("60/1-c Ceza maddesi gereğince yaya geçidinde durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yayageçidindeduraklamak,indirim(Yayageçidindeduraklamak)))

elif (ceza=="Kavşaklara 5 metre kala duraklamak"):
    print("60/1-d Ceza maddesi gereğince kavşaklara 5 metre kala durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kavşaklara5metrekaladuraklamak,indirim(Kavşaklara5metrekaladuraklamak)))

elif (ceza=="Dönemeçlerde duraklamak"):
    print("60/1-e Ceza maddesi gereğince dönemeçlerde durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Dönemeçlerdeduraklamak,indirim(Dönemeçlerdeduraklamak)))

elif (ceza=="Otobüs duraklarında duraklamak"):
    print("60/1-f Ceza maddesi gereğince otobüs duraklarında durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Otobüsduraklarındaduraklamak,indirim(Otobüsduraklarındaduraklamak)))

elif (ceza=="İkinci sırada duraklamak"):
    print("60/1-g Ceza maddesi gereğince ikinci sırada durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(İkincisıradaduraklamak,indirim(İkincisıradaduraklamak)))

elif (ceza=="Trafik işaretlerinin altında duraklamak"):
    print("60/1-h Ceza maddesi gereğince trafik işaretlerinin altında durakladığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Trafikişaretlerininaltındaduraklamak,indirim(Trafikişaretlerininaltındaduraklamak)))

elif (ceza=="Taşıt yolu üzerinde park etmek"):
    print("61/1-a Ceza maddesi gereğince taşıt yolu üzerinde park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Taşıtyoluüzerindeparketmek,indirim(Taşıtyoluüzerindeparketmek)))

elif (ceza=="Sol şeritte park etmek"):
    print("61/1-b Ceza maddesi gereğince sol şeritte park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Solşeritteparketmek,indirim(Solşeritteparketmek)))

elif (ceza=="Yaya geçidinde park etmek"):
    print("61/1-c Ceza maddesi gereğince yaya geçidine park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yayageçidindeparketmek,indirim(Yayageçidindeparketmek)))

elif (ceza=="Kavşaklara 5 metre kala park etmek"):
    print("61/1-d Ceza maddesi gereğince kavşaklara 5 metre kala park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kavşaklara5metrekalaparketmek,indirim(Kavşaklara5metrekalaparketmek)))

elif (ceza=="Dönemeçlerde park etmek"):
    print("61/1-e Ceza maddesi gereğince dönemeçlerde park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Dönemeçlerdeparketmek,indirim(Dönemeçlerdeparketmek)))

elif (ceza=="Otobüs duraklarında park etmek"):
    print("61/1-f Ceza maddesi gereğince otobüs duraklarında park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Otobüsduraklarındaparketmek,indirim(Otobüsduraklarındaparketmek)))

elif (ceza=="İkinci sırada park etmek"):
    print("61/1-g Ceza maddesi gereğince ikinci sırada park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(İkincisıradaparketmek,indirim(İkincisıradaparketmek)))

elif (ceza=="Trafik işaretlerinin altında park etmek"):
    print("61/1-h Ceza maddesi gereğince trafik işaretlerinin altında park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Trafikişaretlerininaltındaparketmek,indirim(Trafikişaretlerininaltındaparketmek)))

elif (ceza=="İzin verilen zaman dışında park etmek"):
    print("61/1-ı Ceza maddesi gereğince izin verilen zaman dışında park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(İzinverilenzamandışındaparketmek,indirim(İzinverilenzamandışındaparketmek)))

elif (ceza=="Kamunun faydalandığı alanların giriş çıkışına park etmek"):
    print("61/1-j Ceza maddesi gereğince kamunun faydalandığı alanların giriş çıkışına park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kamununfaydalandığıalanlarıngirişçıkışınaparketmek,indirim(Kamununfaydalandığıalanlarıngirişçıkışınaparketmek)))

elif (ceza=="Alt veya üst geçitlerde park etmek"):
    print("61/1-k Ceza maddesi gereğince alt veya üst geçitlerde park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Altveyaüstgeçitlerdeparketmek,indirim(Altveyaüstgeçitlerdeparketmek)))

elif (ceza=="İzin verilen süreden fazla park etmek"):
    print("61/1-l Ceza maddesi gereğince izin verilen süreden fazla park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(İzinverilensüredenfazlaparketmek,indirim(İzinverilensüredenfazlaparketmek)))

elif (ceza=="Resmi araçlara ayrılmış alanlara park etmek"):
    print("61/1-m Ceza maddesi gereğince resmi araçlara ayrılmış alanlara park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Resmiaraçlaraayrılmışalanlaraparketmek,indirim(Resmiaraçlaraayrılmışalanlaraparketmek)))

elif (ceza=="Yaya yollarına park etmek"):
    print("61/1-n Ceza maddesi gereğince yaya yollarına park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yayayollarınaparketmek,indirim(Yayayollarınaparketmek)))

elif (ceza=="Engelli araç park yerine park etmek"):
    print("61/1-o Ceza maddesi gereğince engelli araç park yerine park ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Engelliaraçparkyerineparketmek,indirim(Engelliaraçparkyerineparketmek)))

elif (ceza=="Araçlarda olması gereken ışık donanımlarını bulundurmamak"):
    print("63. Ceza maddesi gereğince araçlarda olması gereken ışık donanımlarını bulundurmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçlardaolmasıgerekenışıkdonanımlarınıbulundurmamak,indirim(Araçlardaolmasıgerekenışıkdonanımlarınıbulundurmamak)))

elif (ceza=="Gerekli alanlarda uzun farlarını kullanmamak"):
    print("64/1-a-1 Ceza maddesine göre gerekli alanlarda uzun farlarını kullanmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Gereklialanlardauzunfarlarınıkullanmamak,indirim(Gereklialanlardauzunfarlarınıkullanmamak)))

elif (ceza=="Akşam farları yakmamak"):
    print("64/1-a-2 Ceza maddesi gereğince akşam farları yakmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Akşamfarlarıyakmamak,indirim(Akşamfarlarıyakmamak)))

elif (ceza=="Arka kenar ışıklarını farlarla birlikte kullanılması"):
    print("64/1-a-3 Ceza maddesi gereğince arka kenar ışıklarını farlarla birlikte kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Arkakenarışıklarınıfarlarlabirliktekullanılması,indirim(Arkakenarışıklarınıfarlarlabirliktekullanılması)))

elif (ceza=="Sis farlarını gereksiz yere kullanmak"):
    print("64/1-b-1 Ceza maddesi gereğince sis farlarını gereksiz yere kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sisfarlarınıgereksizyerekullanmak,indirim(Sisfarlarınıgereksizyerekullanmak)))

elif (ceza=="Dönüş ışıklarını farklı anlamlarda kullanmak"):
    print("64/1-b-2 Ceza maddesi gereğince dönüş ışıklarını farklı anlamlarda kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Dönüşışıklarınıfarklıanlamlardakullanmak,indirim(Dönüşışıklarınıfarklıanlamlardakullanmak)))

elif (ceza=="Gece karşılaşmalarında ışıkları söndürmemek"):
    print("64/1-b-3 Ceza maddesi gereğince gece karşılaşmalarında ışıkları söndürmediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Gecekarşılaşmalarındaışıklarısöndürmemek,indirim(Gecekarşılaşmalarındaışıklarısöndürmemek)))

elif (ceza=="Öndeki aracı geçerken kısa süre dışında uzun farları kullanmak"):
    print("64/1-b-4 Ceza maddesi gereğince öndeki aracı geçerken kısa süre dışında uzun farları kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Öndekiaracıgeçerkenkısasüredışındauzunfarlarıkullanmak,indirim(Öndekiaracıgeçerkenkısasüredışındauzunfarlarıkullanmak)))

elif (ceza=="Yönetmeliğe aykırı ışıklandırma yapmak"):
    print("64/1-b-5 Ceza maddesi gereğince yönetmeliğe aykırı ışıklandırma kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yönetmeliğeaykırıışıklandırmayapmak,indirim(Yönetmeliğeaykırıışıklandırmayapmak)))

elif (ceza=="Sadece park lambalarıyla seyretmek"):
    print("64/1-b-6 Ceza maddesi gereğince sadece park lambalarıyla seyrettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sadeceparklambalarıylaseyretmek,indirim(Sadeceparklambalarıylaseyretmek)))

elif (ceza=="Taşıma sınırı üstünde yolcu almak"):
    print("65/1-a Ceza maddesi gereğince taşıma sınırı üstünde yolcu aldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Taşımasınırıüstündeyolcualmak,indirim(Taşımasınırıüstündeyolcualmak)))

elif (ceza=="Dingil ağırlığından fazla yük taşımak"):
    print("65/1-c Ceza maddesi gereğince dingil ağırlığından fazla yük taşıdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Dingilağırlığındanfazlayüktaşımak,indirim(Dingilağırlığındanfazlayüktaşımak)))

elif (ceza=="Tehlike oluşturabilecek şekilde yük yüklemek"):
    print("65/1-d Ceza maddesi gereğince tehlike oluşturabilecek şekilde yük yüklediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Tehlikeoluşturabilecekşekildeyükyüklemek,indirim(Tehlikeoluşturabilecekşekildeyükyüklemek)))

elif (ceza=="Gerekli izin almadan tehlikeli madde taşımak"):
    print("65/1-e Ceza maddesi gereğince gerekli izin almadan tehlikeli madde taşıdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Gerekliizinalmadantehlikelimaddetaşımak,indirim(Gerekliizinalmadantehlikelimaddetaşımak)))

elif (ceza=="Özel izne tabi olan yükleri izin almadan taşımak"):
    print("65/1-f Ceza maddesi gereğince özel izne tabi olan yükleri izin almadan taşıdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Özeliznetabiolanyükleriizinalmadantaşımak,indirim(Özeliznetabiolanyükleriizinalmadantaşımak)))

elif (ceza=="Gabari dışı yük taşımak"):
    print("65/1-g Ceza maddesi gereğince gabari dışı yük taşıdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Gabaridışıyüktaşımak,indirim(Gabaridışıyüktaşımak)))

elif (ceza=="Yükü karayoluna düşecek veya değecek şekilde yüklemek"):
    print("65/1-h Ceza maddesi gereğince yükü karayoluna düşecek veya değecek şekilde yük yüklendiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yükükarayolunadüşecekveyadeğecekşekildeyüklemek,indirim(Yükükarayolunadüşecekveyadeğecekşekildeyüklemek)))

elif (ceza=="Eğimli yollarda dengeyi bozacak şekilde yük yüklemek"):
    print("65/1-i Ceza maddesi gereğince eğimli yollarda dengeyi bozacak şekilde yük yüklendiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Eğimliyollardadengeyibozacakşekildeyükyüklemek,indirim(Eğimliyollardadengeyibozacakşekildeyükyüklemek)))

elif (ceza=="Sürücünün görüşüne engel olaşak şelikde yük yüklemek"):
    print("65/1-j Ceza maddesi gereğince sürücünün görüşüne engel olacak şelikde yük yüklediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Sürücününgörüşüneengelolaşakşelikdeyükyüklemek,indirim(Sürücününgörüşüneengelolaşakşelikdeyükyüklemek)))

elif (ceza=="Çeken ve çekilen araçlarda tedbir almamak"):
    print("65/1-k Ceza maddesi gereğince çeken ve çekilen araçlarda tedbir alınmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Çekenveçekilenaraçlardatedbiralmamak,indirim(Çekenveçekilenaraçlardatedbiralmamak)))

elif (ceza=="Yol denetim istasyonuna girmemek"):
    print("65/4 Ceza maddesi gereğince Yol denetim istasyonuna girmediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yoldenetimistasyonunagirmemek,indirim(Yoldenetimistasyonunagirmemek)))

elif (ceza=="Kış lastiği kullanmamak"):
    print("65/a Ceza maddesi gereğince kış lastiği kullanmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kışlastiğikullanmamak,indirim(Kışlastiğikullanmamak)))

elif (ceza=="Tehlikeli manevra yapmak"):
    print("67/1-a Ceza maddesi gereğince tehlikeli manevra yaptığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Tehlikelimanevrayapmak,indirim(Tehlikelimanevrayapmak)))

elif (ceza=="Yönetmelikteki belirtilen şartlar dışında geriye dönmek"):
    print("67/1-b Ceza maddesi gereğince yönetmelikteki belirtilen şartlar dışında geriye döndüğü için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yönetmeliktekibelirtilenşartlardışındageriyedönmek,indirim(Yönetmeliktekibelirtilenşartlardışındageriyedönmek)))

elif (ceza=="Dönüşlerde niyetini belli edecek şekilde işaret vermemek"):
    print("67/1-c Ceza maddesi gereğince dönüşlerde niyetini belli edecek şekilde işaret vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Dönüşlerdeniyetinibelliedecekşekildeişaretvermemek,indirim(Dönüşlerdeniyetinibelliedecekşekildeişaretvermemek)))

elif (ceza=="Drift yapmak"):
    print("67/1-d Ceza maddesi gereğince drift yaptığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Driftyapmak,indirim(Driftyapmak)))

elif (ceza=="Yayalara rahatsızlık verecek şekilde sağ şeridi işgal etmek"):
    print("68/1-a-1 Ceza maddesi gereğince yayalara rahatsızlık verecek şekilde sağ şeridi işgal ettiği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yayalararahatsızlıkverecekşekildesağşeridiişgaletmek,indirim(Yayalararahatsızlıkverecekşekildesağşeridiişgaletmek)))

elif (ceza=="Yarış düzenlemek"):
    print("70. Ceza maddesi gereğince yarış düzenlediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yarışdüzenlemek,indirim(Yarışdüzenlemek)))

elif (ceza=="Geçiş üstünlüğü kurallarına uymamak"):
    print("71. Ceza maddesi gereğince geçiş üstünlüğü kurallarına uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Geçişüstünlüğükurallarınauymamak,indirim(Geçişüstünlüğükurallarınauymamak)))

elif (ceza=="Çevreyi rahatsız edici araç kullanmak"):
    print("72. Ceza maddesi gereğince çevreyi rahatsız edici araç kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Çevreyirahatsızediciaraçkullanmak,indirim(Çevreyirahatsızediciaraçkullanmak)))

elif (ceza=="Saygısızca araç kullanmak"):
    print("73/a Ceza maddesi gereğince saygısızca araç kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Saygısızcaaraçkullanmak,indirim(Saygısızcaaraçkullanmak)))

elif (ceza=="Araçtan birşeyler atmak veya dökmek"):
    print("73/b Ceza maddesi gereğince araçtan bir şeyler attığı veya döktüğü için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçtanbirşeyleratmakveyadökmek,indirim(Araçtanbirşeyleratmakveyadökmek)))

elif (ceza=="Araç kullanırken cep telefonu ile konuşmak"):
    print("73/c Ceza maddesi gereğince araç kullanırken cep telefonu ile konuştuğu için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçkullanırkenceptelefonuilekonuşmak,indirim(Araçkullanırkenceptelefonuilekonuşmak)))

elif (ceza=="Kavşak giriş çıkışlarında yayalara ilk geçiş hakkını vermemek"):
    print("74/a Ceza maddesi gereğince kavşak giriş çıkışlarında yayalara ilk geçiş hakkını vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kavşakgirişçıkışlarındayayalarailkgeçişhakkınıvermemek,indirim(Kavşakgirişçıkışlarındayayalarailkgeçişhakkınıvermemek)))

elif (ceza=="Yaya geçitlerinde yayayalara ilk geçiş hakkını vermemek"):
    print("74/b Ceza maddesi gereğince yaya geçitlerinde yayayalara ilk geçiş hakkını vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Yayageçitlerindeyayayalarailkgeçişhakkınıvermemek,indirim(Yayageçitlerindeyayayalarailkgeçişhakkınıvermemek)))

elif (ceza=="Okul taşıdında dur işaretine uymamak"):
    print("75. Ceza maddesi gereğince okul taşıdında dur işaretine uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Okultaşıdındadurişaretineuymamak,indirim(Okultaşıdındadurişaretineuymamak)))

elif (ceza=="Demir yolu geçidinde kurallara uymamak"):
    print("76. Ceza maddesi gereğince demir yolu geçidinde kurallara uymadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Demiryolugeçidindekurallarauymamak,indirim(Demiryolugeçidindekurallarauymamak)))

elif (ceza=="Emniyet kemeri takmamak"):
    print("78/1-a Ceza maddesi gereğince emniyet kemeri takmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Emniyetkemeritakmamak,indirim(Emniyetkemeritakmamak)))

elif (ceza=="Kask takmamak"):
    print("78/1-b Ceza maddesi gereğince kask takmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Kasktakmamak,indirim(Kasktakmamak)))

elif(ceza=="Trafik kazasında tedbir almamak"):
    print("81/1-a Ceza maddesi gereğince trafik kazasında tedbir almadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Trafikkazasındatedbiralmamak,indirim(Trafikkazasındatedbiralmamak)))

elif (ceza=="Trafik kazasında evraklarını vermemek"):
    print("81/1-c Ceza maddesi gereğince trafik kazasında evraklarını vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Trafikkazasındaevraklarınıvermemek,indirim(Trafikkazasındaevraklarınıvermemek)))

elif (ceza=="Trafik kazasında karşı tarafa bilgi vermemek"):
    print("81/1-e Ceza maddesi gereğince trafik kazasında karşı tarafa bilgi vermediği için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Trafikkazasındakarşıtarafabilgivermemek,indirim(Trafikkazasındakarşıtarafabilgivermemek)))

elif (ceza=="Trafik polisi izin vermeden kaza yerinden ayrılmak"):
    print("81/3 Ceza maddesi gereğince trafik polisi izin vermeden kaza yerinden ayrıldığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Trafikpolisiizinvermedenkazayerindenayrılmak,indirim(Trafikpolisiizinvermedenkazayerindenayrılmak)))

elif (ceza=="Araç sigortasını yaptırmamak"):
    print("76. Ceza maddesi gereğince araç sigortasını yaptırmadığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Araçsigortasınıyaptırmamak,indirim(Araçsigortasınıyaptırmamak)))

elif (ceza=="Amaç dışında araç kullanmak"):
    print("Ek-2/1 Ceza maddesi gereğince amaç dışında araç kullandığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Amaçdışındaaraçkullanmak,indirim(Amaçdışındaaraçkullanmak)))

elif (ceza=="Belediyeden izin almadan yolcu taşımak"):
    print("Ek-2/3-a Ceza maddesi gereğince belediyeden izin almadan yolcu taşıdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Belediyedenizinalmadanyolcutaşımak,indirim(Belediyedenizinalmadanyolcutaşımak)))

elif (ceza=="Belediyeden izin alınan şartlar dışında yolcu taşımak"):
    print("Ek-2/3-b Ceza maddesi gereğince belediyeden izin alınan şartlar dışında yolcu taşıdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Belediyedenizinalınanşartlardışındayolcutaşımak,indirim(Belediyedenizinalınanşartlardışındayolcutaşımak)))

elif (ceza=="Belediyeden izin alınan bölge dışında yolcu taşımak"):
    print("Ek-2/3-c Ceza maddesi gereğince belediyeden izin alınan bölge dışında yolcu taşıdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Belediyedenizinalınanbölgedışındayolcutaşımak,indirim(Belediyedenizinalınanbölgedışındayolcutaşımak)))

elif (ceza=="Belediyeden alınan izin bitmesine rağmen yolcu taşımak"):
    print("Ek-2/5 Ceza maddesi gereğince belediyeden izin alınan izin bitmesine rağmen yolcu taşıdığı için {}₺ para cezası uygulanmıştır. İlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(Belediyedenalınanizinbitmesinerağmenyolcutaşımak,indirim(Belediyedenalınanizinbitmesinerağmenyolcutaşımak)))

