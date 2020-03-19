# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import threading
import asyncio
import jsonToYang
import json
import traceback
import time
import pprint

testJsonStr = "{\"eventTime\": \"2019-03-23T02:50:00+00:00\", \"data\": [{\"valueUnit\": \"%\", \"typeId\": 0, \"typeValue\": \"2.066667\", \"valueType\": \"float\", \"typeName\": \"ControlCpuUsage\"}, {\"valueUnit\": \"%\", \"typeId\": 1, \"typeValue\": \"26.000000\", \"valueType\": \"float\", \"typeName\": \"MemoryUsage\"}, {\"valueUnit\": \"%\", \"typeId\": 2, \"typeValue\": \"10.000000\", \"valueType\": \"float\", \"typeName\": \"DiskUsage\"}, {\"valueUnit\": \"\u00b0C\", \"typeId\": 3, \"typeValue\": \"27.000000\", \"valueType\": \"float\", \"typeName\": \"Temperature\"}], \"annotatedFamilyId\": \"CPE_RESOURCE\", \"neId\": \"100\", \"indexes\": [{\"indexName\": \"CPE ID\", \"indexId\": 0, \"indexValue\": \"20dbab03f5ec\"}], \"neType\": \"cpefama\", \"familyId\": 601, \"neVersion\": \"v_0_2_3_28\"}"

counter = 0

class YangConverter(threading.Thread):
  def __init__(self, name):
    threading.Thread.__init__(self)
    self.name = name 

  def convertToYang(self, topic, jsonStr):
    jsonObj = json.loads(jsonStr)

    mappingDetails = jsonToYang.getMappingDetails(topic)

    yangStr = jsonToYang.convertToYangJsonStr(mappingDetails, jsonObj)
    #pprint.pprint(yangStr)

  def run(self):
    global counter
    while True:
      self.convertToYang('ENMV_SAMSUNG5G_CPEDATA', testJsonStr)
      counter = counter + 1

class Timer(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    global counter

    for i in range(1,5):
      print('going to sleep')
      time.sleep(1)
      print('Processed this many transactions with yang: ' + str(counter));
      counter = 0

#
# Main code
#
threadLock = threading.Lock()
try:
  thread1 = YangConverter("YangConverterThread-1")
  thread1.start()

  thread2 = Timer()
  thread2.start()

  thread1.join()
  thread2.join()
except Exception as e:
  print("Error processing: " + str(e))
  trackeback.print_exc()
