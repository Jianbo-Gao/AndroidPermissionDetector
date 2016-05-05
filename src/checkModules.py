#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# check related modules.



def checkModules():
	COLOR_RED='\033[1;31m'
	COLOR_GREEN='\033[1;32m'
	COLOR_RESET='\033[1;0m'

	print "Checking related modules...",
	modules = [
		'xml',
		'numpy', 
		'matplotlib', 
		'ConfigParser', 
		'os',
		'sys', 
		'json', 
		'random', 
		'warnings', 
		'zipfile',
		'logging']
	for module in modules:
		try:
			__import__(module)
		except Exception, e:
			print "%30s" % ("["+COLOR_RED+"Success"+COLOR_RESET+"]")
			print "Please install module named " + module
			if module == 'matplotlib':
				print "If you do not use gui, you can comment out matplotlib in logRegression.py"
			return False
	print "%30s" % ("["+COLOR_GREEN+"Success"+COLOR_RESET+"]")
	return True