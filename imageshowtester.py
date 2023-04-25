

import socket
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QHeaderView, QLabel 

from PyQt5.QtGui import QPixmap
import json


class Ui_MainWindow(object):
                             # this will be either "E" for edit or "A" for add
    # detailBoxStartingX=int(screenwidth*0.19)
    def setupSunGalLogo(self):
        
        imageName = './designImages/logo.png'
        self.pixmap = QPixmap(imageName).scaledToHeight(400).scaledToWidth(400)
        self.logoImage.setPixmap(self.pixmap)
        self.logoImage.resize(self.pixmap.height(),self.pixmap.width())
        # self.logoImage.setText("ANY")
        
    def setupUi(self, MainWindow):
    
        MainWindow.setObjectName("MainWindow")
        self.setupUILayout(MainWindow)  
        self.setupSunGalLogo()
        self.retranslateUi(MainWindow)
        # our startup defs and vars
        # startup initialization
       
    def retranslateUi(self, MainWindow):
        self.doRetranslate(MainWindow)

    def exitApp(self):
        sys.exit("Thankyou for using this utility. Goodbye For Now")  

    def setupUILayout(self,MainWindow):
        self.screenbaseheight = 1200    #this is immutable
		# self.screenheight = 1800   							#self.screenRect.height()
        self.screenwidth  = 2500   							#self.screenRect.width()
        print("self.screenwidth=",self.screenwidth)
		# print("self.screenheight=",self.screenheight)
		##########################################################################
		#  variables to consolidate standard widths, heights and grid coordinates
		##########################################################################
        self.detailBoxStartingX=int(self.screenwidth*0.19)
        self.detailBoxWidth = int(self.screenwidth*0.23)
        self.firstDetailColumnX = int(self.screenwidth*0.010)

        self.leftmostX = int(self.screenwidth*0.030)
        self.addButtonX = int(self.screenwidth*0.389)
        self.cancelButtonX = int(self.screenwidth*0.038)
        self.controlBottomMargin = int(self.screenbaseheight*.006)
        self.controlHeight1 = int(self.screenwidth*0.008)
        self.controlHeight2 = int(self.screenwidth*0.015)

        self.buttonwidth1 = int(self.screenwidth*0.026)
        self.buttonheight1 = int(self.screenbaseheight*0.019)

        self.buttonwidth2 = int(self.screenwidth*0.01)


        self.inputFieldWidth1 =    int(self.screenwidth*0.015)
        self.inputFieldWidth2 =    int(self.screenwidth*0.020) 
        self.noeditDisplayField1 = int(self.screenwidth*0.070)

        self.batchDetailRow1 = int(self.screenbaseheight*0.15)


        self.batchEditRow1 = int(self.screenbaseheight*0.020)
        self.batchEditRow2 = (self.batchEditRow1 + self.controlHeight1) + self.controlBottomMargin
        self.batchEditRow3 = (self.batchEditRow2 + self.controlHeight2) + self.controlBottomMargin
		
        self.devicetypeEditRow1 = int(self.screenbaseheight*0.02)

		# END OF  variables to consolidate standard widths, heights and grid coordinates

        MainWindow.resize(int(self.screenwidth*0.45), int(self.screenbaseheight*0.635))
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_refreshing = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refreshing.setObjectName("pushButton_refreshing")
        self.pushButton_refreshing.setStyleSheet('QPushButton {background-color: #A3C1DA; color: green;}')

        # put logo display here
        self.logoImage = QtWidgets.QLabel(self.centralwidget)
        # self.logoImage.setGeometry(QtCore.QRect(int(self.screenwidth *.8), int(self.screenbaseheight*.03), int(self.screenwidth*0.3), int(self.screenbaseheight*0.3)))
        self.logoImage.setObjectName("logoImage")

		##############################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1452, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def doRetranslate(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sungal's LIVING POG Track Burner Utility"))
        # self.logoImage.setText(_translate("MainWindow", "TEMP"))


if __name__ == "__main__":
    import sys
 
    app = QtWidgets.QApplication(sys.argv)
    # Open the style sheet file and read it
    with open('style.qss', 'r') as f:
        style = f.read()
    # Set the current style sheet
    app.setStyleSheet(style)
    app.setStyle('Windows')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    