#
# Copyright Verizon Inc.
# Licensed under the terms of the Apache License 2.0 license.  See LICENSE file in project root for terms.
#
import json

system = None

def process(system):
   print (json.dumps(system, indent=4))

def buildDict(tsd,prefix):
   prefixArray = prefix.split('/')
   currentdict = tsd
   for val in prefixArray:
      if ('[' in val):
          head = val.split('[')[0]
          key = val.split('[')[1]
          value= key.split('=')[1]
          key = key.split('=')[0]
          value = value.replace('\'','').replace(']','')
          if (head not in currentdict):
             currentdict[head] = dict()
             currentdict = currentdict[head]
          else:          
             currentdict = currentdict[head]
          currentdict[value] = dict()
          currentdict[value][key] =  value
          print (head+":"+key+":"+value)
          continue
      if (val in currentdict):
          currentdict = currentdict[val]
          continue
      if (val != "" and '[' not in val and val not in currentdict):
          currentdict[val] = dict()
          currentdict = currentdict[val]
   return (tsd)


#f = open("interface_capture_10_15-19.txt", "r")
f = open("Component_sensor_output_on_BSYS_062419.txt.1", "r")
print ("opening file")
x = f.readline()
while x != "":
  x = x.strip()
  if (x.startswith('key: __timestamp__') == True):
     if (system != None):
       process(system)
     else:
       system = dict()

     tsv = f.readline()
     tsv = tsv.strip()
     tsv = tsv.split(':')[1]
     tsd = dict()
     tsd['__timestamp__'] = tsv
     system['system'] = tsd
  if (x.startswith('key: __prefix__') == True):
     prefixval = f.readline()
     prefixval = prefixval.split('ue:')[1]
     prefixval = prefixval.strip()
     tsd['__prefix__'] = prefixval
     tsd = buildDict(tsd,prefixval)

  x = f.readline()

print ("closing file")
if (system != None):
   process(system)
