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

topic = None
jsonStr = None

def convertToYang(topic, jsonStr):
  jsonObj = json.loads(jsonStr)

  mappingDetails = jsonToYang.getMappingDetails(topic)

  yangStr = jsonToYang.convertToYangJsonStr(mappingDetails, jsonObj)
  #pprint.pprint(yangStr)

  return yangStr

#
# Main code
#
#if len(sys.argv) < 1:
#  print('Must pass a topic and input json string')
#  exit()
#else:

while True:
  topic = input("Topic")
  print('Using topic: ' + topic)
  sys.stdout.flush()
  jsonStr = input("Enter Json")
  print('Using json string: ' + jsonStr)
  sys.stdout.flush()

  yangStr = convertToYang(topic, jsonStr)

  print('YANG_RESPONSE=' + yangStr)
  print('END PROCESSING')
  sys.stdout.flush()
