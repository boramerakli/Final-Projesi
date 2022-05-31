"""
programın çalışması için
tesseract-ocr-w64-setup-v5.1.0.20220510.exe
programı kurulu olmalıdır.


"""

from PyQt5 import QtCore, QtGui, QtWidgets # Arayüz için gerekli kütüphaneleri aktif ettik.++

#arayüz için gerekli kodları pyqt5 designer uygulamasından kopyaladık.
class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(510, 624)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rozet polis.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        dialog.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.591, x2:0.483373, y2:0.602, stop:0 rgba(182, 214, 226, 245), stop:1 rgba(255, 255, 255, 255));")
        dialog.setSizeGripEnabled(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 190, 491, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 120, 151, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("png-transparent-computer-icons-camera-camera-photography-rectangle-camera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 29, 491, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_2)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 310, 491, 130))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setRange(0,1000)
        self.spinBox_2.setRange(0,1000)
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 440, 491, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "CEZA-ÜL SİSTEM-ÜL TESPİT(CST)"))
        dialog.setToolTip(_translate("dialog", "<html><head/><body><p>file:///C:/Users/gomer/OneDrive/Masaüstü/rozet polis.png</p></body></html>"))
        dialog.setWhatsThis(_translate("dialog", "<html><head/><body><p>cvbx</p></body></html>"))
        self.label_5.setText(_translate("dialog", "CEZA TİPİ SEÇİNİZ ;"))
        self.comboBox.setItemText(0, _translate("dialog", "ceza tipi seçiniz..."))
        self.comboBox.setItemText(1, _translate("dialog", "Hız sınırı aşımı"))
        self.comboBox.setItemText(2, _translate("dialog", "Hurdaya çıkarılan aracın işlemlerini yapmamak"))
        self.comboBox.setItemText(3, _translate("dialog", "Sattığı aracı ilgili kurumlara bildirmemek"))
        self.comboBox.setItemText(4, _translate("dialog", "İhaleden alınan araçlarda gerekli bilgileri vermemek"))
        self.comboBox.setItemText(5, _translate("dialog", "Tescil plakasız araç kullanmak"))
        self.comboBox.setItemText(6, _translate("dialog", "Hurda belgeli araç kullanmak"))
        self.comboBox.setItemText(7, _translate("dialog", "Araçta ruhsat bulundurmamak"))
        self.comboBox.setItemText(8, _translate("dialog", "Plakayı yanlış yere takmak"))
        self.comboBox.setItemText(9, _translate("dialog", "App plaka kullanmak"))
        self.comboBox.setItemText(10, _translate("dialog", "İzin verilen sürede uygun plaka takmamak"))
        self.comboBox.setItemText(11, _translate("dialog", "Araç cinsine göre belirlenen sayıda plaka takmamak"))
        self.comboBox.setItemText(12, _translate("dialog", "Plaka üzerinde değişiklik yapmak"))
        self.comboBox.setItemText(13, _translate("dialog", "Plakasız araç kullanmak"))
        self.comboBox.setItemText(14, _translate("dialog", "Başka aracın plakasını kullanmak"))
        self.comboBox.setItemText(15, _translate("dialog", "Sahte plaka takmak"))
        self.comboBox.setItemText(16, _translate("dialog", "Geçici tescil işlemleri yapmamak"))
        self.comboBox.setItemText(17, _translate("dialog", "Araçda bulundurulması gereken donanımları bulundurmamak"))
        self.comboBox.setItemText(18, _translate("dialog", "Mevzuata aykırı ışık kullanmak"))
        self.comboBox.setItemText(19, _translate("dialog", "Araç üzerinde renk değişikliği veya reklam yapıştırmak"))
        self.comboBox.setItemText(20, _translate("dialog", "Gerekli ışık donanımı çalışmayan araç kullanmak"))
        self.comboBox.setItemText(21, _translate("dialog", "Abartı egzoz veya cam filmi kullanmak"))
        self.comboBox.setItemText(22, _translate("dialog", "Araç cinsinde bulundurulması zorunlu gereçleri bulundurmamak"))
        self.pushButton.setText(_translate("dialog", "KAMERA AÇ"))
        self.label.setText(_translate("dialog", " LÜTFEN TARİH SEÇİNİZ ;"))
        self.label_3.setText(_translate("dialog", "HIZ SINIRI ;"))
        self.label_2.setText(_translate("dialog", "UYGULANAN HIZ ;"))
        self.pushButton_2.setText(_translate("dialog", "ONAYLA"))   
        self.init_ui()#programn başlaması için gerekli foksiyonu çağırdık.
        

    def init_ui(self):  # Basılan butonları takip eden fonksiyon.
            self.pushButton.clicked.connect(self.kamera)#butonlara görev atadık.
            self.pushButton_2.clicked.connect(self.cezasec)

    def kamera(self):   # Kamera butonuna basılınca çalışacak fonksiyon.
        import pytesseract
        import cv2
        from PIL import Image   # Gerekli modülleri çağırdık.

        # Görüntüden yazı okuyacak kütüphane için gerekli ortamları kurduk.
        pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\gomer\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

        cap = cv2.VideoCapture(0)#kamerayı açmak için kullandığımız kod
        

        match = True    # İstediğimiz zaman döngüden çıkabilmek için döngüyü bağlı tutacak bir değişken atadık.

        while match:
            _, frame = cap.read()   # Görüntüyü kare kare kameradan okuyacak.

            metin = pytesseract.image_to_string(Image.fromarray(frame))  # okunan yazıyı kaydeden fonksiyon 
             #bütün plakalara ve ait olduğu kişileri bulamadığımızdan dolayı kendi sözlüğümüzü oluşturduk.
            plakalar = {"KEREM OZBAL": "34 TO 2015", "ALPER YUKSEL" : "16 NOG 95", "RAGIP DUNDAR" : "06 HBT 11",
                        "ADNAN MUTU": "06 ANK 06", "ISMAIL GUNDUZ" : "31 A 0001", "TEOMAN ARSLAN" : "17 CNK 17",
                        "MERVE ARIK": "34 BUF 80", "TUBAĞ SEZGİN": "16 UCB 25", "ALPEREN ÇAKICI" : "34 TS 061",
                        "ŞEVVAL YILDIZ": "34 MEH 52"}   # Plaka isim eşleştirmelerini sözlük kullanarak yaptık.

            print(metin.strip()) #okunan plakayı yazdırıyor.

            cv2.imshow("Window", frame)  # Okunan görüntü 'Window' adlı pencerede görüntüleniyor.

            for i,j in plakalar.items():    # Okunan plakanın sözlükte olup olmadığını kontrol ettik.
                if metin.strip() == j:      # Eğer varsa isim ve plaka değişkenlerine atadık.
                    global plaka,isim       # Atadıktan sonra kameranın kapanmasını sağladık.
                    isim = i 
                    plaka = j
                    print(isim)
                    cap.release()
                    cv2.destroyAllWindows()
                    match = False  #döngüden çıkabilmek için kullandık

            if cv2.waitKey(1) == ord("q"): #uygulamanın manuel kapatılmasını sağlıyor
                break

        cap.release()
        cv2.destroyAllWindows()
        
        self.pushButton_2.clicked.connect(self.cezasec)     # Onayla butonuna basıldıktan sonra cezalar kısmına geçen fonksiyonu çağırdık.

    def cezasec(self):  # Cezaları para değerleriyle sözlük olarak kaydettik.
        cezalar = {"Hurdaya çıkarılan aracın işlemlerini yapmamak":427,
                   "Sattığı aracı ilgili kurumlara bildirmemek":3340,
                   "İhaleden alınan araçlarda gerekli bilgileri vermemek": 427,
                   "Tescil plaklasız araç kullanmak": 1823,
                   "Hurda belgeli araç kullanmak": 3674,
                   "Araçta ruhsat bulundurmamak": 166,
                   "Plakayı yanlış yere takmak": 166,
                   "App plaka kullanmak": 750,
                   "İzin verilen sürede uygun plaka takmamak": 1536,
                   "Araç cinsine göre belirlenen sayıda plaka takmamak": 750,
                   "Plaka üzerinde değişiklik yapmak": 750,
                   "Plakasız araç kullanmak": 3093,
                   "Başka aracın plakasını kullanmak": 9107,
                   "Sahte plaka takmak": 9107,
                   "Geçici tescil işlemleri yapmamak": 427,
                   "Araçda bulundurulması gereken donanımları bulundurmamak": 196,
                   "Mevzuata aykırı ışık kullanmak": 1823,
                   "Araç üzerinde renk değişikliği veya reklam yapıştırmak": 196,
                   "Gerekli ışık donanımı çalışmayan araç kullanmak": 196,
                   "Abartı egzoz veya cam filmi kullanmak": 427,
                   "Araç cinsinde bulundurulması zorunlu gereçleri bulundurmamak": 196}
        
        if self.comboBox.currentText() == "Hız sınırı aşımı":   # Hız sınırı cezası olması durumunda gerekli kontrolleri yaptık.
            if int(self.spinBox.text()) < int(self.spinBox_2.text())*1.1:
                self.label_4.setText("Ceza uygulanmasını gerektirecek bir durum yoktur.")
            elif int(self.spinBox.text()) > int(self.spinBox_2.text())*1.1 and int(self.spinBox.text()) <= int(self.spinBox_2.text())*1.3:
                self.label_4.setText("{} tarihinde {} plakalı araç sahibi {} adlı kişiye\nhız sınırını %10 ile %30 arasında geçtiği için 427₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse 320.25₺'ye indirim uygulanacaktır. ".format(self.dateTimeEdit.text(),plaka,isim))
            elif int(self.spinBox.text()) > int(self.spinBox_2.text())*1.3 and int(self.spinBox.text()) <= int(self.spinBox_2.text())*1.5:
                self.label_4.setText("{} tarihinde {} plakalı araç sahibi {} adlı kişiye\nhız sınırını %30 ile %50 arasında geçtiği için 888₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse 666₺'ye indirim uygulanacaktır. ".format(self.dateTimeEdit.text(),plaka,isim))
            else:   
                self.label_4.setText("{} tarihinde {} plakaları araç sahibi {} adlı kişiye\nhız sınırını %50'den fazla aştığı için 1823₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse 1367.25₺'ye indirim uygulanacaktır.".format(self.dateTimeEdit.text(),plaka,isim))
                #diğer ceza tipleri için çıktı veren fonksiyonlar
        elif self.comboBox.currentText() == "ceza tipi seçiniz...":
            self.label_4.setText("Lütfen ceza tipi seçin")
        else:
            self.label_4.setText("{} tarihinde {} plakalı araç sahibi {} adlı kişiye\n{} suçundan dolayı\n{}₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(self.dateTimeEdit.text(),plaka,isim,self.comboBox.currentText(),cezalar[self.comboBox.currentText()],int(cezalar[self.comboBox.currentText()])*0.85))
            






if __name__ == "__main__":  # Kodun terminalden mi ide'den mi çalıştırıldığını kontrol ettik ve en başta programı çalıştırıyor.
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show() # arayüz ekranını açmaya yarıyor.
    sys.exit(app.exec_())
