1. generate python from Yang
python findplugin.py is used for plugin directory

pyang --plugindir `python findplugin.py` -f pybind models/samsung-cpe-perfdata-udm@2018-08-15.yang > samsung_yang.py

2.  To list tree of yang model
pyang -f tree models/samsung-cpe-perfdata-udm@2018-08-15.yang


Start nameko service and server:

1. docker run -p 5672:5672 --hostname nameko-rabbitmq rabbitmq:3

2. nameko run toYangJsonSvc

2a. nameko through remote server:  
nameko run toYangJsonSvc --broker amqp://guest:guest@10.134.214.149:5672

Test validator method
curl -i -d "{\"topic\": \"ENMV_SAMSUNG5G_CPEDATA\", \"jsonStr\": {\"perfdata\": {\"eventTime\": \"2019-03-23T02:50:00+00:00\", \"annotatedFamilyId\": \"CPE_RESOURCE\", \"neId\": \"100\", \"neType\": \"cpefama\", \"familyId\": 601, \"neVersion\": \"v_0_2_3_28\", \"indexData\": {\"0\": {\"indexId\": 0, \"indexName\": \"CPE ID\", \"indexValue\": \"20dbab03f5ec\"}}, \"payloadData\": {\"0\": {\"typeId\": 0, \"valueUnit\": \"%\", \"typeValue\": \"2.066667\", \"valueType\": \"float\", \"typeName\": \"ControlCpuUsage\"}, \"1\": {\"typeId\": 1, \"valueUnit\": \"%\", \"typeValue\": \"26.000000\", \"valueType\": \"float\", \"typeName\": \"MemoryUsage\"}, \"2\": {\"typeId\": 2, \"valueUnit\": \"%\", \"typeValue\": \"10.000000\", \"valueType\": \"float\", \"typeName\": \"DiskUsage\"}, \"3\": {\"typeId\": 3, \"valueUnit\": \"\u00b0C\", \"typeValue\": \"27.000000\", \"valueType\": \"float\", \"typeName\": \"Temperature\"}}}}}" localhost:8000/validateYang


This hits the docer server on ndl-docker1:
curl -i -d "{\"topic\": \"ENMV_SAMSUNG5G_CPEDATA\", \"jsonStr\": {\"eventTime\": \"2019-03-23T02:50:00+00:00\", \"data\": [{\"valueUnit\": \"%\", \"typeId\": 0, \"typeValue\": \"2.066667\", \"valueType\": \"float\", \"typeName\": \"ControlCpuUsage\"}, {\"valueUnit\": \"%\", \"typeId\": 1, \"typeValue\": \"26.000000\", \"valueType\": \"float\", \"typeName\": \"MemoryUsage\"}, {\"valueUnit\": \"%\", \"typeId\": 2, \"typeValue\": \"10.000000\", \"valueType\": \"float\", \"typeName\": \"DiskUsage\"}, {\"valueUnit\": \"\u00b0C\", \"typeId\": 3, \"typeValue\": \"27.000000\", \"valueType\": \"float\", \"typeName\": \"Temperature\"}], \"annotatedFamilyId\": \"CPE_RESOURCE\", \"neId\": \"100\", \"indexes\": [{\"indexName\": \"CPE ID\", \"indexId\": 0, \"indexValue\": \"20dbab03f5ec\"}], \"neType\": \"cpefama\", \"familyId\": 601, \"neVersion\": \"v_0_2_3_28\"}}" http://10.134.214.149:8000/jsonToYangJson



Start pulsar
~/apache-pulsar-2.3.0/bin/pulsar standalone --advertised-address 127.0.0.1



Adding new python modules
/usr/local/bin/pip install confluent-kafka --proxy proxy.ebiz.verizon.com:80 --user
