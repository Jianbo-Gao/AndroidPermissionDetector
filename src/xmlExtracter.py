#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Extract AndroidManifest.xml from *.apk

import zipfile
import xmlDecompiler, log

def extract(apkPath, xmlPath=None):

	log.debug(apkPath+" extracting...")

	try:
		apk = zipfile.ZipFile(apkPath)
	except Exception, e:
		log.warning(apkPath+" is not a zip file")
		return False

	if "AndroidManifest.xml" in apk.namelist():
		try:
			ap = xmlDecompiler.AXMLPrinter(apk.read("AndroidManifest.xml"))
			buff = ap.get_xml_obj().toprettyxml()
		except Exception, e:
			log.warning(apkPath+" xml can not be decoded")
			return False

		if xmlPath == None:
			return buff

		else:
			f = open(xmlPath, "w")
			f.write(buff)
			f.close()
			return True
	else:
		log.warning(apkPath+" has no AndroidManifest.xml")
		return False
