# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import traceback
import xmltodict
import json
import pprint

def readFile(fileName):
    xml = None
    xmlFd = None
    try:
        xmlFd = open(fileName, "r")
        xmlStr = ""
        for line in xmlFd:
            xmlStr = xmlStr + line
        xml = xmlStr
    except Exception as e:
        traceback.print_exc()
    finally:
        if xmlFd != None:
            xmlFd.close()
            
    return xml

jsonStr = readFile("equipment.json")
jsonObj = json.loads(jsonStr)
root = dict()
root['root'] = jsonObj
xmlStr = xmltodict.unparse(root, pretty=True)

fw = open("equipment.xml", "w")
fw.write(xmlStr)
fw.close()

jsonObj = xmltodict.parse(xmlStr)
jsonObj = jsonObj['root']
pprint.pprint(json.loads(json.dumps(jsonObj)))
