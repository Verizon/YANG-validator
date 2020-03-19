# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import json
import jsonToYang


jsonStr = '{"data": [{"attributes": {"ip-address": "10.182.10.105", "id": "-4014091938995079370", "native-condition-type": "LOS_OTS", "manual-clearable": false, "state": "ACTIVE", "alarm-id": "-4014091938995079370", "ra-alarm-id": "0100001127-0008-0560", "mac-address": "40AB07220500", "additional-attrs": {"source": "6500:OPTMON-1-6-13", "direction": "RCV", "location": "NEND", "mode": "NONE", "aidtype": "OPTMON"}, "service-affection": "SERVICE_AFFECTING", "device-id": "f114lb1e-c6d4-3690-96ed-966af131822d", "number-of-occurances": 2, "first-raise-time": "2017-10-23T14:36:18:00Z", "node-type": "6500", "additional-text": "Loss of Signal", "resource": "OPTMON-1-6-13", "acknowledge-state": "NOT_ACKNOWLEDGED", "condition-severity": "MAJOR", "last-raise-time": "2017-10-25T18:35:55:00Z", "device-name": "PC0722CRFE", "partition": [], "node-id": "f490c132-9a26-4b01-babf-99dea16fb099", "affecte-inventory-ids": []}, "type": "FilteredAlarm", "id": "-4014091938995079370"}]}'

jsonObj = json.loads(jsonStr)

mappingDetails = jsonToYang.getMappingDetails("UT_ALARMS_CIENA")


	
yangJsonStr = jsonToYang.convertToYangJsonStr(mappingDetails, jsonObj)


