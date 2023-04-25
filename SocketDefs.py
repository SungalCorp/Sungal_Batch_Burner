
# this  is  taken from the java code of the current AutoInstaller

############################################################################################
# this is how the serial number is generated, we need to do this in python equivalent code
############################################################################################
# public static String generateSerialNumber(Integer batchNumber) {
#         // generate a random number between 1 and 16,777,215, convert to  hex encoded string with length 6 (3 bytes)
#         String suffix = encodeDec(getRandomNumber(1, 16777215), 16, 6);

#         // convert batchNumber to a 6 character hex  encoded string with length 6 (3 bytes)
#         String convertedBatchNumber = encodeDec(batchNumber, 16, 6);

#         // convert the batch number to a 6 character text-hex string
#         // concatinate the 2 strings and return the result
#         return convertedBatchNumber + suffix;
#     }

#########################################################################################################################
# this is how the serial number is written to the data sector, the batch number is still in bytes 7-9  (1 relative).
#########################################################################################################################
# private Boolean writeSerialNumberToPNPSocket(String ipAddress, int port, int PNPSocketAddress, String sectorData, String newSerialNumber, int timeOut) {
#     // insert newSerialNumber into the beginning of the sectorData, then write the whole sector to the track's memory
#     // this is the "SDK" command to set geographical position. We are using the 16 bytes there to store serial number
#     writeConsole("newSerialNumber = " + newSerialNumber);
#     writeConsole("sectorData = " + sectorData);
#     String newSectorData = (newSerialNumber + sectorData.substring(newSerialNumber.trim().length())).trim();
#     String checksum = SocketRetrieval.generateCheckSum(newSectorData);
#     String hexRequestString = "1B7500" + encodeDec(PNPSocketAddress, 16, 2) + "1000" + newSectorData + checksum;
#     writeConsole("hexRequestString = " + hexRequestString + ", checksum = " + checksum);
#     String returnMSG = writeSocket(ipAddress, port, hexRequestString, timeOut);
#     return !returnMSG.substring(12, 14).equals("82"); // 82 is the error code, otherwise things are good.
# }



############################################################################################
# this is how the checksum is calculated, basically xor every byte of data.
############################################################################################
# public static String generateCheckSum(String dataArray) {
#         // required that dataArray = hex coded  
#         int bcc = 0;
#         for (int i = 0; i < dataArray.length(); i += 2) {
#             int currVal = CodeConverter.decodeBaseN(dataArray.substring(i, i + 2), 16);
#             bcc ^= currVal;
#         }
#         return encodeDec(bcc, 16, 2).toUpperCase();
#     }

from fnmatch import translate
from random import randint
import socket
import time
import codecs
import binascii
from unittest import result

# '1B7500' write
# '1B7600' read

# send to check track if there is a track: 1B 04 00 31 00 00 00
# send to check sensor value: 1B 06 00 31 04 00 03 00 19 00 1A

# scanTrackString = "1B 04 00"+ 31 + "00 00 00"


# IPADDR = ''      #'69.122.14.38'
# PORT = 0         # 63003
# NUM_PNP_SOCKETS = 0     #24
# FIRST_SOCKET_ADDRESS = 0    #49
# BATCH_NUMBER = 6
PNP_SOCKET_TIMEOUT = 1

def sendHexString(scanTrackString,mySocket):

        mySocket.settimeout(PNP_SOCKET_TIMEOUT)
        mySocket.send(scanTrackString) # send string
        
        data = mySocket.recv(1024) # receive string
         

        return binascii.hexlify(data).decode() # decode string
        # return data 

def getSocketAddressForHexString(i,firstSocket):
            socketHexAddress = i
            if socketHexAddress == 1:
                socketHexAddress = firstSocket            
            
            socket_num = socketHexAddress

            socketHexAddress = hex(socket_num)
            socketHexAddress = socketHexAddress[len("0x"):100]
            if socket_num < 16:
                socketHexAddress = '0'+ socketHexAddress.strip()
            return  socketHexAddress

def powerShelf(self,mode,ipAddress,port):
    
    mSocket = socket.socket()
    mSocket.settimeout(2)
    mSocket.connect((ipAddress,port))

    suffix = "0000"
    unhexifiedString1 = "1b7300FA0100" + suffix # turn track(s) power off
    unhexifiedString2 = "1b7300FB0100" + suffix # turn PNP socket off

    if mode.upper()=="ON":
        suffix = "6464"
        unhexifiedString1 = "1b7300FB0100" + suffix # turn PNP socket on
        unhexifiedString2 = "1b7300FA0100" + suffix # turn track(s) power on

    requestString1 = binascii.unhexlify(unhexifiedString1)
    requestString2 = binascii.unhexlify(unhexifiedString2)
    
    try:
        print("sendHexString(requestString1,myTCPIPSocket)=",sendHexString(requestString1,mSocket))      
        time.sleep(4)
        print("sendHexString(requestString2,myTCPIPSocket)=",sendHexString(requestString2,mSocket))
        time.sleep(4)
    except:
        mSocket.close()
        self.label_shelfConnectNotice.setText( mode + " UNABLE TO TURN SHELF POWER ")  
        return 

    mSocket.close()

def burnBatchesAndSerialNumbers(nSockets,firstSocket,batchno,myTCPIPSocket):

    # String checksum = SocketRetrieval.generateCheckSum(newSectorData);
    # String hexRequestString = "1B7500" + encodeDec(PNPSocketAddress, 16, 2) + "1000" + newSectorData + checksum;
    # writeConsole("hexRequestString = " + hexRequestString + ", checksum = " + checksum);
    # String returnMSG = writeSocket(ipAddress, port, hexRequestString, timeOut);
    # return !returnMSG.substring(12, 14).equals("82"); // 82 is the error code, otherwise things are good.

    # mySocket = socket.socket()
    # mySocket.connect((IP,port))
    
    # turn tcpip socket and pnp on 
    
    
    socket_num = 0
    print("++++++++Burning  discovered tracks for all active sockets++++++")
    for i in range(1, int(nSockets + 1)):

        # print("????????????request for datasector response = " ,sendHexString(binascii.unhexlify("1B760004000000"),myTCPIPSocket))

        socketAddress = getSocketAddressForHexString(i,firstSocket)
        print("  =====  currently working on socketAddress ", socketAddress)
        newSerialNumber = generateSerialNumber(batchno)
        print("                generated Serial# = ",newSerialNumber)
        newSectorData = (newSerialNumber).ljust(32,'0')
        checksum = generateChecksum(newSectorData)
        print(" ")
        print("                attempting to write ",newSectorData," to  the track sector")
        # 47.23.154.66
        unhexifiedString = '1b7500' + socketAddress + '1000' + newSectorData + checksum
        requestString = binascii.unhexlify(unhexifiedString)
        print("                unhexifiedrequestString = ",unhexifiedString)
        
        
        try:
            # write to sector, get response
            writeSectorResponse = sendHexString(requestString,myTCPIPSocket)
            print('                Rceived from shelf(hexlified): ' + writeSectorResponse) 
            print('                write is successful, now reading back ... ')
            try:
                requestString = binascii.unhexlify('1B7600'+socketAddress+'000000')
                readSectorResponse = sendHexString(requestString,myTCPIPSocket)
                print ("                read is successful, response = ",readSectorResponse)
            except:
                print('                 read unsuccessful')
            # 1B760005000000

            # requestString = b'\x1b\x76\x00\x31\x00\x00\x00'
            print('                request string =',requestString)
            print('                unhexified request = ','1B7600'+socketAddress+'000000')
            dataSector = sendHexString(requestString,myTCPIPSocket)
            print ('           RESULT: Success: Data sector = ',dataSector)
        except:
            print('            RESULT: no Track - write process aborted')
    print("++++++++Burning  discovered tracks Completed ++++++")
    
# # Creating a string variable
# str = "Geeks for Geeks"
 
# # Printing the output of ljust() method
# print(str.ljust(20, '0'))

# # Creating a string variable
# str = "Geeks for Geeks"
 
# # Printing the output of ljust() method
# print(str.ljust(20, '0'))

def encodeToHex(val,places,placeCharacter):    
    return (hex(val)[len("0x"):100]).rjust(places,placeCharacter)

def generateSerialNumber(batchno):
    # returns a string representing hex representation of serial number
    rVal = encodeToHex(int(batchno),6,'0') + encodeToHex(randint(1,16777215),6,'0')
    return rVal
    # return encodeToHex(5,6,'0') + encodeToHex(5,6,'0')

def  generateChecksum(datasector):
    byteStr = binascii.unhexlify(datasector)
    result = 0
    for b in byteStr:
        result =  result ^ b
    
    return encodeToHex(result,2,'0')

def getTracks(IP,port,nSockets,firstSocket,batchno,mySocket):

        for i in range(int(nSockets)):

            socketAddress = getSocketAddressForHexString(i,firstSocket)

            print('after stripping, socketAddress=',socketAddress)

            requestString = binascii.unhexlify('1b0600'+socketAddress+'0400030019001A')
            print('request string =',requestString)
            try:
                sendHexString(requestString,mySocket)
            except:
                print('no Track')
# send(IPADDR,PORT,NUM_PNP_SOCKETS,FIRST_SOCKET_ADDRESS,BATCH_NUMBER)

        


    
