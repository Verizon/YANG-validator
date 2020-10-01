#
# Copyright Verizon Inc.
# Licensed under the terms of the Apache License 2.0 license.  See LICENSE file in project root for terms.
#
import json
import openconfig_platform
from pyangbind.lib import pybindJSON

indent = 10 
parent = None
parentSlot = None
parentSlotIndent = 0
def walkList(listContents, componentType):
   global indent
   global parent 
   global parentSlot
   global parentSlotIndent
#  print ("Component Type:" + componentType + " Indent:" + str(indent))
   if (componentType == 'shelf'):
      if listContents[0]['tid'] in op.components.component:
         return
      shelf = op.components.component.add(listContents[0]['tid'])
#      shelf = op.components.component.add(listContents[0]['name'])
      parent = shelf
      if ('vendor' in listContents[0]):
        shelf.state.mfg_name = listContents[0]['vendor']
#     if ('type' in listContents[0]):
#       shelf.model.componenttype = listContents[0]['type']
      if ('model' in listContents[0]):
        shelf.state.description = listContents[0]['model']

   if (componentType == 'slot'):
      for item in listContents:
      # Slot/subslot 
         slot = None;
         if (parentSlot == None):
            parentSlot = item['slotName']
            parentSlotIndent = indent
            slot = parent.holder.slots.slot.add(item['slotName'])
            slot.slotnumber = item['slotNumber']

         if (parentSlotIndent == indent):
            parentSlot = item['slotName']
            if ( item['slotName'] not in parent.holder.slots.slot ):
               slot = parent.holder.slots.slot.add(item['slotName'])
               slot.slotnumber = item['slotNumber']

         if (item['slotName'] != parentSlot):
            slot = parent.holder.slots.slot[parentSlot]

         if ('card' in item):
            card = op.components.component.add(item['card'][0]['cardId'])
            if ('description' in item['card'][0]):
              card.state.description = item['card'][0]['description']
            card.state.mfg_name = item['card'][0]['vendor']
            comp = slot.component.add(item['card'][0]['cardId'])
            if (item['slotName'] != parentSlot):
               comp.subslotname  = item['slotName']
               comp.subslot  = item['slotNumber']
                     


   for item in listContents:
#   if (type(item) == str):
#      print ( "---" + item + ":" + listContents[item])
    if (type(item) == dict):
       indent=indent+5
       walkDict(item)	
       indent=indent-5

def walkDict(dictItem):
   global indent
   for dictTag in dictItem:
#     if (type(dictItem[dictTag]) == str):
#        print(' '.rjust(indent) +  dictTag + ":" + dictItem[dictTag])
      if (type(dictItem[dictTag]) == dict):
#        print('DictTag:'+ dictTag)
         walkDict(dictItem[dictTag])
#     if (type(dictItem[dictTag]) == list and ( dictTag == 'shelf' or dictTag == 'slot' or dictTag == 'card' or dictTag == 'port')):
      if (type(dictItem[dictTag]) == list and ( dictTag == 'shelf' or (dictTag == 'slot')  or dictTag == 'card')):
#         print(' '.rjust(indent) + 'ListTag:'+ dictTag)
         walkList(dictItem[dictTag], dictTag)

op = openconfig_platform.openconfig_platform()
def convertToYangJsonStr(jsonObj):
  equipdata = jsonObj['equipmentDtlData']
  for equipment in equipdata['equipmentLst']:
    for equipmentContainer in equipment['equipmentContainer']:
      for virtualNE in equipmentContainer['virtualNE']:
        for equipTag in virtualNE:
          if (type(virtualNE[equipTag]) == list):
             walkList(virtualNE[equipTag], equipTag)
  return(pybindJSON.dumps(op))
