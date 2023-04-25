# -*- coding: utf-8 -*-batchLineEditBox
# Written by Keqin Chen and Dan Rothman for:
# Sungal Corportion's G6 Living POG

# Created using  PyQt5 UI code generator 5.15.4

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView

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
    
		self.groupBox_ConnectShelf = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_ConnectShelf.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.03), int(self.screenwidth*0.28), int(self.screenbaseheight*0.07)))
		self.groupBox_ConnectShelf.setObjectName("groupBox_ConnectShelf")

		self.label_IPADDR = QtWidgets.QLabel(self.groupBox_ConnectShelf)
		self.label_IPADDR.setGeometry(QtCore.QRect(self.leftmostX, int(self.screenbaseheight*0.02), int(self.screenwidth*0.06), self.controlHeight1))
		self.label_IPADDR.setObjectName("label_IPADDR")
		self.lineEdit_IPADDR = QtWidgets.QLineEdit(self.groupBox_ConnectShelf)
		self.lineEdit_IPADDR.setGeometry(QtCore.QRect(int(self.screenwidth*0.015), int(self.screenbaseheight*0.04), int(self.screenwidth*0.08), self.controlHeight1))
		self.lineEdit_IPADDR.setObjectName("lineEdit_IPADDR")
          
		self.label_PORT = QtWidgets.QLabel(self.groupBox_ConnectShelf)
		self.label_PORT.setGeometry(QtCore.QRect(int(self.screenwidth*0.1), int(self.screenbaseheight*0.02), int(self.screenwidth*0.03), self.controlHeight1))
		self.label_PORT.setObjectName("label_PORT")
		self.lineEdit_PORT = QtWidgets.QLineEdit(self.groupBox_ConnectShelf)
		self.lineEdit_PORT.setGeometry(QtCore.QRect(int(self.screenwidth*0.1), int(self.screenbaseheight*0.04), int(self.screenwidth*0.04), self.controlHeight1))
		self.lineEdit_PORT.setObjectName("lineEdit_PORT")

		self.label_numSockets = QtWidgets.QLabel(self.groupBox_ConnectShelf)
		self.label_numSockets.setGeometry(QtCore.QRect(int(self.screenwidth*0.15), int(self.screenbaseheight*0.02), int(self.screenwidth*0.045), self.controlHeight1))
		self.label_numSockets.setObjectName("label_numSockets")
		self.lineEdit_numSockets = QtWidgets.QLineEdit(self.groupBox_ConnectShelf)
		self.lineEdit_numSockets.setGeometry(QtCore.QRect(int(self.screenwidth*0.15), int(self.screenbaseheight*0.04), int(self.screenwidth*0.04), self.controlHeight1))
		self.lineEdit_numSockets.setObjectName("lineEdit_numSockets")

		self.label_STARTSOCKET = QtWidgets.QLabel(self.groupBox_ConnectShelf)
		self.label_STARTSOCKET.setGeometry(QtCore.QRect(int(self.screenwidth*0.2), int(self.screenbaseheight*0.02), int(self.screenwidth*0.06), self.controlHeight1))
		self.label_STARTSOCKET.setObjectName("label_STARTSOCKET")
		self.lineEdit_STARTSOCKET = QtWidgets.QLineEdit(self.groupBox_ConnectShelf)
		self.lineEdit_STARTSOCKET.setGeometry(QtCore.QRect(int(self.screenwidth*0.2), int(self.screenbaseheight*0.04), int(self.screenwidth*0.06), self.controlHeight1))
		self.lineEdit_STARTSOCKET.setObjectName("lineEdit_STARTSOCKET")

		# self.pushButton_CONNECTSHELF = QtWidgets.QPushButton(self.groupBox_ConnectShelf,clicked = self.connectShelf)
		# self.pushButton_CONNECTSHELF.setGeometry(QtCore.QRect(int(self.screenwidth*0.27), int(self.screenbaseheight*0.04), int(self.screenwidth*0.05), self.controlHeight1))
		# self.pushButton_CONNECTSHELF.setObjectName("pushButton_CONNECTSHELF")

		self.label_shelfConnectNotice = QtWidgets.QLabel(self.groupBox_ConnectShelf)
		self.label_shelfConnectNotice.setGeometry(QtCore.QRect(int(self.screenwidth*0.33), int(self.screenbaseheight*0.04), int(self.screenwidth*0.08), self.controlHeight1))
		self.label_shelfConnectNotice.setObjectName("shelfConnectNotice")

		# put logo display here
		self.logoImage = QtWidgets.QLabel(self.centralwidget)
		self.logoImage.setGeometry(QtCore.QRect(int(self.screenwidth *.8), int(self.screenbaseheight*.03), int(self.screenwidth*0.15), int(self.screenbaseheight*0.15)))
		self.logoImage.setObjectName("logoImage")
		
		self.groupBox_BATCHEDITAREA = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_BATCHEDITAREA.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.11), int(self.screenwidth*0.43), int(self.screenbaseheight*0.5)))
		self.groupBox_BATCHEDITAREA.setObjectName("groupBox_BATCHEDITAREA")
		
		self.label_SELECTBATCH = QtWidgets.QLabel(self.groupBox_BATCHEDITAREA)
		self.label_SELECTBATCH.setGeometry(QtCore.QRect(self.leftmostX, int(self.screenbaseheight*0.15) , int(self.screenwidth*0.05), self.controlHeight1))
		self.label_SELECTBATCH.setObjectName("label_SELECTBATCH")
		# self.scrollArea = QtWidgets.QScrollArea(self.groupBox_BATCHEDITAREA)
		# self.scrollArea.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.04), int(self.screenwidth*0.2), int(self.screenbaseheight*0.408)))
		# self.scrollArea.setWidgetResizable(True)
		# self.scrollArea.setObjectName("scrollArea")
		# selbf.scrollAreaWidgetContents = QtWidgets.QWidget()
		# self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, int(self.screenwidth*0.2), int(self.screenbaseheight*0.408)))
		# self.scrollAreaWidgetContents.setObjectName(self.centralWidgets)
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(self.leftmostX, self.batchDetailRow1, int(self.screenwidth*0.16), int(self.screenbaseheight*0.408)))
		self.tableWidget.cellClicked.connect(self.selectBatchRow)

		# self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.pushButton_EDITBATCH = QtWidgets.QPushButton(self.groupBox_BATCHEDITAREA,clicked = self.editBatch)
		self.pushButton_EDITBATCH.setGeometry(QtCore.QRect(int(self.screenwidth*0.36), int(self.screenbaseheight*0.025), self.buttonwidth1, self.buttonheight1))
		self.pushButton_EDITBATCH.setObjectName("pushButton_EDITBATCH")
		self.pushButton_EDITBATCH.setDisabled(True)
		self.pushButton_ADDBATCH = QtWidgets.QPushButton(self.groupBox_BATCHEDITAREA,clicked = self.setBatchAddMode)
		self.pushButton_ADDBATCH.setGeometry(QtCore.QRect(self.addButtonX, int(self.screenbaseheight*0.025), self.buttonwidth2, self.buttonheight1))
		self.pushButton_ADDBATCH.setObjectName("pushButton_ADDBATCH")

		self.groupBox_BATCH = QtWidgets.QGroupBox(self.groupBox_BATCHEDITAREA)
		self.groupBox_BATCH.setGeometry(QtCore.QRect(self.detailBoxStartingX, int(self.screenbaseheight*0.035), self.detailBoxWidth, int(self.screenbaseheight*0.14)))
		self.groupBox_BATCH.setObjectName("groupBox_BATCH")

		#
		# these are the display/edit fields for the selected batch
		############################################################################

		#  
		#    BATCHID
		##############################################################
		self.label_BATCHID = QtWidgets.QLabel(self.groupBox_BATCH)
		self.label_BATCHID.setGeometry(QtCore.QRect(self.firstDetailColumnX, self.batchEditRow1, int(self.screenwidth*0.03), self.controlHeight1))
		self.label_BATCHID.setObjectName("label_BATCHID")

		self.lineEdit_BATCH_batchID = QtWidgets.QLineEdit(self.groupBox_BATCH)
		self.lineEdit_BATCH_batchID.setGeometry(QtCore.QRect(self.leftmostX, self.batchEditRow1, int(self.screenwidth*0.03), self.controlHeight1))
		self.lineEdit_BATCH_batchID.setObjectName("lineEdit_BATCH_batchID")
	#  
		#    FACTORYID
		##############################################################

		# row 1, batch edit box
		self.label_FACTORYID = QtWidgets.QLabel(self.groupBox_BATCH)
		self.label_FACTORYID.setGeometry(QtCore.QRect(int(self.screenwidth*0.060), self.batchEditRow1, int(self.screenwidth*0.045), self.controlHeight1))
		self.label_FACTORYID.setObjectName("label_FACTORYID")

		self.lineEdit_BATCH_factoryID = QtWidgets.QLineEdit(self.groupBox_BATCH)
		self.lineEdit_BATCH_factoryID.setGeometry(QtCore.QRect(int(self.screenwidth*0.090), self.batchEditRow1, self.inputFieldWidth2 , self.controlHeight1))
		self.lineEdit_BATCH_factoryID.setObjectName("lineEdit_BATCH_factoryID")

		self.label_FACTORYNAME = QtWidgets.QLabel(self.groupBox_BATCH)
		self.label_FACTORYNAME.setGeometry(QtCore.QRect(int(self.screenwidth*0.120), self.batchEditRow1, self.noeditDisplayField1, self.controlHeight1))
		self.label_FACTORYNAME.setObjectName("label_FACTORYNAME")
		#
		# end of row 1, batch edit box
		#

		# row 2, batch edit box
		self.label_BATCH_deviceTypeID = QtWidgets.QLabel(self.groupBox_BATCH)
		self.label_BATCH_deviceTypeID.setGeometry(QtCore.QRect(int(self.screenwidth*0.051), self.batchEditRow2, int(self.screenwidth*0.06), self.controlHeight1))
		self.label_BATCH_deviceTypeID.setObjectName("label_DEVICETYPE")

		self.lineEdit_BATCH_deviceTypeID = QtWidgets.QLineEdit(self.groupBox_BATCH)
		self.lineEdit_BATCH_deviceTypeID.setGeometry(QtCore.QRect(int(self.screenwidth*0.090),self.batchEditRow2 , self.inputFieldWidth2, self.controlHeight1))
		self.lineEdit_BATCH_deviceTypeID.setObjectName("lineEdit_BATCH_deviceTypeID")

		self.label_BATCH_DEVICETYPENAME = QtWidgets.QLabel(self.groupBox_BATCH)
		self.label_BATCH_DEVICETYPENAME.setGeometry(QtCore.QRect(int(self.screenwidth*0.120), self.batchEditRow2, self.noeditDisplayField1, self.controlHeight1))
		self.label_BATCH_DEVICETYPENAME.setObjectName("label_BATCH_DEVICETYPENAME")

		#
		# end of row 2, batch edit box
		#

		# row 3, mfDate
		self.label_MFDATEMONTH = QtWidgets.QLabel(self.groupBox_BATCH)

		self.label_MFDATEMONTH.setGeometry(QtCore.QRect(self.firstDetailColumnX, self.batchEditRow3, int(self.screenwidth*0.025), self.controlHeight1))
		self.label_MFDATEMONTH.setObjectName("label_MFMONTH")

		self.lineEdit_BATCH_mfDateMonth = QtWidgets.QLineEdit(self.groupBox_BATCH)
		self.lineEdit_BATCH_mfDateMonth.setGeometry(QtCore.QRect(int(self.screenwidth*0.042), self.batchEditRow3, self.inputFieldWidth1, self.controlHeight1))
		self.lineEdit_BATCH_mfDateMonth.setObjectName("lineEdit_BATCH_mfDateMonth")

		self.label_MFDATEDAY = QtWidgets.QLabel(self.groupBox_BATCH)
		self.label_MFDATEDAY.setGeometry(QtCore.QRect(int(self.screenwidth*0.065), self.batchEditRow3, int(self.screenwidth*0.045), self.controlHeight1))
		self.label_MFDATEDAY.setObjectName("label_MFDATEDAY")

		self.lineEdit_BATCH_mfDateDay = QtWidgets.QLineEdit(self.groupBox_BATCH)
		self.lineEdit_BATCH_mfDateDay.setGeometry(QtCore.QRect(int(self.screenwidth*0.095), self.batchEditRow3, self.inputFieldWidth1, self.controlHeight1))
		self.lineEdit_BATCH_mfDateDay.setObjectName("lineEdit_BATCH_mfDateDay")

		self.label_MFDATEYEAR = QtWidgets.QLabel(self.groupBox_BATCH)
		self.label_MFDATEYEAR.setGeometry(QtCore.QRect(int(self.screenwidth*0.12), self.batchEditRow3, int(self.screenwidth*0.045), self.controlHeight1))
		self.label_MFDATEYEAR.setObjectName("label_MFDATEYEAR")

		self.lineEdit_BATCH_mfDateYear = QtWidgets.QLineEdit(self.groupBox_BATCH)
		self.lineEdit_BATCH_mfDateYear.setGeometry(QtCore.QRect(int(self.screenwidth*0.16), self.batchEditRow3, self.inputFieldWidth2, self.controlHeight1))
		self.lineEdit_BATCH_mfDateYear.setObjectName("lineEdit_BATCH_mfDateYear")
		#
		# end of row 3, mfDate
		#
		self.pushButton_SAVEBATCHCHANGE = QtWidgets.QPushButton(self.groupBox_BATCH,clicked = self.saveBatchEdit)
		self.pushButton_SAVEBATCHCHANGE.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.11), self.buttonwidth1, self.buttonheight1 ))
		self.pushButton_SAVEBATCHCHANGE.setObjectName("pushButton_SAVEBATCHCHANGE")
		self.pushButton_CANCELBATCHCHANGE = QtWidgets.QPushButton(self.groupBox_BATCH,clicked = self.cancelBatchEdit)
		self.pushButton_CANCELBATCHCHANGE.setGeometry(self.cancelButtonX, int(self.screenbaseheight*0.11), self.buttonwidth1, self.buttonheight1)
		self.pushButton_CANCELBATCHCHANGE.setObjectName("pushButton_CANCELBATCHCHANGE")

		#
		# these are the display/edit fields for the selected devicetype
		############################################################################

		self.pushButton_EDITDEVICETYPE = QtWidgets.QPushButton(self.groupBox_BATCHEDITAREA,clicked = self.editDevicetype)
		self.pushButton_EDITDEVICETYPE.setGeometry(QtCore.QRect(int(self.screenwidth*0.36), int(self.screenbaseheight*0.19), self.buttonwidth1, self.buttonheight1))
		self.pushButton_EDITDEVICETYPE.setObjectName("pushButton_EDITDEVICETYPE")
		self.pushButton_EDITDEVICETYPE.setDisabled(True)
		self.pushButton_ADDDEVICETYPE = QtWidgets.QPushButton(self.groupBox_BATCHEDITAREA,clicked = self.setDevicetypeAddMode)
		self.pushButton_ADDDEVICETYPE.setGeometry(QtCore.QRect(self.addButtonX, int(self.screenbaseheight*0.19), self.buttonwidth2, self.buttonheight1))
		self.pushButton_ADDDEVICETYPE.setObjectName("pushButton_ADDDEVICETYPE")

		self.groupBox_DEVICETYPE = QtWidgets.QGroupBox(self.groupBox_BATCHEDITAREA)
		self.groupBox_DEVICETYPE.setGeometry(QtCore.QRect(self.detailBoxStartingX, int(self.screenbaseheight*0.2), self.detailBoxWidth, int(self.screenbaseheight*0.25)))
		self.groupBox_DEVICETYPE.setObjectName("groupBox_DEVICETYPE")


		self.label_DEVICETYPEID = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_DEVICETYPEID.setGeometry(QtCore.QRect(int(self.screenwidth*0.008), self.devicetypeEditRow1, int(self.screenwidth*0.04), int(self.screenbaseheight*0.02)))
		self.label_DEVICETYPEID.setObjectName("label_DEVICETYPEID")
		self.lineEdit_DEVICETYPE_deviceTypeID = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_deviceTypeID.setGeometry(QtCore.QRect(int(self.screenwidth*0.020), self.devicetypeEditRow1, self.inputFieldWidth2, int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_deviceTypeID.setObjectName("lineEdit_DEVICETYPE_deviceTypeID")

		self.label_DEVICETYPENAME = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_DEVICETYPENAME.setGeometry(QtCore.QRect(int(self.screenwidth*0.051), self.devicetypeEditRow1, int(self.screenwidth*0.04), int(self.screenbaseheight*0.02)))
		self.label_DEVICETYPENAME.setObjectName("label_DEVICETYPENAME")
		self.lineEdit_DEVICETYPE_deviceTypeName = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_deviceTypeName.setGeometry(QtCore.QRect(int(self.screenwidth*0.070), self.devicetypeEditRow1, int(self.screenwidth*0.08), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_deviceTypeName.setObjectName("lineEdit_DEVICETYPE_deviceTypeName")



		self.label_NUMBEROFSENSORS = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_NUMBEROFSENSORS.setGeometry(QtCore.QRect(int(self.screenwidth*0.16), self.devicetypeEditRow1, int(self.screenwidth*0.04), int(self.screenbaseheight*0.02)))
		self.label_NUMBEROFSENSORS.setObjectName("label_NUMBEROFSENSORS")
		self.lineEdit_DEVICETYPE_numberOfSensors = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_numberOfSensors.setGeometry(QtCore.QRect(int(self.screenwidth*0.18), self.devicetypeEditRow1, int(self.screenwidth*0.02), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_numberOfSensors.setObjectName("lineEdit_DEVICETYPE_numberOfSensors")

		self.label_DIMENSION = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_DIMENSION.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.07), int(self.screenwidth*0.06), int(self.screenbaseheight*0.02)))
		self.label_DIMENSION.setObjectName("label_DIMENSION")

		self.lineEdit_DEVICETYPE_dimension = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_dimension.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.09), int(self.screenwidth*0.06), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_dimension.setObjectName("lineEdit_DEVICETYPE_dimension")

		self.label_STARTINGSENSOR = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_STARTINGSENSOR.setGeometry(QtCore.QRect(int(self.screenwidth*0.08), int(self.screenbaseheight*0.07), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.label_STARTINGSENSOR.setObjectName("label_STARTINGSENSOR")

		self.lineEdit_DEVICETYPE_startingSensor = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_startingSensor.setGeometry(QtCore.QRect(int(self.screenwidth*0.08), int(self.screenbaseheight*0.09), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_startingSensor.setObjectName("lineEdit_DEVICETYPE_startingSensor")

		self.label_SENSOR1DISTANCE = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_SENSOR1DISTANCE.setGeometry(QtCore.QRect(int(self.screenwidth*0.14), int(self.screenbaseheight*0.07), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.label_SENSOR1DISTANCE.setObjectName("label_SENSOR1DISTANCE")

		self.lineEdit_DEVICETYPE_sensor1Distance = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_sensor1Distance.setGeometry(QtCore.QRect(int(self.screenwidth*0.14), int(self.screenbaseheight*0.09), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_sensor1Distance.setObjectName("lineEdit_DEVICETYPE_sensor1Distance")

		self.label_SENSOR2DISTANCE = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_SENSOR2DISTANCE.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.12), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.label_SENSOR2DISTANCE.setObjectName("label_SENSOR2DISTANCE")

		self.lineEdit_DEVICETYPE_sensor2Distance = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_sensor2Distance.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.14), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_sensor2Distance.setObjectName("lineEdit_DEVICETYPE_sensor2Distance")

		self.label_SENSORSPACING = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_SENSORSPACING.setGeometry(QtCore.QRect(int(self.screenwidth*0.07), int(self.screenbaseheight*0.12), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.label_SENSORSPACING.setObjectName("label_SENSORSPACING")

		self.lineEdit_DEVICETYPE_sensorSpacing = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_sensorSpacing.setGeometry(QtCore.QRect(int(self.screenwidth*0.07), int(self.screenbaseheight*0.14), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_sensorSpacing.setObjectName("lineEdit_DEVICETYPE_sensorSpacing")

		self.label_FRONTGAP = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_FRONTGAP.setGeometry(QtCore.QRect(int(self.screenwidth*0.13), int(self.screenbaseheight*0.12), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.label_FRONTGAP.setObjectName("label_FRONTGAP")

		self.lineEdit_DEVICETYPE_frontGap = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_frontGap.setGeometry(QtCore.QRect(int(self.screenwidth*0.13), int(self.screenbaseheight*0.14), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_frontGap.setObjectName("lineEdit_DEVICETYPE_frontGap")

		self.label_REVERSEORDER = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_REVERSEORDER.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.17), int(self.screenwidth*0.07), int(self.screenbaseheight*0.02)))
		self.label_REVERSEORDER.setObjectName("label_REVERSEORDER")

		self.lineEdit_DEVICETYPE_reverseOrder = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_reverseOrder.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.19), int(self.screenwidth*0.07), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_reverseOrder.setObjectName("lineEdit_DEVICETYPE_reverseOrder")

		self.label_TRACKWIDTH = QtWidgets.QLabel(self.groupBox_DEVICETYPE)
		self.label_TRACKWIDTH.setGeometry(QtCore.QRect(int(self.screenwidth*0.09), int(self.screenbaseheight*0.17), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.label_TRACKWIDTH.setObjectName("label_TRACKWIDTH")

		self.lineEdit_DEVICETYPE_trackWidth = QtWidgets.QLineEdit(self.groupBox_DEVICETYPE)
		self.lineEdit_DEVICETYPE_trackWidth.setGeometry(QtCore.QRect(int(self.screenwidth*0.09), int(self.screenbaseheight*0.19), int(self.screenwidth*0.05), int(self.screenbaseheight*0.02)))
		self.lineEdit_DEVICETYPE_trackWidth.setObjectName("lineEdit_DEVICETYPE_trackWidth")

		

		self.pushButton_SAVEDEVICETYPECHANGE = QtWidgets.QPushButton(self.groupBox_DEVICETYPE,clicked = self.saveDevicetypeEdit)
		self.pushButton_SAVEDEVICETYPECHANGE.setGeometry(QtCore.QRect(int(self.screenwidth*0.01), int(self.screenbaseheight*0.22), self.buttonwidth1,self.buttonheight1))
		self.pushButton_SAVEDEVICETYPECHANGE.setObjectName("pushButton_SAVEDEVICETYPECHANGE")
		self.pushButton_CANCELDEVICETYPECHANGE = QtWidgets.QPushButton(self.groupBox_DEVICETYPE,clicked = self.cancelDevicetypeEdit)
		self.pushButton_CANCELDEVICETYPECHANGE.setGeometry(QtCore.QRect(self.cancelButtonX, int(self.screenbaseheight*0.22), self.buttonwidth1,self.buttonheight1))
		self.pushButton_CANCELDEVICETYPECHANGE.setObjectName("pushButton_CANCELDEVICETYPECHANGE")


		self.pushButton_BURN = QtWidgets.QPushButton(self.centralwidget,clicked = self.burnBatch)
		self.pushButton_BURN.setGeometry(QtCore.QRect(int(self.screenwidth*0.18), int(self.screenbaseheight*0.57), int(self.screenwidth*0.04), int(self.screenbaseheight*0.02)))
		self.pushButton_BURN.setObjectName("pushButton_BURN")
		self.pushButton_EXIT = QtWidgets.QPushButton(self.centralwidget,clicked = self.exitApp)
		self.pushButton_EXIT.setGeometry(QtCore.QRect(int(self.screenwidth*0.224), int(self.screenbaseheight*0.57), int(self.screenwidth*0.04), int(self.screenbaseheight*0.02)))
		self.pushButton_EXIT.setObjectName("pushButton_EXIT")

		# outputbox

		self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
		self.scrollArea.setGeometry(QtCore.QRect(int(self.screenwidth*0.02), int(self.screenbaseheight*0.6), int(self.screenwidth*0.408), int(self.screenbaseheight*0.1)))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, int(self.screenwidth*0.408), int(self.screenbaseheight*0.1)))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

		self.output_Box = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
		self.output_Box.setGeometry(QtCore.QRect(0, 0, int(self.screenwidth*0.408), int(self.screenbaseheight*0.1)))
		self.output_Box.setObjectName("output_Box")
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.output_Box = QtWidgets.QTextEdit(readOnly=True)

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

		self.groupBox_ConnectShelf.setTitle(_translate("MainWindow", "Connect Shelf"))

		self.label_shelfConnectNotice.setText(_translate("MainWindow", " "))
		self.label_IPADDR.setText(_translate("MainWindow", "IP Address:"))
		self.label_PORT.setText(_translate("MainWindow", "Port:"))
		# this is temp
		self.logoImage.setText(_translate("MainWindow", "TEMP"))

		self.label_numSockets.setText(_translate("MainWindow", "# of PNP Sockets:"))
		self.label_STARTSOCKET.setText(_translate("MainWindow", "1st SockAddr(base 10):"))
        # self.pushButton_CONNECTSHELF.setText(_translate("MainWindow", "Connect"))

		self.groupBox_BATCHEDITAREA.setTitle(_translate("MainWindow", ""))
		self.label_SELECTBATCH.setText(_translate("MainWindow", "Select Batch"))
		self.pushButton_EDITBATCH.setText(_translate("MainWindow", "edit"))
		self.pushButton_ADDBATCH.setText(_translate("MainWindow", "+"))
		self.pushButton_EDITDEVICETYPE.setText(_translate("MainWindow", "edit"))
		self.pushButton_ADDDEVICETYPE.setText(_translate("MainWindow", "+"))
		self.groupBox_BATCH.setTitle(_translate("MainWindow", "Batch Selected"))
		self.label_BATCHID.setText(_translate("MainWindow", "BatchID:"))
		self.label_FACTORYID.setText(_translate("MainWindow", "FactoryID:"))
		self.label_FACTORYNAME.setText(_translate("MainWindow", "Fact Name goes here"))
	
		self.label_BATCH_deviceTypeID.setText(_translate("MainWindow", "DevicetypeID:"))
		self.label_MFDATEMONTH.setText(_translate("MainWindow", "MF Month:"))
		self.label_MFDATEDAY.setText(_translate("MainWindow", "MF Day:"))
		self.label_MFDATEYEAR.setText(_translate("MainWindow", "MF YEAR:"))

		self.pushButton_SAVEBATCHCHANGE.setText(_translate("MainWindow", "save"))
		self.pushButton_CANCELBATCHCHANGE.setText(_translate("MainWindow", "cancel"))


		self.groupBox_DEVICETYPE.setTitle(_translate("MainWindow", "DeviceType"))
		self.label_DEVICETYPENAME.setText(_translate("MainWindow", "Name:"))
		self.label_DEVICETYPEID.setText(_translate("MainWindow", "ID:"))
		self.label_NUMBEROFSENSORS.setText(_translate("MainWindow", "#PR:"))
		self.label_DIMENSION.setText(_translate("MainWindow", "Dimension:"))
		self.label_STARTINGSENSOR.setText(_translate("MainWindow", "StartPR:"))
		self.label_SENSOR1DISTANCE.setText(_translate("MainWindow", "PR1Dist:"))
		self.label_SENSOR2DISTANCE.setText(_translate("MainWindow", "PR2Dist:"))
		self.label_SENSORSPACING.setText(_translate("MainWindow", "PRSpace:"))
		self.label_FRONTGAP.setText(_translate("MainWindow", "FrontGap:"))
		self.label_REVERSEORDER.setText(_translate("MainWindow", "ReverseOrder:"))
		self.label_TRACKWIDTH.setText(_translate("MainWindow", "TrackWidth:"))

		self.pushButton_SAVEDEVICETYPECHANGE.setText(_translate("MainWindow", "save"))
		self.pushButton_CANCELDEVICETYPECHANGE.setText(_translate("MainWindow", "cancel"))

		self.pushButton_BURN.setText(_translate("MainWindow", "BURN TRACKS"))
		self.pushButton_EXIT.setText(_translate("MainWindow", "EXIT"))

