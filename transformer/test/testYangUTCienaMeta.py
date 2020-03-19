# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import json
import jsonToYang

#with open('CienaUTMetaAddAttrMissVal.json') as json_file:
#with open('CienaUTMetaNoAddAttr.json') as json_file:
with open('CienaUTMetaNoAddAttr4.json') as json_file:
#with open('CienaUTMeta.json') as json_file:
    jsonObj = json.load(json_file)
    print (json.dumps(jsonObj))
    mappingDetails = jsonToYang.getMappingDetails("UT_ALARMS_CIENA_OBJ")
    yangJsonStr = jsonToYang.convertToYangJsonStr(mappingDetails, jsonObj)
