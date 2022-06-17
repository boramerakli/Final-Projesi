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



