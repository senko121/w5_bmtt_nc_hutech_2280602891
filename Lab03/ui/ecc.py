
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests  
from PyQt5.QtWidgets import QMessageBox  

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platfroms"

class Ui_MainWindow(object):
    def setupUi(self, Ui_MainWindow):
        Ui_MainWindow.setObjectName("Ui_MainWindow")
        Ui_MainWindow.resize(937, 522)
        self.centralwidget = QtWidgets.QWidget(Ui_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 70, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, -20, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.txt_information = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_information.setGeometry(QtCore.QRect(250, 110, 511, 91))
        self.txt_information.setObjectName("txt_information")
        
        self.txt_signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(250, 270, 511, 87))
        self.txt_signature.setObjectName("txt_signature")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.btn_generate_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate_keys.setGeometry(QtCore.QRect(610, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_generate_keys.setFont(font)
        self.btn_generate_keys.setObjectName("btn_generate_keys")
        
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(560, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_verify.setFont(font)
        self.btn_verify.setObjectName("btn_verify")
        
        Ui_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 26))
        self.menubar.setObjectName("menubar")
        Ui_MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(Ui_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Ui_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow)


    def retranslateUi(self, Ui_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow.setWindowTitle(_translate("Ui_MainWindow", "MainWindow"))
        self.label_2.setText(_translate("Ui_MainWindow", "ECC CIPHER "))
        self.label_3.setText(_translate("Ui_MainWindow", "INFORMATION "))
        self.label_4.setText(_translate("Ui_MainWindow", "SIGNATURE"))
        self.pushButton.setText(_translate("Ui_MainWindow", "SIGN"))
        self.btn_generate_keys.setText(_translate("Ui_MainWindow", "GENERATE KEYS"))
        self.btn_verify.setText(_translate("Ui_MainWindow", "VERIFY"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())   
