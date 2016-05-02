#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Parse AndroidManifest.xml and Extract Permissions.

import xml.dom.minidom
import json

def parse(xmlPath, permissionPath=None):

	if xmlPath == None:
		print "xmlParser.parse: xmlPath is None."
		return False

	if ".xml" in xmlPath:

		# parse AndroidManifest.xml
		try:
			dom = xml.dom.minidom.parse(xmlPath)
		except:
			print "xmlParser.parse: Parse error."
			return False

		# get permission list
		root = dom.documentElement
		permissionList = []

		root = dom.documentElement
		permissionItems = root.getElementsByTagName('uses-permission')
		for permissionItem in permissionItems:
			permission = permissionItem.getAttribute('android:name')
			permissionList.append(permission)

		if permissionPath == None:
			return permissionList

		else:
			f = open(permissionPath,"a")
			f.write(xmlPath+'\n'+json.dumps(permissionList)+'\n')
			f.close()
			return True

	else:
		print "xmlParser.parse: Unknown file type."
		return False