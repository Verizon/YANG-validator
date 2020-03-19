This folder  contains all the mapper files used by the python transformer. 

It describes how the input JSON attributes will be mapped to the YANG model fields.

The file starts with a "modelName" attribute which states the target YANG Model. 

It is followed by another attribute called "pyangObj", this is the output of the python binding file generated using

`pyang --plugindir $SOMEPATH/site-packages/pyangbind/plugin/ -f pybind vz-udm-ABC.yang openconfig-ABC.yang `


The final required attribute is "rootNode". This attribute defines the overall container tag that the output should be enclosed in.

Following the the about 3 attributes is JSON dictionary that describes the JSON output and the "type" and "tag" and how the JSON output has to be build.