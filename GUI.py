#This is a simpel Ali Express scraper that made by Ahmad Abdelbaset
#Contact details: ahmad.abdelbaset@outlook.com
#Linkedin: https://www.linkedin.com/in/ahmadabdelbaset/
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import AutoSel as AS
from PyQt5.QtWidgets import QMessageBox

Path = ''
MaxProducts = 1000
n_qty = MaxProducts+1

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setFixedSize(385, 430)

        self.search_lineEdit = QtWidgets.QLineEdit(dialog)
        self.search_lineEdit.setGeometry(QtCore.QRect(90, 20, 181, 21))
        self.search_lineEdit.setMaxLength(40)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setObjectName("search_lineEdit")

        self.Brows_pushButton = QtWidgets.QPushButton(dialog)
        self.Brows_pushButton.setGeometry(QtCore.QRect(290, 340, 81, 28))
        self.Brows_pushButton.clicked.connect(self.getPath)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.Brows_pushButton.setFont(font)
        self.Brows_pushButton.setObjectName("Brows_pushButton")

        self.Products_label = QtWidgets.QLabel(dialog)
        self.Products_label.setGeometry(QtCore.QRect(10, 20, 80, 21))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.Products_label.setFont(font)
        self.Products_label.setObjectName("Products_label")

        self.WhatToScrape_label = QtWidgets.QLabel(dialog)
        self.WhatToScrape_label.setGeometry(QtCore.QRect(10, 60, 141, 21))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.WhatToScrape_label.setFont(font)
        self.WhatToScrape_label.setObjectName("WhatToScrape_label")
        self.Price_checkBox = QtWidgets.QCheckBox(dialog)
        self.Price_checkBox.setGeometry(QtCore.QRect(30, 100, 101, 16))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.Price_checkBox.setFont(font)
        self.Price_checkBox.setObjectName("Price_checkBox")
        self.Description_checkBox = QtWidgets.QCheckBox(dialog)
        self.Description_checkBox.setGeometry(QtCore.QRect(30, 130, 101, 22))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.Description_checkBox.setFont(font)
        self.Description_checkBox.setObjectName("Description_checkBox")
        self.SalesAmount_checkBox = QtWidgets.QCheckBox(dialog)
        self.SalesAmount_checkBox.setGeometry(QtCore.QRect(30, 160, 161, 16))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.SalesAmount_checkBox.setFont(font)
        self.SalesAmount_checkBox.setObjectName("SalesAmount_checkBox")
        self.ProductLink_checkBox = QtWidgets.QCheckBox(dialog)
        self.ProductLink_checkBox.setGeometry(QtCore.QRect(30, 190, 121, 20))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.ProductLink_checkBox.setFont(font)
        self.ProductLink_checkBox.setObjectName("ProductLink_checkBox")
        self.Rate_checkBox = QtWidgets.QCheckBox(dialog)
        self.Rate_checkBox.setGeometry(QtCore.QRect(30, 220, 81, 16))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.Rate_checkBox.setFont(font)
        self.Rate_checkBox.setObjectName("Rate_checkBox")
        self.ShippingDetails_checkBox = QtWidgets.QCheckBox(dialog)
        self.ShippingDetails_checkBox.setGeometry(QtCore.QRect(30, 250, 141, 20))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.ShippingDetails_checkBox.setFont(font)
        self.ShippingDetails_checkBox.setObjectName("ShippingDetails_checkBox")
        self.NumberOfProducts_label = QtWidgets.QLabel(dialog)
        self.NumberOfProducts_label.setGeometry(QtCore.QRect(10, 300, 180, 21))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.NumberOfProducts_label.setFont(font)
        self.NumberOfProducts_label.setObjectName("NumberOfProducts_label")
        self.qty_lineEdit = QtWidgets.QLineEdit(dialog)
        self.qty_lineEdit.setGeometry(QtCore.QRect(200, 300, 80, 21))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.qty_lineEdit.setFont(font)
        self.qty_lineEdit.setObjectName("qty_lineEdit")
        self.Output_label = QtWidgets.QLabel(dialog)
        self.Output_label.setGeometry(QtCore.QRect(10, 340, 161, 21))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.Output_label.setFont(font)
        self.Output_label.setObjectName("Output_label")
        self.FilePath_lineEdit = QtWidgets.QLineEdit(dialog)
        self.FilePath_lineEdit.setGeometry(QtCore.QRect(120, 340, 160, 21))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.FilePath_lineEdit.setFont(font)
        self.FilePath_lineEdit.setObjectName("FilePath_lineEdit")

        #self.progressBar = QtWidgets.QProgressBar(dialog)
        #self.progressBar.setGeometry(QtCore.QRect(10, 410, 411, 23))
        font = QtGui.QFont()

        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        #self.progressBar.setFont(font)
        #self.progressBar.setProperty("value", 24)
        #self.progressBar.setObjectName("progressBar")

        self.ScrapeNow_pushButton = QtWidgets.QPushButton(dialog)
        self.ScrapeNow_pushButton.setGeometry(QtCore.QRect(10, 375, 360, 28))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.ScrapeNow_pushButton.setFont(font)
        self.ScrapeNow_pushButton.setObjectName("ScrapeNow_pushButton")
        self.ScrapeNow_pushButton.clicked.connect(self.Scrape)

        #self.About_pushButton = QtWidgets.QPushButton(dialog)
        #self.About_pushButton.setGeometry(QtCore.QRect(290, 370, 81, 28))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        #self.About_pushButton.setFont(font)
        #self.About_pushButton.setObjectName("About_pushButton")

        self.Linkedin_label = QtWidgets.QLabel(dialog)
        self.Linkedin_label.setGeometry(QtCore.QRect(10, 405, 360, 28))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.Linkedin_label.setFont(font)
        self.Linkedin_label.setObjectName("Linkedin_label")


        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "AliExpress Scraper"))
        self.Brows_pushButton.setText(_translate("dialog", "Browse"))
        self.Products_label.setText(_translate("dialog", "Product:"))
        self.WhatToScrape_label.setText(_translate("dialog", "What to scrape?"))
        self.Price_checkBox.setText(_translate("dialog", "Price"))
        self.Description_checkBox.setText(_translate("dialog", "Description"))
        self.SalesAmount_checkBox.setText(_translate("dialog", "Sales Amount"))
        self.ProductLink_checkBox.setText(_translate("dialog", "Product Link"))
        self.Rate_checkBox.setText(_translate("dialog", "Rate"))
        self.ShippingDetails_checkBox.setText(_translate("dialog", "Shipping Details"))
        self.NumberOfProducts_label.setText(_translate("dialog", "How many products?"))
        self.Output_label.setText(_translate("dialog", "Output File:"))
        self.ScrapeNow_pushButton.setText(_translate("dialog", "Scrape Now"))
        #self.About_pushButton.setText(_translate("dialog", "About"))
        #self.Linkedin_label.setText(_translate("dialog", "Click Here"))

        self.Linkedin_label.setText('''<a href='https://www.linkedin.com/in/ahmadabdelbaset/'>For more Information, click here to contact </a>''')
        self.Linkedin_label.setOpenExternalLinks(True)


    def check_what_checked(self):
        Price = False
        ProductName = False
        ProductLink = False
        Shipping = False
        Rate = False
        Sold = False
        if self.Description_checkBox.isChecked():
            ProductName = True
        if self.Price_checkBox.isChecked():
            Price = True
        if self.ProductLink_checkBox.isChecked():
            ProductLink = True
        if self.ShippingDetails_checkBox.isChecked():
            Shipping = True
        if self.Rate_checkBox.isChecked():
            Rate = True
        if self.SalesAmount_checkBox.isChecked():
            Sold = True

        return Price, ProductName, ProductLink, Shipping, Rate, Sold


    def getPath(self):
        file = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        global Path
        Path = file.replace('/','\\\\')
        self.FilePath_lineEdit.setText(Path)


    def Scrape(self):
        global n_qty
        if self.qty_lineEdit.text() == '':
            print("Error: Enter products number between 0 and 1000")
        else:
            n_qty = int(self.qty_lineEdit.text())

            Price, ProductName, ProductLink, Shipping, Rate, Sold = self.check_what_checked()

            if (Price==False and ProductName==False and ProductLink==False and Shipping==False and Rate==False and Sold==False):
                print("Error: Please Check Something")

            elif Path == '' or self.search_lineEdit.text()=='':
                print("Error: Please choose file path or product or number of products")

            else:
                if n_qty > 0 and n_qty < MaxProducts:
                    AS.search_for(self.search_lineEdit.text(), int(self.qty_lineEdit.text()),Path, Price, ProductName, ProductLink, Shipping, Rate, Sold)
                else:
                    print("Error: Enter products number between 0 and 1000")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())



