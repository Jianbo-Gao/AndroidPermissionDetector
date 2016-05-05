#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Extract AndroidManifest.xml from *.apk

import zipfile
import xmlDecompiler, log

def extract(apkPath, xmlPath=None):

	log.debug(apkPath+" extracting...")

	if apkPath.endswith(".apk"):
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
			log.warning("AndroidManifest.xml not exist.")
			return False

	else:
		log.error("Unknown file type.")
		return False
