#
# Copyright Verizon Inc.
# Licensed under the terms of the Apache License 2.0 license.  See LICENSE file in project root for terms.
#
import json
import sys
import ietf_network_topology
from pyangbind.lib import pybindJSON

ietf_network_instance = ietf_network_topology.ietf_network()
network = None
indent = 10 
listNameH = None
prevNE = None
prevTP = None
segment = 0
def walkList(listContents, listName):
   global indent
   global listNameH
#  print (' '.rjust(indent) + "ListName:" + listName + " Indent:" + str(indent))
   listNameH = listName
   for item in listContents:
    if (type(item) == str):
      print ( "STR---" + item + ":" + listContents[item])
    if (type(item) == dict):
       indent=indent+5
       walkDict(item)	
       indent=indent-5

def walkDict(dictItem):
   global indent
   global listNameH
   global network
   global prevNE
   global prevTP
   global segment

   if (listNameH == 'circuit'):
      network =  ietf_network_instance.networks.network.add(dictItem['circuitName'])
   if (listNameH == 'portRef' and 'neName' in dictItem and dictItem['neName'] not in network.node):
      network.node.add(dictItem['neName']) 
   if (listNameH == 'portRef' and 'neName' in dictItem and dictItem['neName'] in network.node and 'portAID' in dictItem and dictItem['portAID'] not in network.node[dictItem['neName']].termination_point):
      network.node[dictItem['neName']].termination_point.add(dictItem['portAID'])
      if (prevNE != None and prevTP != None):
          segment = segment + 1
          link = network.link.add('segment'+ str(segment))
          link.source.source_node = prevNE
          link.source.source_tp = prevTP
          link.destination.dest_node = dictItem['neName']
          link.destination.dest_tp = dictItem['portAID']
      prevNE = dictItem['neName']   
      prevTP = dictItem['portAID']   

   for dictTag in dictItem:

#    if (type(dictItem[dictTag]) == str and listNameH == 'portRef'):
#       print(' '.rjust(indent) +  dictTag + ":" + dictItem[dictTag],  file=sys.stderr)
#    if (type(dictItem[dictTag]) == str ):
#       print(' '.rjust(indent) +  dictTag + ":" + dictItem[dictTag])
     if (type(dictItem[dictTag]) == dict):
#       print('DictTag:'.rjust(indent)+ dictTag)
        walkDict(dictItem[dictTag])
     if (type(dictItem[dictTag]) == list) :
#        print(' '.rjust(indent) + 'ListTag:'+ dictTag)
        walkList(dictItem[dictTag], dictTag)

def convertToYangJsonStr(jsonObj):
  global indent
  circuitdata = jsonObj['circuitData']
  global ietf_network_instance
  global prevNE
  global prevTP
  global segment
  ietf_network_instance = ietf_network_topology.ietf_network()
  prevNE = None
  prevTP = None
  segment = 0
  walkDict(circuitdata)
# populated all the node and tp ids
# print (pybindJSON.dumps(ietf_network_instance,mode="ietf"))
  return(pybindJSON.dumps(ietf_network_instance,mode="ietf"))

