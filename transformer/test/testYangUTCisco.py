# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import json
import jsonToYang


#jsonStr = '{"push.push-change-update":{"push.update-data":{"alm.alarm":{"alm.owner":"","alm.source-object-id":0,"alm.perceived-severity":"critical","alm.system-received-time":"2019-04-0204: 07: 16.363","alm.probable-cause":"mplsTunnelDown","alm.root-cause-alarm-identifier":{"alm.event-identifier":0},"alm.cause-type":"cause-unknown","alm.system-update-time":"2019-04-0306: 56: 19.232","alm.description":"Device: NYCMNYWS-CSCX68Y25BMPLSTunnelwithid: nullisOperationallyDOWN","alm.node-ref":"NYCMNYWS-CSCX68Y25B","alm.category":"MPLS","alm.source-object-ref":"MD=CISCO_EPNM!ND=NYCMNYWS-CSCX68Y25B","alm.business-key":"MPLS_TUNNEL: 166.34.111.78: : : ##SubAlarm@@_421","alm.ack-state":"unacknowledged","alm.remote-interface-ip-address":"166.34.111.78","alm.alarm-identifier":{"alm.resource-object-ref":"MD=CISCO_EPNM!ND=NYCMNYWS-CSCX68Y25B","alm.probable-cause":"mplsTunnelDown","alm.event-identifier":892322899}}},"push.topic":"alarm","push.time-of-update":"2019-04-0306: 56: 19.232","push.notification-id":-9058108182000441521,"push.operation":"push: modify"}}'

jsonStr = '{"push.push-change-update": {"push.update-data": {"alm.alarm": {"alm.owner": "", "alm.source-object-id": 0, "alm.perceived-severity": "critical", "alm.system-received-time": "2019-05-08 11:00:01.366", "alm.probable-cause": "entSensorThresholdNotification", "alm.root-cause-alarm-identifier": {"alm.event-identifier": 0}, "alm.cause-type": "cause-unknown", "alm.system-update-time": "2019-06-04 05:18:54.785", "alm.description": "Alarm Duplicating: Device:166.34.111.22, Sensor 0/6-DENALI ADC DACREF1 VTUNE with current value 198 milli voltsDC has violated  the threshold value 500 milli voltsDC.", "alm.node-ref": "NYCMNYWS-CSCX68Y08A", "alm.category": "Optical Networking", "alm.source-object-ref": "MD=CISCO_EPNM!ND=NYCMNYWS-CSCX68Y08A", "alm.business-key": "166.34.111.22:entSensorThresholdNotification:39098##SubAlarm@@_2", "alm.ack-state": "unacknowledged", "alm.remote-interface-ip-address": "166.34.111.22", "alm.alarm-identifier": {"alm.resource-object-ref": "MD=CISCO_EPNM!ND=NYCMNYWS-CSCX68Y08A", "alm.probable-cause": "entSensorThresholdNotification", "alm.event-identifier": 1610487892}}}, "push.topic": "alarm", "push.time-of-update": "2019-06-04 05:18:54.785", "push.notification-id": -5995635441674197083, "push.operation": "push:modify"}}'

jsonObj = json.loads(jsonStr)
#print(json.dumps(jsonObj, indent=4))

mappingDetails = jsonToYang.getMappingDetails("UT_ALARMS_CISCO")


	
yangJsonStr = jsonToYang.convertToYangJsonStr(mappingDetails, jsonObj)


