#
# Copyright Verizon Inc.
# Licensed under the terms of the Apache License 2.0 license.  See LICENSE file in project root for terms.
#
import json

class TransformJuniperAlarm:

    def transform(self, injson):
       outjson = dict();
       for key in injson.keys():
          if (key != 'kv') :
            outjson[key] = injson[key]
          if (key == 'kv') :
            kvlist = injson[key]
            for keyval in kvlist:
               if ('uintValue' in keyval):
                  outjson[keyval['key']] = keyval['uintValue'] 
               if ('strValue' in keyval):
                  outjson[keyval['key']] = keyval['strValue'] 
       dataa = dict()
       data = dict();
       data['data'] = outjson
       dataa['data'] = data
       return(dataa)
