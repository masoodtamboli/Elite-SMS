from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import date
from datetime import timedelta
import datetime
import csv
from threading import Thread
import sys
from time import sleep
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import psycopg2

class Ui_MainWindow1(object):
    #This is MainThread Method
    def meth_main(self):
        self.vehicleNum = (self.bike_num_LE.text().upper())
        self.mobileNum = (self.mob_num_LE.text())
        self.expiryDate = (self.dateEdit.text())
        inputDate = datetime.datetime.strptime(self.expiryDate,'%Y-%m-%d') #To subtract one day from PUCC expiry date
        self.myNewExpiryDate = inputDate - timedelta(days=1)
        self.myNewExpiryDate = str(self.myNewExpiryDate).strip(':00')
        
        #Shows Message Box for confirmation of Data to send
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Is this Information Correct?')
        msg.setInformativeText('Vehicle Number : {VNum} \nMobile Number : {MNum} \nExpiry Date : {EDate} \nMessage Sending Date : {mDate}'.format(VNum = self.vehicleNum, MNum = self.mobileNum, EDate = self.expiryDate, mDate = self.myNewExpiryDate))
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonYes = msg.button(QMessageBox.Yes)
        retval = msg.exec_()
        if msg.clickedButton() == buttonYes:
            t1 = Thread(target = self.getData).start()
    

    # Save data to CSV
    def getData(self):  
        inputDate = datetime.datetime.strptime(self.expiryDate,'%Y-%m-%d') #To subtract one day from PUCC expiry date
        self.newExpiryDate = inputDate - timedelta(days=1)
        self.newExpiryDate = str(self.newExpiryDate).strip(':00')
        try:
            with open('userdata.csv','a',newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([self.vehicleNum, self.mobileNum, self.newExpiryDate])

        except Exception as e:
            pass
        
        self.bike_num_LE.setText('')
        self.mob_num_LE.setText('')


    # this method sends sms to customer
    def sendMessage(self):
        try:
            with open('placename.txt') as txtfile:
                myAddr = txtfile.readlines()
                myAddr = myAddr[0].lower()
        except:
            pass


        if 'shewalvadi' in myAddr:
            myAddressM1 = 'शिवाजी सर्विस स्टेशन (शेवाळवाडी भाजी मार्केट च्या बाजूस)'
            myAddressE1 = 'Shivaji Service Station (Shewalvadi beside Vege. Mkt.)'
            
            try:
                with open('userdata.csv') as csvFile:
                    result = csv.reader(csvFile)
                    for row in result:
                        user_mob = row[1]          
                        dateTemp = row[2].strip(' ')
                        myDate = date.today().strftime('%Y-%m-%d')
                        if dateTemp == myDate:
                            try:
                                myMessage = "आपल्या गाडी क्रमांक {} ची PUC उद्या संपणार आहे. आपण {} येथे येऊन PUC काढून १०००रू दंड वाचवावे.\nYour Vehicle {} PUC is expiring tomorrow kindly visit {} to renew it.\n-Faruk Tamboli (Noman PUC Center)".format(row[0],myAddressM1,row[0],myAddressE1)
                                
                                url = "https://www.fast2sms.com/dev/bulk"
                                querystring = {"authorization":"tLX5WAPeG7XDm4ny6VVA4ZTG4MI45WT02jqzECKeaHY0a11E4r5qcZITPgi5","sender_id":"SSSPUC","message":myMessage,"language":"unicode","route":"p","numbers":user_mob}
                                headers = {
                                    'cache-control': "no-cache"
                                }
                                response = requests.request("GET", url, headers=headers, params=querystring)
                            except Exception as e:
                                pass
            except Exception as e:
            	pass

        elif 'sayyed' in myAddr:
            myAddressM2 = 'मगर फ्युएल स्टेशन (सैय्यद नगर, रेल्वे फाटक)'
            myAddressE2 = 'Magar Fuel Station (Sayyed Nagar, Railway Phatak)'
            
            try:
                with open('userdata.csv') as csvFile:
                    result = csv.reader(csvFile)
                    for row in result:
                        user_mob = row[1]          
                        dateTemp = row[2].strip(' ')
                        myDate = date.today().strftime('%Y-%m-%d')
                        if dateTemp == myDate:
                            try:
                                myMessage = "आपल्या गाडी क्रमांक {} ची PUC उद्या संपणार आहे. आपण {} येथे येऊन PUC काढून १०००रू दंड वाचवावे.\nYour Vehicle {} PUC is expiring tomorrow kindly visit {} to renew it.\n-Faruk Tamboli (Magar PUC Center)".format(row[0],myAddressM2,row[0],myAddressE2)
                                
                                url = "https://www.fast2sms.com/dev/bulk"
                                querystring = {"authorization":"tLX5WAPeG7XDm4ny6VVA4ZTG4MI45WT02jqzECKeaHY0a11E4r5qcZITPgi5","sender_id":"MFSPUC","message":myMessage,"language":"unicode","route":"p","numbers":user_mob}
                                headers = {
                                    'cache-control': "no-cache"
                                }
                                response = requests.request("GET", url, headers=headers, params=querystring)
                            except :
                                pass
            except Exception as e:
                pass


        elif 'katraj' in myAddr:
            self.myAddressM = 'कात्रज -शहीद कर्नल प्रकाश पाटील पेट्रोलियम (अंबेगांव, बुद्रुक, देहु-कात्रज बाईपास रोड, पुणे)'
            
            try:
                 with open('userdata.csv') as csvFile:
                    result = csv.reader(csvFile)
                    for row in result: 
                        user_mob = row[1]          
                        dateTemp = row[2].strip(' ')
                        myDate = date.today().strftime('%Y-%m-%d')
                        if dateTemp == myDate:
                            try:
                                myMessage = "आपल्या गाडी क्रमांक {} ची PUC उद्या संपणार आहे. आपण {} येथे येऊन PUC काढून १०००रू दंड वाचवावे.\n -फारूक तांबोळी\n-(सनराइज PUC सेंटर)".format(row[0],self.myAddressM)
                                
                                url = "https://www.fast2sms.com/dev/bulk"
                                querystring = {"authorization":"tLX5WAPeG7XDm4ny6VVA4ZTG4MI45WT02jqzECKeaHY0a11E4r5qcZITPgi5","sender_id":"SPPPUC","message":myMessage,"language":"unicode","route":"p","numbers":user_mob}
                                headers = {
                                    'cache-control': "no-cache"
                                }
                                response = requests.request("GET", url, headers=headers, params=querystring)
                            except Exception as e :
                                pass
            except:
                pass
        else:
            pass
        


    #when RadioButton's state is changed expiry date will be automatically calculated
    def changeDate(self):
        self.todayDate = date.today()
        
        if self.sixMonthRbt.isChecked()==True:
            self.newdate = self.todayDate + timedelta(days=182)
            self.dateEdit.setDate(self.newdate)
        else:
            self.newdate = self.todayDate + timedelta(days=364)
            self.dateEdit.setDate(self.newdate)


    #This Method Backups the userdata to Gmail
    def backUpData(self):
        fromaddr = 'thepucpunetest@gmail.com'
        toaddr = 'faruktamboli01@gmail.com'
        myPlace = ''
        try:
            with open('placename.txt','r') as myfile:
                myPlace = myfile.readlines()
        except:
            pass
        
        try:
            with open('userdata.csv') as csvFile:
                result = csv.reader(csvFile)
        except:
            pass

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['to'] = toaddr
        msg['Subject'] = "Todays Data Backup from"+str(myPlace)
        body = 'Todays Data Backup from '+ myPlace[0] + '\n Date: '+ str(date.today())

        msg.attach(MIMEText(body,'plain'))

        filename = 'userdata.csv'
        with open(filename,'r') as f: 
            attachment = MIMEText(f.read())

        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)
        try:
            server = smtplib.SMTP(host='smtp.gmail.com', port=587)
            server.starttls()
            server.login(fromaddr,'PUC@1234')
            text = msg.as_string()
            server.sendmail(fromaddr,toaddr,text)
            server.quit()
        except :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Connection Error!')
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()


    #Ui Method
    def setupUi(self, MainWindow):

        #Thread to Send Messages
        Thread(target=self.sendMessage).start()

        with open('placename.txt','r') as txtfile:
            mydata = txtfile.readlines()
            if 'sayyed' in mydata:
            	self.PUC = 'Magar PUC Center, Pune'
            elif 'katraj' in mydata:
                self.PUC = 'Sunrise PUC Center, Pune'
            else:
                self.PUC = 'Noman PUC Center, Pune' 

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('Images/icon.jpg'))
        MainWindow.resize(614,400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Design Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 614, 71))
        self.label.setStyleSheet("background-color: rgb(146,43,33); color: rgb(255,255,255)")
        font = QtGui.QFont('Aharoni')
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 71, 614, 21))
        self.label1.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255,255,255)")
        font = QtGui.QFont('Helvetica',10)
        font.setPointSize(9)
        font.setWeight(10)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignBottom)
        self.label1.setObjectName("label1")

        #Vehicle number Label
        self.bike_no_label = QtWidgets.QLabel(self.centralwidget)
        self.bike_no_label.setGeometry(QtCore.QRect(140, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bike_no_label.setFont(font)
        self.bike_no_label.setObjectName("bike_no_label")

        #vehicle number edit Text
        self.bike_num_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.bike_num_LE.setGeometry(QtCore.QRect(270, 120, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bike_num_LE.setFont(font)
        
        #Mobile Number Label
        self.mob_num_label = QtWidgets.QLabel(self.centralwidget)
        self.mob_num_label.setGeometry(QtCore.QRect(145, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mob_num_label.setFont(font)
        self.mob_num_label.setObjectName("mob_num_label")

        #Mobile Number Edit Text
        self.mob_num_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.mob_num_LE.setGeometry(QtCore.QRect(270, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mob_num_LE.setFont(font)
        self.mob_num_LE.setObjectName("mob_num_LE")

        #Date of Expiry Label
        self.epiry_label = QtWidgets.QLabel(self.centralwidget)
        self.epiry_label.setGeometry(QtCore.QRect(130, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.epiry_label.setFont(font)
        self.epiry_label.setObjectName("epiry_label")

        #Date Edit
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(270, 240, 181, 31))
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.dateEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")

        #Months Label
        self.monthsLabel = QtWidgets.QLabel(self.centralwidget)
        self.monthsLabel.setGeometry(QtCore.QRect(115, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.monthsLabel.setFont(font)
        self.monthsLabel.setObjectName("monthsLabel")

        #Radio Buttons fro Months
        self.sixMonthRbt = QtWidgets.QRadioButton(self.centralwidget)
        self.sixMonthRbt.setGeometry(QtCore.QRect(275, 300, 82, 17))
        self.sixMonthRbt.setObjectName("sixMonthRbt")
        self.sixMonthRbt.toggled.connect(self.changeDate)
        
        self.twelveMonthRbt = QtWidgets.QRadioButton(self.centralwidget)
        self.twelveMonthRbt.setGeometry(QtCore.QRect(360, 300, 82, 17))
        self.twelveMonthRbt.setObjectName("twelveMonthRbt")
        self.twelveMonthRbt.toggled.connect(self.changeDate)

        #Submit Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 340, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.meth_main)

        #Backup Button
        self.backUpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backUpBtn.setGeometry(QtCore.QRect(20, 100, 50, 40))
        self.backUpBtn.setObjectName("pushButton")
        self.backUpBtn.clicked.connect(self.backUpData)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Elite SMS"))
        self.label.setText(_translate("MainWindow",self.PUC))
        self.label1.setText(_translate("MainWindow",'                                                                      Designed and Developed By : INFORMATICS IT SOLUTIONS   '))
        self.bike_no_label.setText(_translate("MainWindow", "Vehicle Number :"))
        self.bike_num_LE.setPlaceholderText(_translate("MainWindow", "MH12CP9656"))
        self.mob_num_label.setText(_translate("MainWindow", "Mobile Number :"))
        self.mob_num_LE.setPlaceholderText(_translate("MainWindow", "9689562665"))
        self.epiry_label.setText(_translate("MainWindow", "PUCC Expiry Date :"))
        self.monthsLabel.setText(_translate("MainWindow","Expiry Date Validity :"))
        self.sixMonthRbt.setText(_translate("MainWindow", "6 Months"))
        self.twelveMonthRbt.setText(_translate("MainWindow", "12 Months"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.backUpBtn.setText(_translate("MainWindow","Backup"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
