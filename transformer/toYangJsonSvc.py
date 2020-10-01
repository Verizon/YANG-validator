#
# Copyright Verizon Inc.
# Licensed under the terms of the Apache License 2.0 license.  See LICENSE file in project root for terms.
#
from nameko.rpc import rpc
from nameko.web.handlers import http
import jsonToYang
import json
import traceback
import UTSEquipment
import UTSCircuitWalkAll
import time

class toYangJsonSvc:
  name = "toYangJson"

  @http('POST', '/validateYang')
  def validateYangRequest(self, request):
    data = json.loads(request.get_data(as_text=True))
    jsonStr = data['jsonStr']
    if type(jsonStr) == dict:
      jsonStr = json.dumps(jsonStr)
    return self.validateYang(data['topic'], jsonStr)

  @rpc
  def validateYang(self, topic, jsonStr):
    #
    # Get the mappings 
    #
    mappingDetails = jsonToYang.getMappingDetails(topic)

    yangJsonStr = jsonToYang.validateYang(mappingDetails, jsonStr) 

    return yangJsonStr 

  @http('GET', '/getMappingDetails')
  def getMappingDetails(self, request):
    return self.getAllMappingDetails()

  @rpc
  def getAllMappingDetails(self):
    return jsonToYang.getAllMappingDetails() 
