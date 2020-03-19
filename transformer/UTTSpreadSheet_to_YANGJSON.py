# Copyright Verizon Inc. 
# Licensed under the terms of the Apache License 2.0 license.  
# See LICENSE file in project root for terms.
import openconfig_platform
import json
import requests

from pyangbind.lib import pybindJSON

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import sys

if len (sys.argv) != 2:
   print ("Usage:python " + sys.argv[0] + " UTT_Template.xls")
   sys.exit(1)


df = pd.read_excel(sys.argv[1], sheet_name='Shelf')

#print("Column headings:")
#print(df.columns)
#Index(['Template Name', 'Front/Rear', 'Rack Template Name', 'Part Number',
#      'Material ID', 'SAP Code', 'CLEI-7', 'Manufacturer',
#             'Category/Equip Type/Model Name', 'Status', 'Shelf Name',
#             'Shelf AID Formula', 'Shelf AID Rule', 'Description', 'Weight',
#	            'Height', 'Width', 'Depth', 'Dim to Base', 'Dim to Left',
#		           'Dim to Front', 'Dim to Top', 'Subclass'],
#			         dtype='object')



op = openconfig_platform.openconfig_platform()
try:
	shelf = op.components.component.add(df['Template Name'][0])
	shelf.model.templatename = df['Template Name'][0];
	shelf.model.facing = df['Front/Rear'][0];
	shelf.model.containedtemplate = df['Rack Template Name'][0];
	shelf.model.partnumber = df['Part Number'][0];
	shelf.model.materialid = df['Material ID'][0];
	shelf.model.sapcode = df['SAP Code'][0];
	shelf.model.clei_7 = df['CLEI-7'][0];
	shelf.model.manufacturer = df['Manufacturer'][0];
	shelf.model.componenttype = df['Category/Equip Type/Model Name'][0];
	shelf.model.aidformula = df['Shelf AID Formula'][0];
	shelf.model.aidrule = df['Shelf AID Rule'][0];
	shelf.model.description = df['Description'][0];
	shelf.model.status = df['Status'][0];
	shelf.model.weight = df['Weight'][0];
	shelf.model.height = df['Height'][0];
	shelf.model.width = df['Width'][0];
	shelf.model.depth = df['Depth'][0];
	shelf.model.dimtobase = df['Dim to Base'][0];
	shelf.model.dimtoleft = df['Dim to Left'][0];
	shelf.model.dimtofront = df['Dim to Front'][0];
	shelf.model.dimtotop = df['Dim to Top'][0];
	shelf.model.subclass = df['Subclass'][0];
except KeyError as e:
    print ("KeyError Shelf:"+ str(e),file=sys.stderr)

df = pd.read_excel(sys.argv[1], sheet_name='Slot')
#print("Column headings:")
#print(df.columns)
#
# Column headings:
#Index(['Physical Slot Name (Shelf Face Plate)', 'Logical Slot Name (EMS/CLI)',
#       'Slot Number', 'Barcode Slot Position', 'Front/Rear',
#              'Traffic Bearing (Y/N)',
#	             'Slot Orientation (Vertical/Horizontal/Inverted)',
#		            'Shelf Template Name', 'Rack Template Name', 'Description', 'Model',
#			           'Height', 'Width', 'Depth', 'Dim to Base', 'Dim to Left',
#				          'Dim to Front', 'Dim to Top', 'Rel Order', 'Parent Card Template Name',
#					         'Subclass'],
#						       dtype='object')
#
#
for i in df.index:
    slot = shelf.model.slots.slot.add(df['Physical Slot Name (Shelf Face Plate)'][i])
    slot.logicalslotname = df['Logical Slot Name (EMS/CLI)'][i]
    slot.slotnumber = df['Slot Number'][i]
    slot.barcodeslotposition = df['Barcode Slot Position'][i]
    slot.side = df['Front/Rear'][i]
    slot.trafficBearing = df['Traffic Bearing (Y/N)'][i]
    slot.orientation = df['Slot Orientation (Vertical/Horizontal/Inverted)'][i]
    slot.description = df['Description'][i]
    slot.purpose = df['Model'][i]
    slot.height = df['Height'][0];
    slot.width = df['Width'][0];
    slot.depth = df['Depth'][0];
    slot.dimtobase = df['Dim to Base'][0];
    slot.dimtoleft = df['Dim to Left'][0];
    slot.dimtofront = df['Dim to Front'][0];
    slot.dimtotop = df['Dim to Top'][0];
    slot.subclass = df['Subclass'][0];
  

df = pd.read_excel(sys.argv[1], sheet_name='Card')
#print("Column headings:")
#print(df.columns)
#Column headings:
#Index(['Template Name', 'Shelf Applicable', 'Manufacturer', 'Part Number',
#       'Material ID', 'SAP Code', 'CLEI-7', 'Category/Card Type',
#              'Face Label/Model Name', 'Card AID Formula', 'Status', 'Description',
#	             'Slot Occupancy', 'Card Type', 'Number Of Ports', 'Height', 'Width',
#		            'Depth', 'Traffic Bearing (Y/N)', 'Subclass'],
#			          dtype='object')
for i in df.index:
    card = op.components.component.add(df['Template Name'][i])
    card.model.partnumber = df['Part Number'][i]
    card.model.manufacturer = df['Manufacturer'][i]
    card.model.materialid = df['Material ID'][i]
    card.model.sapcode = df['SAP Code'][i]
    card.model.clei_7 = df['CLEI-7'][i]
    card.model.componenttype = df['Category/Card Type'][i]
    card.model.aidformula = df['Card AID Formula'][i]
    card.model.status = df['Status'][i]
    card.model.description = df['Description'][i]
    card.model.trafficBearing = df['Traffic Bearing (Y/N)'][i]
    card.model.numberofports = df['Number Of Ports'][i]
    card.model.height = df['Height'][i]
    card.model.width = df['Width'][i]
    card.model.depth = df['Depth'][i]
    card.model.subclass = df['Subclass'][i]

df = pd.read_excel(sys.argv[1], sheet_name='Port')
#print("Column headings:")
#print(df.columns)

#
#
#Column headings:
#Index(['Physical Port Name on NE', 'Port Name in EMS/TL1/CLI', 'Port Number',
#       'Front/Rear', 'Card Template Name', 'Connector', 'TP_TYPE', 'Bandwidth',
#              'Digital Wrap', 'Channelization', 'Status', 'Relation Type',
#	             'Related Port', 'Parent Port Name', 'Dual Conn Name',
#		            'Dual Conn Indicator', 'Direction', 'Description',
#			           'Shelf Template Name', 'Port AID Formula', 'Port AID', 'Height',
#				          'Width', 'Depth', 'Dim to Base', 'Dim to Left', 'Dim to Front',
#					         'Dim to Top'],
#						       dtype='object')

for i in df.index:
    component = str(df['Card Template Name'][i])
    if component == 'nan':
       component = str(df['Shelf Template Name'][i])
    if component != 'nan':
       try:
           compo = op.components.component[component]
           port = compo.model.ports.port.add(df['Physical Port Name on NE'][i])
           port.portnameonems = df['Port Name in EMS/TL1/CLI'][i]
           port.portnumber = df['Port Number'][i]
           port.side = df['Front/Rear'][i]
           port.connector = df['Connector'][i]
           port.tptype = df['TP_TYPE'][i]
           port.bandwidth = df['Bandwidth'][i]
           port.digitalwrap = df['Digital Wrap'][i]
           port.channelization = df['Channelization'][i]
           port.status = df['Status'][i]
           port.relationtype = df['Relation Type'][i]
           port.relatedport = df['Related Port'][i]
           port.parentportname = df['Parent Port Name'][i]
           port.dualconnname = df['Dual Conn Name'][i]
           port.dualconnindicator = df['Dual Conn Indicator'][i]
           port.direction = df['Direction'][i]
           port.description = df['Description'][i]
           port.formula = df['Port AID Formula'][i]
           port.aid = df['Port AID'][i]
           port.height = df['Height'][i]
           port.width = df['Width'][i]
           port.depth = df['Depth'][i]
           port.dimtobase = df['Dim to Base'][i]
           port.dimtoleft = df['Dim to Left'][i]
           port.dimtofront = df['Dim to Front'][i]
           port.dimtotop = df['Dim to Top'][i]
#          print(pybindJSON.dumps(compo))
       except KeyError as e:
           print ("KeyError Port:"+ str(e),file=sys.stderr)

df = pd.read_excel(sys.argv[1], sheet_name='Slot_Card_Map')
#rint("Column headings:")
#rint(df.columns)

for i in df.index:
    component = str(df['Shelf Template Name'][i])
    if component != 'nan':
       try:
           compo = op.components.component[component]
           slot = compo.model.slots.slot[df['Physical Slot Name (Shelf Face Plate)'][i]]
           card = op.components.component[df['Card Template Name'][i]]
           slot_card = slot.cards.add(df['Card Template Name'][i])
           slot_card.card = card
       except KeyError as e:
           print ("KeyError Slot_Card_Map:"+ str(e), file=sys.stderr)
print (pybindJSON.dumps(op))
