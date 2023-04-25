
# example of how this def would be called

#updateDatabaseTable(apiServer,"batches",['factoryID','deviceTypeID','mfDate'],
#                                         [1,210,'10/12/2022'])

import json,requests

BATCH_FILTER = "filter=deviceTypeID<3000&orderby=batchID"
DEVICETYPE_FILTER = "filter=deviceTypeID<3000&orderby=deviceTypeID"

# // example:
# //
# //dbInsert?tablename=displayfixtures&fields={"storeID":1,"level":1,"displayfixtureIDForUser":"testertest","type":"gondola","location":"Detroit"}
# modify this code to do both update and insert
def updateDatabaseTable(apiServer,tableName,fields,fieldVals,changeMode,filter):
    #changeMode is either "A" or "E" for add edit
	operation = ""
	addKeyfieldAddon = ""
	keyField = ""
	nextIDValue = 0
	URLAddon = '&fields={'
	
	if changeMode.upper()=="A":   #we are adding
		operation = "dbInsert"
		filter=""
		if (tableName.upper() == "BATCHES"):
			keyField = "batchID"
			nextIDValue = getMaxBatchID(apiServer) + 1
		if (tableName.upper() == "DEVICETYPES"):
			keyField = "deviceTypeID"	
			nextIDValue = getMaxDeviceTypeID(apiServer) + 1
		
		addKeyfieldAddon = '"' + keyField + '":"' + str(nextIDValue) + '",'
		URLAddon += addKeyfieldAddon

	if changeMode.upper()=="E":
		operation = "dbUpdate"

	

	for i in range(len(fields)):
		URLAddon += ('"' + fields[i] + '":"' + str(fieldVals[i]) + '",')
	# now fill  in  the keyfield for adds
	updateBatchURL = apiServer + operation + "?tablename=" + tableName + URLAddon 
	
	# print("maxbatchID =",getMaxBatchID(apiServer))
	# print("maxDeviceTypeID(apiServer)=",getMaxDeviceTypeID(apiServer))


	filtExp = ""
	if filter !="":	
		filtExp = "&filter=" + filter

	updateBatchURL = updateBatchURL[:len(updateBatchURL)-1] + "}" + filtExp

	# print("URL = ",updateBatchURL)
	return requests.get(updateBatchURL)
	
# updateBatchURL = apiServer + "dbUpdate?tablename="+"batches" + "&fields={%22" + "factoryID" + "%22:" + str(self['factoryID'])  + ",%22deviceTypeID%22:" + str(self['deviceTypeID']) + ",%22" + "mfDateMonth" + "%22:" + str(self['mfDateMonth']) + ",%22" + "mfDateDay:" + str(self["mfDateDay"]) + "}&filter=batchID=" + '6'  #str(self.selectedBatchID)
# example of how to call this
# updateDatabaseTable("https://apiserver.sungalcorp.synology.me/","batches",
# 		['factoryID','deviceTypeID','mfDateDay','mfDateMonth','mfDateYear'],
# 		[11,112,1,1,2022],"batchID=4")

def getBatches(apiServer,mode):
	rVal = getTable(apiServer,"batches",BATCH_FILTER)
	# a bit clugy, but for display, consolidate the date fields into a 
	# single date
	if mode.upper() == "DISPLAY":
		for batch in rVal:
			batch["mfDate"]= str(batch["mfDateMonth"]) + "/" + str(batch["mfDateDay"]) + "/" +str(batch["mfDateYear"])
			del batch["mfDateDay"]
			del batch["mfDateMonth"]
			del batch["mfDateYear"]
	return rVal

	
def getDeviceTypes(apiServer):
	return  getTable(apiServer,"deviceTypes",DEVICETYPE_FILTER)

def getTable(apiServer,tableName,specialConditions):
	#?filter=deviceTypeID<3000&orderby=batchID'
	url = apiServer + 'dbGet_' + tableName 
	if len(specialConditions) > 0:
		url += '?' + specialConditions
	
	resultTable = json.loads(requests.get(url).text)
	
	return [p for p in resultTable ]



# helper function to get highest batchID for adding a new batch where batchID = 
# the highest batchID + 1
def getMaxBatchID(apiServer):
	resultset = getTable(apiServer,'maxBatchID','')
	# print ("resultset for getMaxBatchID =", resultset)
	return resultset[0]["maxbatchID"]

# helper function to get highest deviceTypeID for adding a new batch where deviceTypeID = 
# the highest deviceTypeID + 1

def getMaxDeviceTypeID(apiServer):
	resultset = getTable(apiServer,'maxDeviceTypeIDForTracks','')
	# print("resultset for getMaxDeviceTypeID =", resultset)
	return resultset[0]["maxDeviceTypeID"]


def getDictionary(apiServer,tableName,keyField):
	rVal = {}
	resultDataSet = getTable(apiServer,tableName,"")
	for record in resultDataSet:
		rVal[str(record[keyField])] = record           
	return rVal

    # batchDictionary = 

	# {
	# 	"1" : {batchID:1, factoryid : 002, mfdate:"01/01/2022"},
	# 	"2" : {batchID:2, factoryid : 002, mfdate:"03/02/2022"}
	# }
    # batchnumber = 4;
	# to get a batch record from the dictionary we reference :

	# batchDictionary["2"] = {batchID:2, factoryid : 002, mfdate:"03/02/2022"}


