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

elif (ceza=="f"):
    print("a")