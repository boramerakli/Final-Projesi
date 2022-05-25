def indirim(a):
    return a-(a*0.25) 

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
