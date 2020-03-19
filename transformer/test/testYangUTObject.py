# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import json
import jsonToYang



jsonStr = '{"data":{"id":"301270715594854765","type":"FilteredAlarm","attributes":{"id":"301270715594854765","alarm-id":"-4808036964064782398","node-id":"6f1d9c15-c61d-44c6-823a-288aa8f3246e","ra-alarm-id":"0100005452-0070-1442","node-type":"6500","state":"CLEARED","resource":"OTUTTP-1-4-2","resource-id":"OTUTTP-1-4-2","native-condition-type":"RTCLK","condition-severity":"INFO","service-affecting":"SERVICE_AFFECTING","manual-clearable":false,"additional-text":"Loss Of Clock","first-raise-time":"2019-05-02T17:31:26.000Z","last-raise-time":"2019-05-10T14:58:11.000Z","clear-time":"2019-05-10T14:58:25.000Z","number-of-occurrences":2708,"acknowledge-state":"NOT_ACKNOWLEDGED","device-id":"a65dacb4-7d3e-3e2b-83c3-8598da6c2d69","device-name":"CN6500T12-196004","device-long-name":"CN6500T12-196004","ip-address":"166.38.196.4","mac-address":"EC:B0:E1:5A:10:05","card-type":"5x100G/12x40G | QSFP28/QSFP+ | PKT/OTN I/F","fic":"6500T - 400IP","partition":["29d55926-2641-4aa3-8013-97acab7f3430"],"additional-attrs":{"FIC":"6500T - 400IP","YEAR":"2019","MODE":"NONE","aidtype":"OTUTTP","location":"NEND","source":"6500:OTUTTP-1-4-2","CARDTYPE":"5x100G/12x40G | QSFP28/QSFP+ | PKT/OTN I/F","direction":"RCV"},"affected-inventory-ids":[],"sequence-id":"1557500291000"}}}'

jsonObj = json.loads(jsonStr)

mappingDetails = jsonToYang.getMappingDetails("UT_ALARMS_CIENA")


	
yangJsonStr = jsonToYang.convertToYangJsonStr(mappingDetails, jsonObj)


