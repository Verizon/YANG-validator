# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import sys
import getopt
from pyangbind.lib import pybindJSON
import json
import logging
import traceback
import sys
from pprint import pformat
import re
import time


topicModelMapping = [
  {"topic": "ENMV_SAMSUNG5G_CPEDATA", "mappingFile": "mappings/samsungCpePerfdataYangMap.json", "isEquipmentTopic": "false"},
  {"topic": "BNC-FILTERED-ALARMS", "mappingFile": "mappings/bncFilteredAlarms.json" , "isEquipmentTopic": "false"},
  {"topic":"UT_ALARMS_CIENA","mappingFile": "mappings/UT_Ciena_AlarmMapper.json" , "isEquipmentTopic": "false"},
  {"topic":"UT_ALARMS_CIENA_OBJ","mappingFile": "mappings/UT_Ciena_AlarmMapperObject.json" , "isEquipmentTopic": "false"},
  {"topic":"UT_ALARMS_CISCO","mappingFile": "mappings/UT_Cisco_AlarmMapper.json" , "isEquipmentTopic": "false"},
  {"topic":"UT_ALARMS_CISCO_CCS","mappingFile": "mappings/UT_CiscoCCS_AlarmMapper.json" , "isEquipmentTopic": "false"},
  {"topic":"UTS_EQUIPMENT","mappingFile": "mappings/UTS_EquipmentMapper.json" , "isEquipmentTopic": "false"},
  {"topic":"MSE_ALARMS_CISCO","mappingFile": "mappings/MSE_Cisco_AlarmMapper.json" , "isEquipmentTopic": "false"},
  {"topic":"MSE_ALARMS_JUNIPER","mappingFile": "mappings/MSE_Juniper_AlarmMapper.json" , "isEquipmentTopic": "false"},
  {"topic":"UTS_EQUIPMENT_API","mappingFile": "mappings/UTS_EquipmentMapper.json" , "isEquipmentTopic": "true"},
  {"topic":"UTS_CIRCUIT_API","mappingFile": "mappings/UTS_CircuitMapper.json" , "isEquipmentTopic": "false"}
]

loadedMaps = []
rootJson  = None

def getAllMappingDetails():
  global topicModelMapping

  mapList = []

  for mappingInfo in topicModelMapping:
    # Load mapping file
    mappingObj = loadMappingFile(mappingInfo['mappingFile'])

    mappingDetails = dict()
    mappingDetails['topic'] = mappingInfo['topic']
    mappingDetails['mappingObj'] = mappingObj
    mappingDetails['isEquipmentTopic'] = mappingInfo['isEquipmentTopic']

    mapList.append(mappingDetails)

  return json.dumps(mapList)

def getMappingDetails(topic):
  global loadedMaps
  global topicModelMapping
  mapDetails = None
  # is map loaded yet
  for maps in loadedMaps:
    if maps['topic'] == topic:
      mapDetails = maps
      break

  # it is just return
  if mapDetails != None:
    return mapDetails

  # load mapping file

  # Find configuration we want
  mappingInfo = None
  for topicModel in topicModelMapping:
    if topicModel['topic'] == topic:
      mappingInfo = topicModel
      break

  if mappingInfo == None:
    print('No mapping found for: ' + topic)
    return None

  # Load mapping file
  mappingObj = loadMappingFile(mappingInfo['mappingFile'])

  mappingDetails = dict()
  mappingDetails['topic'] = topic
  mappingDetails['mappingObj'] = mappingObj
  mappingDetails['isEquipmentTopic'] = mappingInfo['isEquipmentTopic']

  # Load python object first (import)
  try:
    yangObj = __import__(mappingObj['pyangObj'])
  except ImportError as e:
    print(str(e))
    return None
  mappingDetails['yangObj'] = yangObj

  loadedMaps.append(mappingDetails)

  return mappingDetails

def loadMappingFile(file):
  #
  # Read the yang mapper for samsung
  #
  mapperStr = ''
  with open(file, 'r') as yp:
    line = yp.readline()
    while line:
      mapperStr = mapperStr + line
      line = yp.readline()

  #
  # Convert mapper to jsonObj
  #  
  mapperObj = json.loads(mapperStr)
  return mapperObj

#
# Convert json string to json object
#
def jsonToPyangObject(mappingDetails, jsonStr):
  loadedObject = pybindJSON.loads(jsonStr, mappingDetails['yangObj'], mappingDetails['mappingObj']['modelName'])
  return loadedObject

def convertToYangObject(mappingDetails, line):
  return jsonToPyangObject(mappingDetails, line)

def validateYang(mappingDetails, yangJson):
  yangObj = convertToYangObject(mappingDetails, yangJson)
  return pybindJSON.dumps(yangObj)
