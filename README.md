yang-validator
==============
The yang-validator project utilizes pyang to provide a method for assisting equipment vendors to utilize OpenConfig YANG JSON for existing platforms that are not already OpenConfig.     yang-validator also utilizes nameko and rabbitmq to provide a microservice for validating JSON messages are infact OpenConfig compliant.

yang-validator is also used in conjuction with jtransformer.   jtransformer can be found at: https://github.com/Verizon/YANG-transformer.      jtransformer can be used for making the actual transformations from none OpenConfig compliant YANG to OpenConfig compliant YANG using the mappings from this project.

When developing on macos there is a challenge with connecting to localhost for nameko to rabbitmq.   Edit config.yaml to specify the ip address of the location of rabbitmq.

Tested Versions
===============
* Python 3.7.3
* nameko 2.12.0  pip install 'nameko==2.12.0'
* pyang 2.0.1 .  pip install 'pyang==2.0.1'
* pyangbind 0.8.1 pip install 'pyangbind==0.8.1'


Mapping Files
=============
All mapping files are contained in transformer/mappings directory.   These files explain how to go from a propietary JSON to OpenConfig.

Models
======
OpenConfig models are contained in this directory.    Also included are specific enhancements not yet included in OpenConfig.   Care should be taken when enhancing the models without discussion with OpenConfig.


Build for Docker
================
docker build -t transformer .

Run
===
docker run -d -p 5672:5672 --hostname nameko-rabbitmq rabbitmq:3

Run Validator Python
======================
docker run --rm -it -p 8000:8000 transformer

Run in the background
=====================
docker run -d --rm -it -p 8000:8000 transformer

__Note: There is an issue on MacOS with Docker calling localhost or 127.0.0.1.   You must use your ip address with the transformer to invoke rabittmq.    You edit that ip address in the YAML file__

Test the Validator
==================
curl -i -d "{\"topic\": \"ENMV_SAMSUNG5G_CPEDATA\", \"jsonStr\": {\"perfdata\": {\"eventTime\": \"2019-03-23T02:50:00+00:00\", \"annotatedFamilyId\": \"CPE_RESOURCE\", \"neId\": \"100\", \"neType\": \"cpefama\", \"familyId\": 601, \"neVersion\": \"v_0_2_3_28\", \"indexData\": {\"0\": {\"indexId\": 0, \"indexName\": \"CPE ID\", \"indexValue\": \"20dbab03f5ec\"}}, \"payloadData\": {\"0\": {\"typeId\": 0, \"valueUnit\": \"%\", \"typeValue\": \"2.066667\", \"valueType\": \"float\", \"typeName\": \"ControlCpuUsage\"}, \"1\": {\"typeId\": 1, \"valueUnit\": \"%\", \"typeValue\": \"26.000000\", \"valueType\": \"float\", \"typeName\": \"MemoryUsage\"}, \"2\": {\"typeId\": 2, \"valueUnit\": \"%\", \"typeValue\": \"10.000000\", \"valueType\": \"float\", \"typeName\": \"DiskUsage\"}, \"3\": {\"typeId\": 3, \"valueUnit\": \"\u00b0C\", \"typeValue\": \"27.000000\", \"valueType\": \"float\", \"typeName\": \"Temperature\"}}}}}" localhost:8000/validateYang

Run Standalone
==============
nameko run toYangJsonSvc


View Docker logs
================
First get the container id
docker ps

then execute bash on container id to see logs
docker exec -it 36dd5a020491 bash

Stop the container
==================
docker stop 9158083d86fa


