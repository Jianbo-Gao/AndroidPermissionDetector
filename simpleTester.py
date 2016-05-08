#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# simple tester: no train, on log output, no other functions, 
# only test an apk file simply.

# For market spider and website.

import os, argparse, datetime
from src import *

DIR_PATH = os.path.split(os.path.realpath(__file__))[0]
LOG_PATH = os.path.join(DIR_PATH, "log", str(datetime.date.today())+".log")
PARAM_DIR_PATH = os.path.join(DIR_PATH, "param")
PARAM_DEFAULT_PATH = os.path.join(PARAM_DIR_PATH, "default")

def get_args():
	parser = argparse.ArgumentParser(
		description="Process args for Android Permission Tester")

	parser.add_argument('-f', '--file',
						required=True,
						action='store',
						dest='apkFilePath',
						help='[Test] The path of apk file to test')

	parser.add_argument('-V', '--version',
						action='version',
						version='Android Permission Tester 1.0.2')

	args = parser.parse_args()
	return args



def test(path):

	log.set_logger(filename=LOG_PATH, level="CRITICAL:DEBUG")

	if path:
		paramPath = PARAM_DEFAULT_PATH
		machineLearning = MachineLearning()
		result = machineLearning.test(path,paramPath)
		if result:
			log.info("Test finish.")
			log.info("result: "+str(result))
			return result
		else:
			log.error("You need an apk file to test.")
			log.error("Test abort")
			return

def commandLine():
	args = get_args()

	log.set_logger(filename=LOG_PATH, level="CRITICAL:DEBUG")
	log.debug(str(args))

	print test(args.apkFilePath)

if __name__ == "__main__":
	commandLine()