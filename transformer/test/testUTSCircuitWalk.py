# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import json
import UTSCircuitWalkAll

#with open('BCBK96TN0005.json') as json_file:
#with open('BCBK96TN0006.json') as json_file:
#with open('MGBJ98YB0001.json') as json_file:
with open('NP0B9MR10001.json') as json_file:
#with open ('I1001_100G_ASBNVA13_RCMDVAGR.json') as json_file:
#with open ('I1001_100G_ASBNVA13_RCMDVAHL.json') as json_file:
#with open ('I1001_100G_PITBPADT_PITBPAOY.json') as json_file:
#with open('I1001_100G_ASBNVA13_PITBPANS.json') as json_file:  
    data = json.load(json_file)
    UTSCircuitWalkAll.convertToYangJsonStr(data)
