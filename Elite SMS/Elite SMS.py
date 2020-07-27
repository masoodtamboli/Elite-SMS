from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from window2 import Ui_MainWindow1
from PyQt5.QtWidgets import QMessageBox,QLineEdit
from PyQt5.QtGui import QPixmap
import urllib.request
class Ui_MainWindow(object):
    def connect1(self):
        host = 'http://google.com'
        try:
            urllib.request.urlopen(host)
            return True
        except:
            pass

    def gotomain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()       
        self.username = (self.lineEdit.text())
        self.Password = (self.lineEdit_2.text()) 

        if self.connect1()==True:
            if self.username=='faruk' and self.Password=='1234':
                self.ui.setupUi(self.window)
                MainWindow.hide()
                self.window.show()
            
            elif self.username=='' and self.Password=='':
                msg = QMessageBox()
                msg.setWindowTitle("ERROR")
                msg.setText("Username or Password is Empty")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("ERROR")
                msg.setText("Username or Password is Wrong")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Please connect to Internet')
            retval = msg.exec_()
    
    def checkRadio(self):
        with open('placename.txt','r') as file1:
            addr = file1.readline()
            if addr == '':
                self.radioSayyed.setEnabled(True)
                self.radioSheval.setEnabled(True)
                self.radiokatraj.setEnabled(True)
            else:
                self.radioSayyed.setEnabled(False)
                self.radioSheval.setEnabled(False)
                self.radiokatraj.setEnabled(False)
            

    def radioSayyed1(self,selected):
        if selected:
            with open('placename.txt','w') as myFile:
                myFile.write('Sayyed Nagar')

    def radioSheval1(self,selected):
        if selected:
            with open('placename.txt','w') as myFile:
                myFile.write('Shewalvadi')

    def radiokatraj1(self,selected):
        if selected:
            with open('placename.txt','w') as myFile:
                myFile.write('Katraj')


    def setupUi(self, MainWindow):

        MainWindow.setFixedSize(640,480)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('Images/icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Wallpaper Label
        self.Dlabel = QtWidgets.QLabel(self.centralwidget)
        self.Dlabel.setGeometry(QtCore.QRect(0, 2, 331, 475))
        pixmap = QPixmap('Images/my.jpg')
        self.Dlabel.setPixmap(pixmap)
        self.Dlabel.setObjectName("Dlabel")
        

        #username textbox
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 150, 181, 41))
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)

        #password textbox
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 250, 181, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)

        #Login label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #username label 
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        #password label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        #Placename radioBox
        self.radioSayyed = QtWidgets.QRadioButton(self.centralwidget)
        self.radioSayyed.setGeometry(370,320,91,20)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.radioSayyed.setFont(font)
        self.radioSayyed.setObjectName("radioSayyed")
        self.radioSayyed.toggled.connect(self.radioSayyed1)

        #Placename radioBox
        self.radioSheval = QtWidgets.QRadioButton(self.centralwidget)
        self.radioSheval.setGeometry(470,320,91,20)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.radioSheval.setFont(font)
        self.radioSheval.setObjectName("radioSheval")
        self.radioSheval.toggled.connect(self.radioSheval1)

        #Placename radioBox
        self.radiokatraj = QtWidgets.QRadioButton(self.centralwidget)
        self.radiokatraj.setGeometry(560,320,91,20)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.radiokatraj.setFont(font)
        self.radiokatraj.setObjectName("radiokatraj")
        self.radiokatraj.toggled.connect(self.radiokatraj1)
        
        #login Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 360, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.gotomain)
        
        self.checkRadio()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Elite SMS"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Username :"))
        self.label_3.setText(_translate("MainWindow", "Password :"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.radioSayyed.setText(_translate("MainWindow","Sayyed Nagar"))
        self.radioSheval.setText(_translate("MainWindow","Shewalvadi"))
        self.radiokatraj.setText(_translate("MainWindow","Katraj"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
