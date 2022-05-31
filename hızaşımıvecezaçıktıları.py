if self.comboBox.currentText() == "Hız sınırı aşımı":  
            if int(self.spinBox.text()) < int(self.spinBox_2.text())*1.1:
                self.label_4.setText("Ceza uygulanmasını gerektirecek bir durum yoktur.")
            elif int(self.spinBox.text()) > int(self.spinBox_2.text())*1.1 and int(self.spinBox.text()) <= int(self.spinBox_2.text())*1.3:
                self.label_4.setText("{} tarihinde {} plakalı araç sahibi {} adlı kişiye\nhız sınırını %10 ile %30 arasında geçtiği için 427₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse 320.25₺'ye indirim uygulanacaktır. ".format(self.dateTimeEdit.text(),plaka,isim))
            elif int(self.spinBox.text()) > int(self.spinBox_2.text())*1.3 and int(self.spinBox.text()) <= int(self.spinBox_2.text())*1.5:
                self.label_4.setText("{} tarihinde {} plakalı araç sahibi {} adlı kişiye\nhız sınırını %30 ile %50 arasında geçtiği için 888₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse 666₺'ye indirim uygulanacaktır. ".format(self.dateTimeEdit.text(),plaka,isim))
            else:   
                self.label_4.setText("{} tarihinde {} plakaları araç sahibi {} adlı kişiye\nhız sınırını %50'den fazla aştığı için 1823₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse 1367.25₺'ye indirim uygulanacaktır.".format(self.dateTimeEdit.text(),plaka,isim))
        elif self.comboBox.currentText() == "ceza tipi seçiniz...":
            self.label_4.setText("Lütfen ceza tipi seçin")
        else:
            self.label_4.setText("{} tarihinde {} plakalı araç sahibi {} adlı kişiye\n{} suçundan dolayı\n{}₺ para cezası uygulanmıştır.\nİlk 15 gün içerisinde ödenirse {}₺'ye indirim uygulanacaktır.".format(self.dateTimeEdit.text(),plaka,isim,self.comboBox.currentText(),cezalar[self.comboBox.currentText()],int(cezalar[self.comboBox.currentText()])*0.85))
