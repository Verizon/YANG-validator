# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import json
import jsonToYang
import UTSEquipment

#with open('CICHRBNC-0023_Equipment_Response.json') as json_file:
with open('UTSEquipmentDetail2.json') as json_file:
    jsonObj = json.load(json_file)
    mappingDetails = jsonToYang.getMappingDetails("UTS_EQUIPMENT_API")
    if mappingDetails['isEquipmentTopic'] == 'true' :
       yangJsonStr = UTSEquipment.convertToYangJsonStr(jsonObj)
       print (str(yangJsonStr))
