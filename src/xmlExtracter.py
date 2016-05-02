#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Extract AndroidManifest.xml from *.apk

import zipfile
import xmlDecompiler

def extract(apkPath, xmlPath=None):

	if apkPath == None:
		print "xmlExtracter.extract: apkPath is None."
		return False

	if ".apk" in apkPath:
		apk = zipfile.ZipFile(apkPath)

		if "AndroidManifest.xml" in apk.namelist():
			ap = xmlDecompiler.AXMLPrinter(apk.read("AndroidManifest.xml"))
			buff = ap.get_xml_obj().toprettyxml()

			if xmlPath == None:
				return buff

			else:
				f = open(xmlPath, "w")
				f.write(buff)
				f.close()
				return True

		else:
			print "xmlExtracter.extract: AndroidManifest.xml not exist."
			return False

	else:
		print "xmlExtracter.extract: Unknown file type."
		return False
