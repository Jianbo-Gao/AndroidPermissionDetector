#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Android Permission Tester


import os, argparse, datetime
from src import *

DIR_PATH = os.path.split(os.path.realpath(__file__))[0]
LOG_PATH = os.path.join(DIR_PATH, "log", str(datetime.date.today())+".log")
PARAM_DIR_PATH = os.path.join(DIR_PATH, "param")
PARAM_DEFAULT_PATH = os.path.join(PARAM_DIR_PATH, "default")

def get_args():
	parser = argparse.ArgumentParser(
		description="Process args for Android Permission Tester")

	parser.add_argument('-c', '--check',
						action='store_true',
						default=False,
						dest='checkOpt',
						help='[Train&Test]: Check related modules before use(recommend)')

	parser.add_argument('-T', '--train',
						action='store_true',
						default=False,
						dest='trainOpt',
						help='Train with samples')

	parser.add_argument('-t', '--test',
						action='store_true',
						default=False,
						dest='testOpt',
						help='Test apk file')

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
						help='[Train&Test] The name(if train, except default) of your training result')

	parser.add_argument('-f', '--file',
						action='store',
						dest='apkFilePath',
						help='[Test] The path of apk file to test')

	parser.add_argument('-q', '--quiet',
						action='store_true',
						default=False,
						dest='quietOpt',
						help='[Train&Test] No output except result and error')

	parser.add_argument('-V', '--version',
						action='version',
						version='Android Permission Tester 1.0.2')

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
	print "\n##############################################################"
	print "#  Welcome to use Android Permission Tester(Version 1.0.2)!  #"
	print "##############################################################\n"

	if args.quietOpt:
		log.set_logger(filename=LOG_PATH)
	else:
		log.set_logger(filename=LOG_PATH, level="INFO:DEBUG")

	log.debug(str(args))

	if args.checkOpt:
		if not checkModules():
			log.debug("do not pass checkModules")
			exit()

	if args.trainOpt and args.testOpt:
		log.error("You cannot train and test at the same time")
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
		log.info("Test start.")
		if args.apkFilePath:
			if args.paramName != None:
				args.paramName = os.path.join(PARAM_DIR_PATH, args.paramName)
			result = cmdTest(args.apkFilePath, args.paramName)
			if result:
				log.info("Test finish.")
				log.info("result: "+str(result))
				print "[Test Result] Control Power: "+result
		else:
			log.error("You need an apk file to test.")
			log.error("Test abort")
			exit()


if __name__ == "__main__":
	commandLine()


