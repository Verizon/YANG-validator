# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import sys
import threading
import asyncio
import jsonToYang
import json
import traceback
import time
import pprint

testJsonStr = None

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

    print('going to sleep')
    time.sleep(1)
    print('Processed this many transactions with yang: ' + str(counter));
    counter = 0

#
# Main code
#
if len(sys.argv) == 1:
  print('Must pass a json strong')
  exit()
else:
  print('Using json string: ' + sys.argv[1])

testJsonStr = sys.argv[1]

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
