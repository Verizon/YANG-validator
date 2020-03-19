# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import json
import UTSEquipment

#with open('CICHRBNC-0023_Equipment_Response.json') as json_file:  
with open('UTSEquipmentDetail.json') as json_file:  
    data = json.load(json_file)
    output = UTSEquipment.convertToYangJsonStr(data)
    print (str(output))
