# CEZA TESPİT SİSTEMİ
#
Önceden sisteme kaydedilmiş olan plaka kodlarını kamera yardımı ile görüntüyü okuyarak tespit edip bu plakalar üzerinde işlemler yapılmasına kolaylık sağlayan bir 
ceza sistemidir.

Bu sistemde pytesseract ile OCR (optik karakter tanıma) sistemi kullanılmıştır.

Bunların yanında pyqt5 gibi ara yüz geliştirme programlarından yardım alınmıştır ve
görüntü işleme için kullandığımız OpenCV kütüphanemizde projemizde yer almaktadır.

## Görüntüden yazı okuyacak kütüphane için gerekli ortamları kurduk.
#
 ```
        pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\gomer\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe" 
 ```
 
 # ![ocr](https://user-images.githubusercontent.com/105217625/174186794-085a3866-ea45-4ff2-9ade-0e053c700792.jpg)

## Ceza tipi seçildikten sonra bize ceza çıktısını vericek olan kodu yazdık.
#
``` 
        self.label_4.setText("{} tarihinde {} plakalı araç sahibi {} adlı kişiye\n{} suçundan dolayı\n{}₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(self.dateTimeEdit.text(),plaka,isim,self.comboBox.currentText(),cezalar[self.comboBox.currentText()],int(cezalar[self.comboBox.currentText()])*0.85))
          
```
## Ceza çıktısını arayüz üzerinde denedik.
#
![arayüz](https://user-images.githubusercontent.com/105217625/174190525-981f6c8f-c3a2-4212-90ce-b22f2f685d13.png)

## GEREKSİNİMLER
#
```
         Python3.10

         tesseract-ocr-w64-setup-v5.1.0.20220510.exe
```
## Gerekli kütüphaneler
#
##### PyQt5
##### Pytesseract
##### Opencv


## Ceza tespit sistemi nasıl çalışır?
#
#### Sistemi başlattığımız zaman öncelikle tarih ve saat bilgileri girilmektedir 
#### Kamera butonuna basılarak kameranın aktif olması beklenmektedir. Kamera aktif olduktan sonra aracın plakası taratılmalıdır.
#### Sonraki adımda ise 2 farklı yol izlenmektedir.
#### Hız limiti cezası seçeneği seçildiyse hız limiti ve uygulanan hız girildikten sonra ceza çıktısı alınabilir.
#### Diğer bir ceza tipi seçildiyse hız bilgileri girilmeden ceza çıktısı alınabilmektedir.


## PROJE TANITIM VİDEOSU
#
https://user-images.githubusercontent.com/105217625/174192371-5d61cb80-0972-4668-b1a8-7a7b192c2ad1.mp4
#
#
1-Hurdaya çıkarılan aracın işlemlerini yapmamak
2-Sattığı aracı ilgili kurumlara bildirmemek
3-İhaleden alınan araçlarda gerekli bilgileri vermemek
4-Tescil plakasız araç kullanmak
5-Hurda belgeli araç kullanmak
6-Araçta ruhsat bulundurmamak
7-Plakayı yanlış yere takmak
8-App plaka kullanmak
9-İzin verilen sürede uygun plaka takmamak
10-Araç cinsine göre belirlenen sayıda plaka takmamak 
11-Plaka üzerinde değişiklik yapmak
12-Plakasız araç kullanmak
13-Başka aracın plakasını kullanmak
14-Sahte plaka takmak
15-Geçici tescil işlemleri yapmamak
16-Araçda bulundurulması gereken donanımları bulundurmamak
17-Mevzuata aykırı ışık kullanmak
18-Araç üzerinde renk değişikliği veya reklam yapıştırmak
19-Gerekli ışık donanımı çalışmayan araç kullanmak
20-Abartı egzoz veya cam filmi kullanmak
21-Araç cinsinde bulundurulması zorunlu gereçleri bulundurmamak
22-Ticari araçların takoğraf kullanmaması
23-30 gün içerisinde lpg ruhsata işletmemek
24-Araçlar üzerindeki değişikliklerin uygun olmaması
25-Muayenesiz araç kullanmak
26-Muayenesi olmadığı için trafikten men edilen araç kullanmak
27-Muayenede ağır kusurlu olan aracı kullanmak
28-Ehliyetsiz araç kullanmak
29-Ehliyetine el konulmuş kişilerin araç kullanması
30-Ehliyeti iptal edilmiş kişilerin araç kullanması
31-Ehliyet sınıfı dışında araç kullanmak
32-Geçerlilik süresi biten ehliyetle araç kullanmak
33-Dış ülke ehliyetiyle belirlenen şartlar dışında araç kullanmak
34-Sürücü sertifakasını ehliyete dönüştürmeden araç kullanmak
35-İkamet adresini tescil birimine bildirmemek
36-Ehliyeti yanında olmadan araç kullanmak
37-Hızının gerektirdiği şeritte araç kullanmamak
38-Şerit değiştirmeden önce gireceği şeridi kontrol etmemek
39-Tehlikeli şekilde şerit değiştirmek
40-Sürekli sol şeridi kullanmak
41-Emniyet şeridini kullanmak
42-Ardı ardına tehlikeli şerit değiştirmek (makas atmak)
43-Ters yönde araç kullanmak
44-Hayvan sürülerinin taşıt yoluna çıkmasını engellememek
45-Polisin dur ihtarına uymamak
46-Kırımızı ışıkta geçmek
47-Trafik levhalarına uymamak
48-Trafik güvenliğini tehlikeye düşürmek
49-Alkollü araç kullanmak
50-Uyuşturucu madde kullanıp araç kullanmak
51-Alkolmetreye üflememek
52-Ticari araç kullanma sürelerine uymamak
53-Hız cezası
54-Kavşaklara yaklaşırken hızını azaltmamak
55-Yol ve trafik durumuna göre davranmamak
56-Öndeki araçla güvenli mesafe bırakmamak
57-Konvoy halinde araçlar arasında gerekli mesafe bırakmamak
58-Sağa dönüş kurallarına uymamak
59-Sola dönüş kurallarına uymamak
60-Dönel kavşak kurallarına uymamak
61-Dönel kavşakta geriye dönüş kurallarına uymamak
62-Sağa veya sola dönüşte yayalara yol vermemek
63-Hatalı sollama yapmak
64-Sollama yapmanın yasak olduğu yerde sollama yapmak
65-Geçilme kurallarına uymamak
66-Şerit izleme ve değiştirme kurallarına uymamak
67-Karşıdan gelen aracın geçişini zorlaştırmak
68-Yakın takip
69-Hız sınırının çok altında araç kullanmak
70-Dar yollarda araç sınıfına göre geçiş kolaylığı sağlamamak
71-Kavşaklarda ilk geçiş hakkını vermemek
72-Kontrollü kavşaklarda ilk geçiş hakkını vermemek
73-Kontrolsüz kavşaklarda ilk geçiş hakkını vermemek
74-Yeşil ışık yansa bile duran trafikte kavşağa girmek
75-Kavşaklarda duraklamak
76-Aksine işaret olması bile ray üzerindeki araca ilk geçiş hakkını vermemek
77-Yolcu indirme ve bindirme kurallarına uymamak
78-Yerleşim yeri dışında park etme
79-Taşıt yolu üzerinde duraklamak
80-Sol şeritte duraklamak
81-Yaya geçidinde duraklamak
82-Kavşaklara 5 metre kala duraklamak
83-Dönemeçlerde duraklamak
84-Otobüs duraklarında duraklamak
85-İkinci sırada duraklamak
86-Trafik işaretlerinin altında duraklamak
87-Taşıt yolu üzerinde park etmek
88-Sol şeritte park etmek
89-Yaya geçidinde park etmek
90-Kavşaklara 5 metre kala park etmek
91-Dönemeçlerde park etmek
92-Otobüs duraklarında park etmek
93-İkinci sırada park etmek
94-Trafik işaretlerinin altında park etmek
95-İzin verilen zaman dışında park etmek
96-Kamunun faydalandığı alanların giriş çıkışına park etmek
97-Alt veya üst geçitlerde park etmek
98-İzin verilen süreden fazla park etmek
99-Resmi araçlara ayrılmış alanlara park etmek
100-Yaya yollarına park etmek
101-Engelli araç park yerine park etmek
102-Araçlarda olması gereken ışık donanımlarını bulundurmamak
103-Gerekli alanlarda uzun farlarını kullanmamak
104-Akşam farları yakmamak
105-Arka kenar ışıklarını farlarla birlikte kullanılması
106-Sis farlarını gereksiz yere kullanmak
107-Dönüş ışıklarını farklı anlamlarda kullanmak
108-Gece karşılaşmalarında ışıkları söndürmemek
109-Öndeki aracı geçerken kısa süre dışında uzun farları kullanmak
110-Yönetmeliğe aykırı ışıklandırma yapmak
111-Sadece park lambalarıyla seyretmek
112-Taşıma sınırı üstünde yolcu almak
113-Dingil ağırlığından fazla yük taşımak
114-Tehlike oluşturabilecek şekilde yük yüklemek
115-Gerekli izin almadan tehlikeli madde taşımak
116-Özel izne tabi olan yükleri izin almadan taşımak
117-Gabari dışı yük taşımak
118-Yükü karayoluna düşecek veya değecek şekilde yüklemek
119-Eğimli yollarda dengeyi bozacak şekilde yük yüklemek
120-Sürücünün görüşüne engel olaşak şelikde yük yüklemek
121Çeken ve çekilen araçlarda tedbir almamak
122-Yol denetim istasyonuna girmemek
123-Kış lastiği kullanmamak
124-Tehlikeli manevra yapmak
125-Yönetmelikteki belirtilen şartlar dışında geriye dönmek
126-Dönüşlerde niyetini belli edecek şekilde işaret vermemek
127-Drift yapmak
128-Yayalara rahatsızlık verecek şekilde sağ şeridi işgal etmek
129-Yarış düzenlemek
130-Geçiş üstünlüğü kurallarına uymamak
131-Çevreyi rahatsız edici araç kullanmak
132-Saygısızca araç kullanmak
133-Araçtan birşeyler atmak veya dökmek
134-Araç kullanırken cep telefonu ile konuşmak
135-Kavşak giriş çıkışlarında yayalara ilk geçiş hakkını vermemek
136-Yaya geçitlerinde yayayalara ilk geçiş hakkını vermemek
137-Okul taşıdında dur işaretine uymamak
138-Demir yolu geçidinde kurallara uymamak
139-Emniyet kemeri takmamak
140-Kask takmamak
141-Trafik kazasında tedbir almamak
142-Trafik kazasında evraklarını vermemek
143-Trafik kazasında karşı tarafa bilgi vermemek
144-Trafik polisi izin vermeden kaza yerinden ayrılmak
145-Araç sigortasını yaptırmamak
146-Amaç dışında araç kullanmak
147-Belediyeden izin almadan yolcu taşımak
148-Belediyeden izin alınan şartlar dışında yolcu taşımak
149-Belediyeden izin alınan bölge dışında yolcu taşımak
150-Belediyeden alınan izin bitmesine rağmen yolcu taşımak
#

## Kullanılan kaynaklar ve alınan yardımlar
#
https://youtu.be/4BfvPCMvcPA

https://youtu.be/mV5NwcxE3U0

https://youtu.be/vMfHcFQ9rz4

https://github.com/JaidedAI/EasyOCR

#
https://stackoverflow.com/
#
https://github.com/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama
#
https://www.udemy.com/course/python-dersleri-veri-bilimi-ve-makine-ogrenmesine-hazirlik/
#
https://www.udemy.com/share/101Wcu3@XPWXIwT7mWrU6icPlDPojSDodc0t9tYKEnZGbdMUPNedCByJz3c2xwTAf1xCcnLaNA==/
#
MUHAMMED FARUK ERDOĞMUŞ : muhammederdogmus537@gmail.com



