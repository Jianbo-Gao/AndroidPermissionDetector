#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Android Permission Detector


import os, argparse, datetime, json
from src import *

DIR_PATH = os.path.split(os.path.realpath(__file__))[0]
LOG_DIR_PATH = os.path.join(DIR_PATH, "log")
LOG_PATH = os.path.join(LOG_DIR_PATH, str(datetime.date.today())+".log")
PARAM_DIR_PATH = os.path.join(DIR_PATH, "param")
PARAM_DEFAULT_PATH = os.path.join(PARAM_DIR_PATH, "default")

def get_args():
	parser = argparse.ArgumentParser(
		description="Process args for Android Permission Detector")

	parser.add_argument('-c', '--check',
						action='store_true',
						default=False,
						dest='checkOpt',
						help='[Train&Detect]: Check related modules before use(recommend)')

	parser.add_argument('-t', '--train',
						action='store_true',
						default=False,
						dest='trainOpt',
						help='Train with samples')

	parser.add_argument('-d', '--detect',
						action='store_true',
						default=False,
						dest='testOpt',
						help='Detect apk file')

	parser.add_argument('-g', '--google',
						action='store',
						dest='googleDirPath',
						help='[Train] Google samples dir path')

	parser.add_argument('-m', '--malware',
						action='store',
						dest='malwareDirPath',
						help='[Train] Malware samples dir path')

	parser.add_argument('-p', '--param',
						action='store',
						default=None,
						dest='paramName',
						help='[Train&Detect] The name(if train, except default) of your training result')

	parser.add_argument('-f', '--file',
						action='store',
						dest='apkFilePath',
						help='[Detect] The path of apk file to detect')

	parser.add_argument('-q', '--quiet',
						action='store_true',
						default=False,
						dest='quietOpt',
						help='[Train&Detect] No output except result and error')

	parser.add_argument('-j', '--json',
						action='store_true',
						default=False,
						dest='jsonOpt',
						help='[Detect] report in json format')

	parser.add_argument('-V', '--version',
						action='version',
						version='Android Permission Detector 1.0.2')

	args = parser.parse_args()
	return args

def cmdTrain(googleDirPath, malwareDirPath, paramName=None):

	machineLearning = MachineLearning()
	return machineLearning.train(googleDirPath, malwareDirPath, paramName)

def cmdTest(testApkFilePath, paramName=None):
	machineLearning = MachineLearning()
	if paramName == None:
		paramFilePath = PARAM_DEFAULT_PATH
	else:
		paramFilePath = os.path.join(PARAM_DIR_PATH, paramName)
	return machineLearning.test(testApkFilePath, paramFilePath)

def commandLine():

	args = get_args()

	if not os.path.isdir(LOG_DIR_PATH):
		os.mkdir(LOG_DIR_PATH)

	if args.quietOpt:
		log.set_logger(filename=LOG_PATH)
	else:
		log.set_logger(filename=LOG_PATH, level="INFO:DEBUG")
		print "\n################################################################"
		print "#  Welcome to use Android Permission Detector(Version 1.0.2)!  #"
		print "################################################################\n"


	log.debug(str(args))

	if args.checkOpt:
		if not checkModules():
			log.debug("do not pass checkModules")
			exit()

	if args.trainOpt and args.testOpt:
		log.error("You cannot train and detect at the same time")
		exit()

	if args.trainOpt:
		log.info("Train start.")
		if args.googleDirPath and args.malwareDirPath:
			if args.paramName == "default":
				log.error("Please do not use 'default' as your train param name")
				log.error("Train abort")
				exit()
			if args.paramName != None:
				args.paramName = os.path.join(PARAM_DIR_PATH, args.paramName)
			result = cmdTrain(args.googleDirPath, args.malwareDirPath, args.paramName)
			if result:
				log.info("Train finish.")
				log.info("result: "+result)
		else:
			log.error("You need googleDirPath and malwareDirPath to train")
			log.error("Train abort")
			exit()

	if args.testOpt:
		log.info("Detect start.")
		if args.apkFilePath:
			if args.paramName != None:
				args.paramName = os.path.join(PARAM_DIR_PATH, args.paramName)
			result = cmdTest(args.apkFilePath, args.paramName)
			if result:
				log.info("Detect finish.")
				log.info("result: "+str(result))

				score = float(result[0])
				if score < 33.34:
					apkClass = "Low"
				elif score < 66.67:
					apkClass = "Middle"
				elif score <= 100:
					apkClass = "High"
				else:
					apkClass = "Unknown"

				if args.jsonOpt:
					report={}
					report["Control Power"] = result[0]
					report["Class"] = apkClass
					report["Dangerous Permissions"] = result[1]
					report["All Permissions"] = result[2]
					print json.dumps(report)
				else:
					print "#################"
					print "# Detect Report #"
					print "#################"
					print "[Control Power]\n"+result[0]
					print "[Class]\n"+apkClass
					print "[Dangerous Permissions]"
					for permission in result[1]:
						print permission
					print "[All Permissions]"
					for permission in result[2]:
						print permission


		else:
			log.error("You need an apk file to detect.")
			log.error("Detect abort")
			exit()


if __name__ == "__main__":
	commandLine()


