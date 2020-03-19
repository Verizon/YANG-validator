# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import json
import jsonToYang

#with open('CiscoUT.json') as json_file:
with open('equipment.json') as json_file:
    jsonObj = json.load(json_file)
    print (json.dumps(jsonObj))
    mappingDetails = jsonToYang.getMappingDetails("UTS_EQUIPMENT")
    yangJsonStr = jsonToYang.convertToYangJsonStr(mappingDetails, jsonObj)
