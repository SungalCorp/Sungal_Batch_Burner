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
