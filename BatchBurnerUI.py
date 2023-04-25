# -*- coding: utf-8 -*-batchLineEditBox
# Written by Keqin Chen and Dan Rothman for:
# Sungal Corportion's G6 Living POG

# Created using  PyQt5 UI code generator 5.15.4
#
# This uitility is written to burn batch number and Serial number 
# to Sungal G6 tracks from manufacture
# and to manage batch and devicetype record keeping for newly manufactured tracks

# every manufactured track is a member of a batch, which is a group of tracks with 
# 1. the same manufacture date
# 2. the same device type (model)
# 3. manufactured in the same factory

# The device type of a batch (#2) is known through the batch's devicetypeID, which 
# links it to the device type's record. In this way, each track can be linked to a 
# device type so that a process can know the atrributes and dimensions of the track


#  General  functions of batch burn utility

# 1. get IP and port of (motherboard) shelf from user.
# 2. get response from TCPIP socket
# 3. get batch number from user. Allow user to edit  batch data
# 4. allow user to edit devicetype data if necessary
# 5. generate serial number using the batch number
# 6. allow user to burn batch number and serial number to  firmware memory of  the track
# 6. allow user to save changes to central database


import socket
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QLabel 

from PyQt5.QtGui import QPixmap
import json
from configparser import ConfigParser
from SocketDefs import *   # getTracks,burnBatchesAndSerialNumbers
from DBUtils import getDictionary, updateDatabaseTable,getBatches
from UIGraphics import setupUILayout, doRetranslate
from datetime import date
from MessageBoxes import *  

# Global vars
configFilePath = r'config.ini'  #ini file path
cfg = ConfigParser()
cfg.read(configFilePath)
apiServer = cfg.get('URLs', 'apiServer')
editInputPrefix = "lineEdit_"
successfulUpdateCode = '<Response [200]>'


class Ui_MainWindow(object):

    IPADDR = ''                  #'69.122.14.38'
    PORT = 0                     # 63003
    NUM_PNP_SOCKETS = 0          #24
    FIRST_SOCKET_ADDRESS = 0     #49
    BATCH_NUMBER = 6
    MY_SOCKET = socket.socket()

    BATCHID_COLUMN = 0
    DEVICETYPEID_COLUMN = 2

    selectedDeviceTypeID = 0
    selectedBatchID = 0
    selected_DEVICETYPE_Rec  = {}
    selected_BATCH_Rec = {}
    batchFieldsList = []
    devicetypeFieldsList = []    
    defaultAddValues = {}
    changeMode = "E"                                # this will be either "E" for edit or "A" for add
    # detailBoxStartingX=int(screenwidth*0.19)
    def setupSunGalLogo(self):
        
        imageName = './designImages/logo.png'
        self.pixmap = QPixmap(imageName).scaledToHeight(100).scaledToWidth(100)
        self.logoImage.setPixmap(self.pixmap)
        self.logoImage.resize(self.pixmap.height(),self.pixmap.width())
        # self.logoImage.setText("ANY")
        
    def setupUi(self, MainWindow):
    
        MainWindow.setObjectName("MainWindow")
        setupUILayout(self,MainWindow)  
        self.setupSunGalLogo()
        self.retranslateUi(MainWindow)
        # our startup defs and vars
        # startup initialization
        self.batchFieldsList=[self.lineEdit_BATCH_batchID,
                              self.lineEdit_BATCH_factoryID,
                              self.lineEdit_BATCH_deviceTypeID,
                              self.lineEdit_BATCH_mfDateMonth,
                              self.lineEdit_BATCH_mfDateDay,
                              self.lineEdit_BATCH_mfDateYear]

        self.devicetypeFieldsList =[self.lineEdit_DEVICETYPE_deviceTypeName,
                                    self.lineEdit_DEVICETYPE_deviceTypeID,
                                    self.lineEdit_DEVICETYPE_numberOfSensors,
                                    self.lineEdit_DEVICETYPE_dimension,
                                    self.lineEdit_DEVICETYPE_startingSensor,
                                    self.lineEdit_DEVICETYPE_sensor1Distance,
                                    self.lineEdit_DEVICETYPE_sensor2Distance,
                                    self.lineEdit_DEVICETYPE_sensorSpacing,
                                    self.lineEdit_DEVICETYPE_frontGap,
                                    self.lineEdit_DEVICETYPE_reverseOrder,
                                    self.lineEdit_DEVICETYPE_trackWidth]

        
        #when we add a new batch or devicetype record, these fields get a default value
        
        self.defaultAddValues = {
                            'BATCH'       : [   {'inputField' : self.lineEdit_BATCH_mfDateMonth,  'defaultValue' : date.today().month},
                                                {'inputField' : self.lineEdit_BATCH_mfDateDay,    'defaultValue' : date.today().day  },
                                                {'inputField' : self.lineEdit_BATCH_mfDateYear,   'defaultValue' : date.today().year },
                                                {'inputField' : self.lineEdit_BATCH_batchID,      'defaultValue' : 0                 }
                                            ],
                            'DEVICETYPE'  : [
                                                {'inputField' :self.lineEdit_DEVICETYPE_deviceTypeID, 'defaultValue' :0}
                                            ]           
                            }   
        
        # run startup processes
        self.refreshData()
        # set selection to last batch in batches table. Execute selectBatchRow() to get all the screen controls set and populated correctly
        self.tableWidget.selectRow(self.tableWidget.rowCount()-1)
        self.selectBatchRow(self.tableWidget.rowCount()-1)
        # self.fillFields("DEVICETYPE",self.devicetypeFieldsList)
        self.resetDevicetypeEditMode()
        self.resetBatchEditMode()
        self.resetDevicetypeEditMode()
    
    def refreshData(self):
        self.showBatchTable()
        self.batchDictionary = getDictionary(apiServer,"batches","batchID")
        self.devicetypeDictionary = getDictionary(apiServer,"devicetypes","deviceTypeID")
        self.factoryDictionary = getDictionary(apiServer,"factorys","factoryID")
    
    def showBatchTable(self):

        batchList = getBatches(apiServer,"DISPLAY")        
        self.tableWidget.setRowCount(len(batchList))
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        table_header = []
        didHeaderFill = False
        row = 0
        col = 0
        for batch in batchList:
            self.tableWidget.setColumnCount(len(batch))
            for attribute, value in batch.items():
                if didHeaderFill == False:
                    table_header.append(attribute) 
            self.tableWidget.setHorizontalHeaderLabels(table_header)
            didHeaderFill = True

            for attribute, value in batch.items():
                self.tableWidget.setItem(row,col, QtWidgets.QTableWidgetItem(str(value)))
                col += 1
        row += 1

        self.tableWidget.horizontalHeader().resizeSections
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    def selectBatchRow(self,row):
        # global  vars for batchID selected in table and devicetype linked to batch  with
        # the selected batchID
        self.selectedDeviceTypeID = self.tableWidget.item(row,self.DEVICETYPEID_COLUMN).text()
        self.selectedBatchID = self.tableWidget.item(row,self.BATCHID_COLUMN).text()
        self.selected_DEVICETYPE_Rec = self.devicetypeDictionary[str(self.selectedDeviceTypeID)]
        self.selected_BATCH_Rec = self.batchDictionary[str(self.selectedBatchID)]
        
        # print("self.selectedDeviceTypeID =", self.selectedDeviceTypeID,"self.selected_DEVICETYPE_Rec=",self.selected_DEVICETYPE_Rec)
        # print("self.selectedBatchID =", self.selectedBatchID,"self.selected_BATCH_Rec=",self.selected_BATCH_Rec)
        
        # code for selection/deselection color

        # this takes care of "whiting out" unselected rows
        for row2 in range(self.tableWidget.rowCount()):
                for col2 in range(self.tableWidget.columnCount()):
                    # print("IN THE SELECT BATCH ROW 1st loop")
                    self.tableWidget.item(row2,col2).setBackground(QtGui.QColor(255,255,255))

        for col in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row,col).setBackground(QtGui.QColor(170,170,170))
            # print("IN THE SELECT BATCH ROW 2nd loop")
            
        # end of code to take care of selection/deselection color
        #

        # fill the dislay fields to the right of the table with data from selected 
        # batch and the devicetype of the batch
        self.fillFields("BATCH", self.batchFieldsList)
        self.fillFields("DEVICETYPE", self.devicetypeFieldsList)
        self.resetBatchEditMode()
        self.resetDevicetypeEditMode()
        # print("IN THE SELECT BATCH ROW - Down to the end")
        return                             

    # defs for edits/adds/saves for both tables (batches, devicetypes)

    def editBatch(self):
       self.setBatchEditMode()
    
    def editDevicetype(self):
        self.setDevicetypeEditMode()
 
    def setBatchAddMode(self):   #s.b.setBatchAddMode
        self.setBatchEditMode()       
        self.setAddMode("BATCH") #s.b. setAddMode
        self.changeMode = "A"
        
    def setDevicetypeAddMode(self): #s.b.setDevicetypeAddMode
        self.setDevicetypeEditMode()
        self.setAddMode("DEVICETYPE")  #s.b. setAddMode
        self.changeMode = "A"

    def setBatchEditMode(self):
        self.changeMode = "E"
        return self.setEditFields("batch","ON")

    def resetBatchEditMode(self):
        return self.setEditFields("batch","OFF")

    def setDevicetypeEditMode(self):
        self.changeMode = "E"
        return self.setEditFields("devicetype","ON")
 
    def resetDevicetypeEditMode(self):
        return self.setEditFields("devicetype","OFF")
    
    def saveBatchEdit(self):
        self.resetBatchEditMode()
        return self.saveEdit("BATCH","batchID")

    def saveDevicetypeEdit(self):
        self.resetDevicetypeEditMode()
        return self.saveEdit("DEVICETYPE","deviceTypeID") 

    def cancelBatchEdit(self):        
        self.fillFields("BATCH",self.batchFieldsList)
        self.resetBatchEditMode()

    def cancelDevicetypeEdit(self):
        self.fillFields("DEVICETYPE",self.devicetypeFieldsList)
        self.resetDevicetypeEditMode()


    # generic functions for both batch and devicetypes
    # enables/disables inputfields and buttons for edit and add operations
    def setAddMode(self,mode):   #s.b. setAddMode
        # default field values for adding either a batch or devicetype record get displayed and contained in the screen's input/display field  
        for valuePair in self.defaultAddValues[mode.upper()]:
            inputField = valuePair['inputField']
            inputField.clear()
            inputField.insert(str(valuePair['defaultValue']))

        # changeMode = "A"  # for ADD operation

    def getFieldnameFromInputfield(self,inputField,mode):
        startPos = len(editInputPrefix.strip() + mode.upper().strip()+"_")
        return inputField.objectName()[startPos:100]

    def fillFields(self, mode, fieldList):
        mCurrRec = {}
        if mode.upper()=="BATCH":
            mCurrRec = self.selected_BATCH_Rec
            self.label_FACTORYNAME.setText( self.factoryDictionary[str(mCurrRec["factoryID"])]["factoryName"])
            print("mCurrRec[deviceTypeID]=",mCurrRec["deviceTypeID"])
            # print("self.devicetypeDictionary=",self.devicetypeDictionary)
            # print("self.devicetypeDictionary[str(mCurrRec[deviceTypeID])][deviceTypeName]=",self.devicetypeDictionary[str(mCurrRec['deviceTypeID'])]['deviceTypeName'])
            self.label_BATCH_DEVICETYPENAME.setText( self.devicetypeDictionary[str(mCurrRec["deviceTypeID"])]["deviceTypeName"])
        
        if mode.upper()=="DEVICETYPE":
            mCurrRec = self.selected_DEVICETYPE_Rec

        for field in fieldList:
            dictLookupName = self.getFieldnameFromInputfield(field,mode)
            field.clear()
            field.insert(str(mCurrRec[dictLookupName]))
            # background =  transparent
            field.setStyleSheet("QLineEdit"
                                "{"
                                "background : transparent;"
                                "}")
            field.setReadOnly(True)            
        
 
    def setEditFields(self,mode,onoff):
       
        isOn = onoff.upper()=="ON"
        selectedFieldList=[]
        keyField=""
        if mode.upper()=="BATCH":
            # enable/disable buttons appropriately for the operation
            selectedFieldList = self.batchFieldsList
            self.pushButton_SAVEBATCHCHANGE.setDisabled(not isOn)    
            self.pushButton_CANCELBATCHCHANGE.setDisabled(not isOn)
            self.pushButton_ADDBATCH.setDisabled(isOn)
            self.pushButton_EDITBATCH.setDisabled(isOn)
            keyField="batchID"

        if mode.upper()=="DEVICETYPE":
            #  enable/disable buttons appropriately for the operation
            selectedFieldList = self.devicetypeFieldsList
            self.pushButton_SAVEDEVICETYPECHANGE.setDisabled(not isOn)    
            self.pushButton_CANCELDEVICETYPECHANGE.setDisabled(not isOn)
            self.pushButton_ADDDEVICETYPE.setDisabled(isOn)
            self.pushButton_EDITDEVICETYPE.setDisabled(isOn)
            keyField="deviceTypeID"

        for field in [inputField for inputField in selectedFieldList if self.getFieldnameFromInputfield(inputField,mode)!= keyField]:
            
            field.setReadOnly(not isOn)
            if isOn:
                field.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;" 
                                "}")
            else:
                field.setStyleSheet("QLineEdit"
                                "{"
                                "background : transparent;" 
                                "}")
   
    def saveEdit(self, mode, keyField):
        # this saves both edits and adds

        inputFieldsList = []
        tableName = ""
        if mode.upper() == "BATCH":
            inputFieldsList = self.batchFieldsList
            tableName = "batches"
        if mode.upper() == "DEVICETYPE":
            inputFieldsList = self.devicetypeFieldsList
            tableName = "devicetypes"

        fieldnameList = [self.getFieldnameFromInputfield(inputField,mode) for inputField in inputFieldsList 
                                                        if self.getFieldnameFromInputfield(inputField,mode)!= keyField]

        valueList = [inputField.text() for inputField in inputFieldsList 
                                                        if self.getFieldnameFromInputfield(inputField,mode)!= keyField]
        selectedID = 0
        if mode.upper() == "BATCH":
            selectedID = self.selectedBatchID  
        if mode.upper() == "DEVICETYPE":
            selectedID = self.selectedDeviceTypeID
        # print ("What is changeMode ? ",self.changeMode)
        result = updateDatabaseTable(apiServer,tableName,fieldnameList,valueList,self.changeMode,keyField + "=" + str(selectedID))

        if str(result).strip()==successfulUpdateCode:
            self.refreshData() 
        return str(result).strip()    
            

    # END OF generic functions for both batch and devicetypes which
    # enable/disable inputfields and buttons for edit and add operations

    def connectShelf(self):
        try: 
            self.IPADDR = self.lineEdit_IPADDR.text()
            self.PORT = int(self.lineEdit_PORT.text())
            self.NUM_PNP_SOCKETS = int(self.lineEdit_numSockets.text())
            self.FIRST_SOCKET_ADDRESS = int(self.lineEdit_STARTSOCKET.text())
            print(self.IPADDR,self.PORT,self.NUM_PNP_SOCKETS,self.FIRST_SOCKET_ADDRESS)
           
            self.MY_SOCKET.settimeout(2)
            self.MY_SOCKET.connect((self.IPADDR,self.PORT))
            self.label_shelfConnectNotice.setText('CONNECTED')
            self.label_shelfConnectNotice.setStyleSheet("QLabel { color : green;}")
        except:
            self.label_shelfConnectNotice.setText('CONNECTION FAIL')
            self.label_shelfConnectNotice.setStyleSheet("QLabel { color : red;}")

    def burnBatch(self):

        try:
            powerShelf(self,"ON",self.lineEdit_IPADDR.text(),int(self.lineEdit_PORT.text()))        
            self.connectShelf()
        except TimeoutError:
            showDialog("INFO","CONNECTION TO SHELF HAS NOT BEEN ESTABLISHED, SOCKET HAS TIMED OUT","FAILURE TO BURN TRACKS")
            return False
        except:
            showDialog("INFO","CONNECTION TO SHELF HAS NOT BEEN ESTABLISHED, ENTER IP ADDR, PORT, # OF SOCKETS AND STARTING SOCKET # OR CONTACT TECHNICIAN IF PROBLEM PERSISTS","FAILURE TO BURN TRACKS")
            return  False
    
        burnBatchesAndSerialNumbers(self.NUM_PNP_SOCKETS,self.FIRST_SOCKET_ADDRESS,self.selectedBatchID,self.MY_SOCKET)
        powerShelf(self,"OFF",self.lineEdit_IPADDR.text(),int(self.lineEdit_PORT.text()))
        self.MY_SOCKET.close()
        self.MY_SOCKET = socket.socket()
        # getTracks(self.IPADDR,self.PORT,self.NUM_PNP_SOCKETS,self.FIRST_SOCKET_ADDRESS,self.BATCH_NUMBER,self.MY_SOCKET)
        return True
        
    def retranslateUi(self, MainWindow):
        doRetranslate(self,MainWindow)

    def exitApp(self):
        sys.exit("Thankyou for using this utility. Goodbye For Now")  

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